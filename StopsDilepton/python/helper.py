import PhysicsTools.HeppyCore.framework.config as cfg
import os

#import subprocess
#import os.path
#
#from RootTools.fwlite.Database import Database
#
#def getCachedFiles( name, dpmdir, subdirs,server, verbose  ):
#    basedir="root://%s/"%server
#    prot="xrd"
#    dpmdir = "/cms/"+dpmdir
#    lscommand= prot + " " + server + "  ls  " +dpmdir
#    dirs={}
#    allfiles=[]
#    cache = Database("signal_cache.db", "fileCache", ["name"])
#    nFiles = cache.contains({'name':name})
#    if nFiles:
#        print 'Found sample in cache, adding %i file'%nFiles
#        files = cache.getDicts({'name':name})
#        for f in files:
#            allfiles.append(f["value"])
#    else:
#        print 'Sample in cache not found'
#        for subdir in subdirs:
#            #gfalout  = subprocess.Popen(["gfal-ls "+ basedir+"/"+dpmdir+'/'+subdir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#            lsout = subprocess.Popen([ lscommand ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#            for f in lsout.stdout.readlines():
#                f =  f.rsplit()
#                if len(f)==0:
#                    continue
#                f=f[-1]
#                if not f.endswith("root"):
#                    continue

def getFilesFromDAS( dataset, instance, limit): 
    def _dasPopen(dbs):
        if 'LSB_JOBID' in os.environ:
            raise RuntimeError, "Trying to do a DAS query while in a LXBatch job (env variable LSB_JOBID defined)\nquery was: %s" % dbs
        if 'X509_USER_PROXY' in os.environ:
            dbs += " --key {0} --cert {0}".format(os.environ['X509_USER_PROXY'])
        print 'DAS query\t: %s'%dbs
        return os.popen(dbs)

    sampleName = dataset.rstrip('/')
    query, qwhat = sampleName, "dataset"
    if "#" in sampleName: qwhat = "block"

    dbs='das_client --query="file %s=%s instance=prod/%s" --limit %i'%(qwhat,query, instance, limit)
    dbsOut = _dasPopen(dbs).readlines()
    
    files = []
    for line in dbsOut:
        if line.startswith('/store/'):
            line = line.rstrip()
            files.append(line)

    return files

def getFilesOnDPM(dataset,pattern=".*root"):
    import re
    from CMGTools.Production.dataset import getDatasetFromCache, writeDatasetToCache
    cache_name = 'HEPHY%{path}%{pattern}.pck'.format(path = dataset.replace('/','_'), pattern = pattern)
    try:
        files = getDatasetFromCache(cache_name)
    except IOError:
        files = [ 'root://hephyse.oeaw.ac.at//%s'%x for x in  getFilesFromDAS(dataset, instance='phys03', limit=0) if re.match(pattern,x) ] 
        if len(files) == 0:
            raise RuntimeError, "ERROR making dataset: no files found under %s matching '%s'" % (dataset,pattern)
        writeDatasetToCache(cache_name, files)
    return files

def makeMyPrivateMCComponentFromDPM(name, dataset, xSec=1):

    component = cfg.MCComponent(
        dataset=dataset,
        name = name,
        #files = [ 'root://hephyse.oeaw.ac.at/%s'%f for f in getFilesFromDAS(dataset, instance='phys03') ],
        files = getFilesOnDPM( dataset, pattern=".*root"),
        xSection = xSec,
        nGenEvents = 1,
        triggers = [],
        effCorrFactor = 1,
    )

    return component
