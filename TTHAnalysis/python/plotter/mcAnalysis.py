#!/usr/bin/env python
#from tree2yield import *
from CMGTools.TTHAnalysis.plotter.tree2yield import *
from CMGTools.TTHAnalysis.plotter.projections import *
import pickle, re

## These must be defined as standalone functions, to allow runing them in parallel
def _runYields(args):
    key,tty,cuts,noEntryLine = args
    return (key, tty.getYields(cuts,noEntryLine=noEntryLine))

def _runPlot(args):
    key,tty,plotspec,cut = args
    #timer = ROOT.TStopwatch()
    #print "Starting plot %s for %s, %s" % (plotspec.name,key,tty._cname)
    ret = (key,tty.getPlot(plotspec,cut))
    #print "Done plot %s for %s, %s in %s s" % (plotspec.name,key,tty._cname,timer.RealTime())
    return ret

class MCAnalysis:
    def __init__(self,samples,options):
        self._options = options
        self._allData     = {}
        self._data        = []
        self._signals     = []
        self._backgrounds = [] 
        self._isSignal    = {}
        self._rank        = {} ## keep ranks as in the input text file
        self._projection  = Projections(options.project, options) if options.project != None else None
        self._premap = []
        self._optionsOnlyProcesses = {}
        defaults = {}
        for premap in options.premap:
            to,fro = premap.split("=")
            if to[-1] == ":": to = to[:-1]
            to = to.strip()
            for k in fro.split(","):
                self._premap.append((re.compile(k.strip()+"$"), to))
        for line in open(samples,'r'):
            if re.match("\s*#.*", line): continue
            line = re.sub(r"(?<!\\)#.*","",line)  ## regexp black magic: match a # only if not preceded by a \!
            line = line.replace(r"\#","#")        ## and now we just unescape the remaining #'s
            extra = {}
            if ";" in line:
                (line,more) = line.split(";")[:2]
                for setting in [f.replace(';',',').strip() for f in more.replace('\\,',';').split(',')]:
                    if "=" in setting: 
                        (key,val) = [f.strip() for f in setting.split("=")]
                        extra[key] = eval(val)
                    else: extra[setting] = True
            field = [f.strip() for f in line.split(':')]
            if len(field) == 1 and field[0] == "*":
                if len(self._allData): raise RuntimeError, "MCA defaults ('*') can be specified only before all processes"
                #print "Setting the following defaults for all samples: "
                for k,v in extra.iteritems():
                    #print "\t%s: %r" % (k,v)
                    defaults[k] = v
                continue
            else:
                for k,v in defaults.iteritems():
                    if k not in extra: extra[k] = v
            if len(field) <= 1: continue
            if "SkipMe" in extra and extra["SkipMe"] == True and not options.allProcesses: continue
            signal = False
            pname = field[0]
            if pname[-1] == "+": 
                signal = True
                pname = pname[:-1]
            ## if we remap process names, do it
            for x,newname in self._premap:
                if re.match(x,pname):
                    pname = newname
           ## If we have a user-defined list of processes as signal
            if len(options.processesAsSignal):
                signal = False
                for p0 in options.processesAsSignal:
                    for p in p0.split(","):
                        if re.match(p+"$", pname): signal = True
            ## Options only processes
            if field[1] == "-": 
                self._optionsOnlyProcesses[field[0]] = extra
                self._isSignal[field[0]] = signal
                continue
            ## If we have a selection of process names, apply it
            skipMe = (len(options.processes) > 0)
            for p0 in options.processes:
                for p in p0.split(","):
                    if re.match(p+"$", pname): skipMe = False
            for p0 in options.processesToExclude:
                for p in p0.split(","):
                    if re.match(p+"$", pname): skipMe = True
            for p0 in options.filesToExclude:
                for p in p0.split(","):
                    if re.match(p+"$", field[1]): skipMe = True
            if skipMe: continue
            ## 
            treename = extra["TreeName"] if "TreeName" in extra else options.tree 
            rootfile = "%s/%s/%s/%s_tree.root" % (options.path, field[1].strip(), treename, treename)
            if options.remotePath:
                rootfile = "root:%s/%s/%s_tree.root" % (options.remotePath, field[1].strip(), treename)
            elif os.path.exists(rootfile+".url"): #(not os.path.exists(rootfile)) and :
                rootfile = open(rootfile+".url","r").readline().strip()
            elif (not os.path.exists(rootfile)) and os.path.exists("%s/%s/%s/tree.root" % (options.path, field[1].strip(), treename)):
                # Heppy calls the tree just 'tree.root'
                rootfile = "%s/%s/%s/tree.root" % (options.path, field[1].strip(), treename)
                treename = "tree"
            elif (not os.path.exists(rootfile)) and os.path.exists("%s/%s/%s/tree.root.url" % (options.path, field[1].strip(), treename)):
                # Heppy calls the tree just 'tree.root'
                rootfile = "%s/%s/%s/tree.root" % (options.path, field[1].strip(), treename)
                rootfile = open(rootfile+".url","r").readline().strip()
                treename = "tree"
            pckfile = options.path+"/%s/skimAnalyzerCount/SkimReport.pck" % field[1].strip()
            tty = TreeToYield(rootfile, options, settings=extra, name=pname, cname=field[1].strip(), treename=treename)
            if signal: 
                self._signals.append(tty)
                self._isSignal[pname] = True
            elif pname == "data":
                self._data.append(tty)
            else:
                self._isSignal[pname] = False
                self._backgrounds.append(tty)
            if pname in self._allData: self._allData[pname].append(tty)
            else                        : self._allData[pname] =     [tty]
            if "data" not in pname:
                pckobj  = pickle.load(open(pckfile,'r'))
                counters = dict(pckobj)
                tty.setFullNevt(int(counters['All Events']))
                if ('Sum Weights' in counters) and options.weight:
                    nevt = counters['Sum Weights']
                    scale = "genWeight*%s/%g" % (field[2], 0.001*nevt)
                else:
                    nevt = counters['All Events']
                    scale = "%s/%g" % (field[2], 0.001*nevt)
                if len(field) == 4: scale += "*("+field[3]+")"
                for p0,s in options.processesToScale:
                    for p in p0.split(","):
                        if re.match(p+"$", pname): scale += "*("+s+")"
                tty.setScaleFactor(scale)
                if options.fullSampleYields:
                    fullYield = 0.0;
                    try:
                        fullYield = float(eval(field[2])) * 1000. * options.lumi
                        if len(field) == 4:
                            try:
                                fullYield = fullYield * float(eval(field[3]))
                            except:
                                pass
                    except:
                        pass
                    tty.setFullYield(fullYield)
            elif len(field) == 3:
                tty.setScaleFactor(field[2])
                if options.fullSampleYields:
                    try:
                        pckobj  = pickle.load(open(pckfile,'r'))
                        counters = dict(pckobj)
                        nevt = counters['All Events']
                        tty.setFullYield(nevt)
                        tty.setFullNevt(int(nevt))
                    except:
                        tty.setFullYield(0)
                        tty.setFullNevt(0)
            else:
                try:
                    pckobj  = pickle.load(open(pckfile,'r'))
                    counters = dict(pckobj)
                    tty.setFullNevt(int(counters['All Events']))
                except:
                    tty.setFullNevt(0)
            # Adjust free-float and fixed from command line
            for p0 in options.processesToFloat:
                for p in p0.split(","):
                    if re.match(p+"$", pname): tty.setOption('FreeFloat', True)
            for p0 in options.processesToFix:
                for p in p0.split(","):
                    if re.match(p+"$", pname): tty.setOption('FreeFloat', False)
            for p0, p1 in options.processesToPeg:
                for p in p0.split(","):
                    if re.match(p+"$", pname): tty.setOption('PegNormToProcess', p1)
            if pname not in self._rank: self._rank[pname] = len(self._rank)
        #if len(self._signals) == 0: raise RuntimeError, "No signals!"
        #if len(self._backgrounds) == 0: raise RuntimeError, "No backgrounds!"
    def listProcesses(self):
        ret = self._allData.keys()[:]
        ret.sort(key = lambda n : self._rank[n])
        return ret
    def listOptionsOnlyProcesses(self):
        return self._optionsOnlyProcesses.keys()
    def isBackground(self,process):
        return process != 'data' and not self._isSignal[process]
    def isSignal(self,process):
        return self._isSignal[process]
    def listSignals(self,allProcs=False):
        ret = [ p for p in self._allData.keys() if p != 'data' and self._isSignal[p] and (self.getProcessOption(p, 'SkipMe') != True or allProcs) ]
        ret.sort(key = lambda n : self._rank[n])
        return ret
    def listBackgrounds(self,allProcs=False):
        ret = [ p for p in self._allData.keys() if p != 'data' and not self._isSignal[p] and (self.getProcessOption(p, 'SkipMe') != True or allProcs) ]
        ret.sort(key = lambda n : self._rank[n])
        return ret
    def hasProcess(self,process):
        return process in self._allData
    def scaleProcess(self,process,scaleFactor):
        for tty in self._allData[process]: tty.setScaleFactor(scaleFactor)
    def scaleUpProcess(self,process,scaleFactor):
        for tty in self._allData[process]: 
            tty.setScaleFactor( "((%s) * (%s))" % (tty.getScaleFactor(),scaleFactor) )
    def getProcessOption(self,process,name,default=None):
        if process in self._allData:
            return self._allData[process][0].getOption(name,default=default)
        elif process in self._optionsOnlyProcesses:
            options = self._optionsOnlyProcesses[process]
            return options[name] if name in options else default
        else: raise RuntimeError, "Can't get option %s for undefined process %s" % (name,process)
    def setProcessOption(self,process,name,value):
        if process in self._allData:
            return self._allData[process][0].setOption(name,value)
        elif process in self._optionsOnlyProcesses:
            self._optionsOnlyProcesses[process][name] = value
        else: raise RuntimeError, "Can't set option %s for undefined process %s" % (name,process)
    def getScales(self,process):
        return [ tty.getScaleFactor() for tty in self._allData[process] ] 
    def getYields(self,cuts,process=None,nodata=False,makeSummary=False,noEntryLine=False):
        ## first figure out what we want to do
        tasks = []
        for key,ttys in self._allData.iteritems():
            if key == 'data' and nodata: continue
            if process != None and key != process: continue
            for tty in ttys:
                tasks.append((key,tty,cuts,noEntryLine))
        ## then do the work
        retlist = []
        if self._options.jobs == 0: 
            retlist = map(_runYields, tasks)
        else:
            #from sys import stderr
            #stderr.write("Will run %d tasks on %d multiple treads\n" % (len(tasks),self._options.jobs))
            from multiprocessing import Pool
            pool = Pool(self._options.jobs)
            retlist  = pool.map(_runYields, tasks)
            pool.close()
            pool.join()
        ## then gather results with the same process
        mergemap = {}
        for (k,v) in retlist: 
            if k not in mergemap: mergemap[k] = []
            mergemap[k].append(v)
        ## and finally merge them
        ret = dict([ (k,mergeReports(v)) for k,v in mergemap.iteritems() ])

        rescales = []
        self.compilePlotScaleMap(self._options.plotscalemap,rescales)
        for p,v in ret.items():
            for regexp in rescales:
                if re.match(regexp[0],p): ret[p]=[v[0], [x*regexp[1] for x in v[1]]]

        regroups = [] # [(compiled regexp,target)]
        self.compilePlotMergeMap(self._options.plotmergemap,regroups)
        for regexp in regroups: ret = self.regroupReports(ret,regexp)

        # if necessary project to different lumi, energy,
        if self._projection:
            self._projection.scaleReport(ret)
        # and comute totals
        if makeSummary:
            allSig = []; allBg = []
            for (key,val) in ret.iteritems():
                if key != 'data':
                    if self._isSignal[key]: allSig.append(ret[key])
                    else: allBg.append(ret[key])
            if self._signals and not ret.has_key('signal') and len(allSig) > 0:
                ret['signal'] = mergeReports(allSig)
            if self._backgrounds and not ret.has_key('background') and len(allBg) > 0:
                ret['background'] = mergeReports(allBg)
        return ret
    def getPlotsRaw(self,name,expr,bins,cut,process=None,nodata=False,makeSummary=False):
        return self.getPlots(PlotSpec(name,expr,bins,{}),cut,process,nodata,makeSummary)
    def getPlots(self,plotspec,cut,process=None,nodata=False,makeSummary=False):
        ret = { }
        allSig = []; allBg = []
        tasks = []
        for key,ttys in self._allData.iteritems():
            if key == 'data' and nodata: continue
            if process != None and key != process: continue
            for tty in ttys:
                tasks.append((key,tty,plotspec,cut))
        retlist = []
        if self._options.jobs == 0: 
            retlist = map(_runPlot, tasks)
        else:
            #from sys import stderr
            #stderr.write("Will run %d tasks on %d multiple treads\n" % (len(tasks),self._options.jobs))
            from multiprocessing import Pool
            pool = Pool(self._options.jobs)
            retlist  = pool.map(_runPlot, tasks)
            pool.close()
            pool.join()
        ## then gather results with the same process
        mergemap = {}
        for (k,v) in retlist: 
            if k not in mergemap: mergemap[k] = []
            mergemap[k].append(v)
        ## and finally merge them
        ret = dict([ (k,mergePlots(plotspec.name+"_"+k,v)) for k,v in mergemap.iteritems() ])

        rescales = []
        self.compilePlotScaleMap(self._options.plotscalemap,rescales)
        for p,v in ret.items():
            for regexp in rescales:
                if re.match(regexp[0],p): v.Scale(regexp[1])

        regroups = [] # [(compiled regexp,target)]
        self.compilePlotMergeMap(self._options.plotmergemap,regroups)
        for regexp in regroups: ret = self.regroupPlots(ret,regexp,plotspec)

        # if necessary project to different lumi, energy,
        if self._projection:
            self._projection.scalePlots(ret)
        if makeSummary:
            allSig = [v for k,v in ret.iteritems() if k != 'data'and self._isSignal[k] == True  ]
            allBg  = [v for k,v in ret.iteritems() if k != 'data'and self._isSignal[k] == False ]
            if self._signals and not ret.has_key('signal') and len(allSig) > 0:
                ret['signal'] = mergePlots(plotspec.name+"_signal", allSig)
                ret['signal'].summary = True
            if self._backgrounds and not ret.has_key('background') and len(allBg) > 0:
                ret['background'] = mergePlots(plotspec.name+"_background",allBg)
                ret['background'].summary = True
        return ret
    def prettyPrint(self,reports,makeSummary=True):
        allSig = []; allBg = []
        for key in reports:
            if key != 'data':
                if self._isSignal[key]: allSig.append((key,reports[key]))
                else: allBg.append((key,reports[key]))
        allSig.sort(key = lambda (n,v): self._rank[n])
        allBg.sort( key = lambda (n,v): self._rank[n])
        table = allSig + allBg
        if makeSummary:
            if len(allSig)>1:
                table.append(('ALL SIG',mergeReports([v for n,v in allSig])))
            if len(allBg)>1:
                table.append(('ALL BKG',mergeReports([v for n,v in allBg])))
        if "data" in reports: table += [ ('DATA', reports['data']) ]

        # maximum length of the cut descriptions
        clen = max([len(cut) for cut,yields in table[0][1]]) + 3
        cfmt = "%%-%ds" % clen;

        fmtlen = 10
        nfmtL = "  %8d"
        nfmtS = "  %8.2f" if self._options.weight else nfmtL
        nfmtX = "  %8.4f" if self._options.weight else nfmtL

        if self._options.errors:
            nfmtS+=u" %7.2f"
            nfmtX+=u" %7.4f"
            nfmtL+=u" %7.2f"
            fmtlen+=9
        if self._options.fractions:
            nfmtS+=" %7.1f%%"
            nfmtX+=" %7.1f%%"
            nfmtL+=" %7.1f%%"
            fmtlen+=8

        if self._options.txtfmt == "text":
            print "CUT".center(clen),
            for h,r in table: 
                if len("   "+h) <= fmtlen:
                    print ("   "+h).center(fmtlen),
                elif len(h) <= fmtlen:
                    print h.center(fmtlen),
                else:
                    print h[:fmtlen],
            print ""
            print "-"*((fmtlen+1)*len(table)+clen)
            for i,(cut,dummy) in enumerate(table[0][1]):
                print cfmt % cut,
                for name,report in table:
                    (nev,err,nev_run_upon) = report[i][1]
                    den = report[i-1][1][0] if i>0 else 0
                    fraction = nev/float(den) if den > 0 else 1
                    if self._options.nMinusOne: 
                        fraction = report[-1][1][0]/nev if nev > 0 else 1
                    toPrint = (nev,)
                    if self._options.errors:    toPrint+=(err,)
                    if self._options.fractions: toPrint+=(fraction*100,)
                    if self._options.weight and nev < 1000: print ( nfmtS if nev > 0.2 else nfmtX) % toPrint,
                    else                                  : print nfmtL % toPrint,
                print ""
        elif self._options.txtfmt in ("tsv","csv","dsv","ssv"):
            sep = { 'tsv':"\t", 'csv':",", 'dsv':';', 'ssv':' ' }[self._options.txtfmt]
            if len(table[0][1]) == 1:
                for k,r in table:
                    if sep in k:
                        if self._options.txtfmt in ("tsv","ssv"):
                            k = k.replace(sep,"_")
                        else:
                            k = '"'+k.replace('"','""')+'"'
                    (nev,err,fraction) = r[0][1][0], r[0][1][1], 1.0
                    toPrint = (nev,)
                    if self._options.errors:    toPrint+=(err,)
                    if self._options.fractions: toPrint+=(fraction*100,)
                    if self._options.weight and nev < 1000: ytxt = ( nfmtS if nev > 0.2 else nfmtX) % toPrint
                    else                                  : ytxt = nfmtL % toPrint
                    print "%s%s%s" % (k,sep,sep.join(ytxt.split()))
                print ""

    def _getYields(self,ttylist,cuts):
        return mergeReports([tty.getYields(cuts) for tty in ttylist])
    def __str__(self):
        mystr = ""
        for a in self._allData:
            mystr += str(a) + '\n' 
        for a in self._data:
            mystr += str(a) + '\n' 
        for a in self._signals:
            mystr += str(a) + '\n' 
        for a in self._backgrounds:
            mystr += str(a) + '\n'
        return mystr[:-1]
    def processEvents(self,eventLoop,cut):
        for p in self.listProcesses():
            for tty in self._allData[p]:
                tty.processEvents(eventLoop,cut)
    def compilePlotMergeMap(self,inlist,relist):
        for m in inlist:
            to,fro = m.split("=")
            if to[-1] == "+": to = to[:-1]
            else: raise RuntimeError, 'Incorrect plotmergemap format: %s'%m
            to = to.strip()
            for k in fro.split(","):
                relist.append((re.compile(k.strip()+"$"), to))
    def compilePlotScaleMap(self,inlist,relist):
        for m in inlist:
            dset,scale = m.split("=")
            if dset[-1] == "*": dset = dset[:-1]
            else: raise RuntimeError, 'Incorrect plotscalemap format: %s'%m
            relist.append((re.compile(dset.strip()+"$"),float(scale)))
    def regroupReports(self,pmap,regexp):
        patt, to = regexp
        mergemap={}
        for (k,v) in pmap.items():
            k2 = k
            if k2 != to and re.match(patt,k2): k2 = to
            if k2 not in mergemap: mergemap[k2]=[]
            mergemap[k2].append(v)
        return dict([ (k,mergeReports(v)) for k,v in mergemap.iteritems() ])
    def regroupPlots(self,pmap,regexp,pspec):
        patt, to = regexp
        mergemap={}
        for (k,v) in pmap.items():
            k2 = k
            if k2 != to and re.match(patt,k2): k2 = to
            if k2 not in mergemap: mergemap[k2]=[]
            mergemap[k2].append(v)
        return dict([ (k,mergePlots(pspec.name+"_"+k,v)) for k,v in mergemap.iteritems() ])
    def stylePlot(self,process,plot,pspec,mayBeMissing=False):
        if process in self._allData:
            for tty in self._allData[process]: 
                tty._stylePlot(plot,pspec)
                break
        elif process in self._optionsOnlyProcesses:
            opts = self._optionsOnlyProcesses[process]
            stylePlot(plot, pspec, lambda key,default : opts[key] if key in opts else default)
        elif not mayBeMissing:
            raise KeyError, "Process %r not found" % process


def addMCAnalysisOptions(parser,addTreeToYieldOnesToo=True):
    if addTreeToYieldOnesToo: addTreeToYieldOptions(parser)
    parser.add_option("-j", "--jobs",           dest="jobs", type="int", default=0, help="Use N threads");
    parser.add_option("-P", "--path",           dest="path",        type="string", default="./",      help="path to directory with input trees and pickle files (./)") 
    parser.add_option("--RP", "--remote-path",   dest="remotePath",  type="string", default=None,      help="path to remote directory with trees, but not other metadata (default: same as path)") 
    parser.add_option("-p", "--process", dest="processes", type="string", default=[], action="append", help="Processes to print (comma-separated list of regexp, can specify multiple ones)");
    parser.add_option("--pg", "--pgroup", dest="premap", type="string", default=[], action="append", help="Group proceses into one. Syntax is '<newname> := (comma-separated list of regexp)', can specify multiple times. Note tahat it is applied _before_ -p, --sp and --xp");
    parser.add_option("--xf", "--exclude-files", dest="filesToExclude", type="string", default=[], action="append", help="Files to exclude (comma-separated list of regexp, can specify multiple ones)");
    parser.add_option("--xp", "--exclude-process", dest="processesToExclude", type="string", default=[], action="append", help="Processes to exclude (comma-separated list of regexp, can specify multiple ones)");
    parser.add_option("--sp", "--signal-process", dest="processesAsSignal", type="string", default=[], action="append", help="Processes to set as signal (overriding the '+' in the text file)");
    parser.add_option("--float-process", "--flp", dest="processesToFloat", type="string", default=[], action="append", help="Processes to set as freely floating (overriding the 'FreeFloat' in the text file; affects e.g. mcPlots with --fitData)");
    parser.add_option("--fix-process", "--fxp", dest="processesToFix", type="string", default=[], action="append", help="Processes to set as not freely floating (overriding the 'FreeFloat' in the text file; affects e.g. mcPlots with --fitData)");
    parser.add_option("--peg-process", dest="processesToPeg", type="string", default=[], nargs=2, action="append", help="--peg-process X Y make X scale as Y (equivalent to set PegNormToProcess=Y in the mca.txt)");
    parser.add_option("--scale-process", dest="processesToScale", type="string", default=[], nargs=2, action="append", help="--scale-process X Y make X scale by Y (equivalent to add it in the mca.txt)");
    parser.add_option("--AP", "--all-processes", dest="allProcesses", action="store_true", help="Include also processes that are marked with SkipMe=True in the MCA.txt")
    parser.add_option("--project", dest="project", type="string", help="Project to a scenario (e.g 14TeV_300fb_scenario2)")
    parser.add_option("--plotgroup", dest="plotmergemap", type="string", default=[], action="append", help="Group plots into one. Syntax is '<newname> := (comma-separated list of regexp)', can specify multiple times. Note it is applied after plotting.")
    parser.add_option("--scaleplot", dest="plotscalemap", type="string", default=[], action="append", help="Scale plots by this factor (before grouping). Syntax is '<newname> := (comma-separated list of regexp)', can specify multiple times.")

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser(usage="%prog [options] tree.root cuts.txt")
    addMCAnalysisOptions(parser)
    (options, args) = parser.parse_args()
    tty = TreeToYield(args[0],options) if ".root" in args[0] else MCAnalysis(args[0],options)
    cf  = CutsFile(args[1],options)
    for cutFile in args[2:]:
        temp = CutsFile(cutFile,options)
        for cut in temp.cuts():
            cf.add(cut[0],cut[1])
    report = tty.getYields(cf)#, process=options.process)
    tty.prettyPrint(report)
