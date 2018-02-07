##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES         ##
## skim condition: >= 1 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

# WTF?
jsonAna.useLumiBlocks = True

storePackedCandidates = False
####### Leptons  #####
# lep collection
lepAna.packedCandidates = 'packedPFCandidates'

## ELECTRONS
lepAna.loose_electron_pt  = 5
eleID = "CBID"
doElectronScaleCorrections = False

keepLHEWeights =  getHeppyOption("keepLHEweights",True)

if eleID == "CBID":
  lepAna.loose_electron_id  = "POG_Cuts_ID_SPRING16_25ns_v1_ConvVetoDxyDz_Veto" # no Iso
  lepAna.loose_electron_lostHits = 999. # no cut
  lepAna.loose_electron_dxy    = 0.1
  lepAna.loose_electron_dz     = 0.2

  lepAna.inclusive_electron_id  = ""#"POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto_full5x5"
  lepAna.inclusive_electron_lostHits = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

elif eleID == "MVAID":
  inclusive_electron_id  = "" # same as in susyCore

  #lepAna.loose_electron_id = "POG_MVA_ID_Phys14_NonTrig_VLoose" # Phys14 era
  lepAna.loose_electron_id = "POG_MVA_ID_Spring15_NonTrig_VLoose" # Spring15 25ns era

elif eleID == "Incl": # as inclusive as possible
  lepAna.loose_electron_id  = ""
  lepAna.loose_electron_lostHits = 999. # no cut
  lepAna.loose_electron_dxy    = 999.
  lepAna.loose_electron_dz     = 999.

  lepAna.inclusive_electron_id  = ""
  lepAna.inclusive_electron_lostHits = 999.  # no cut
  lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
  lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

## MUONS
# store everything
lepAna.inclusive_muon_dxy = 999.
lepAna.inclusive_muon_dz  = 999.
lepAna.inclusive_muon_eta = 999.
lepAna.inclusive_muon_id = None#   POG_ID_Loose
lepAna.inclusive_muon_pt = 0.

lepAna.loose_muon_pt  = 5

# Isolation
isolation = "relIso03"

if isolation == "miniIso":
  # do miniIso
  lepAna.doMiniIsolation = True
  lepAna.miniIsolationPUCorr = 'rhoArea'
  lepAna.miniIsolationVetoLeptons = None
  lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
  lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
elif isolation == "relIso03":
  # normal relIso03
  lepAna.ele_isoCorr = "rhoArea"
  lepAna.mu_isoCorr = "deltaBeta"

  lepAna.loose_electron_relIso = 0.5
  lepAna.loose_muon_relIso = 0.5

if doElectronScaleCorrections:
    era = '25ns'
    lepAna.doElectronScaleCorrections = {
    'data' : 'EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_Golden22June_approval',

    'GBRForest': ('$CMSSW_BASE/src/CMGTools/RootTools/data/egamma_epComb_GBRForest_76X.root',
    'gedelectron_p4combination_'+era),
    'isSync': False
    }

# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 1
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10
jetAna.recalibrateJets =  True 
jetAna.applyL2L3Residual = "Data" 
jetAna.jetPt = 15
jetAna.jetEta = 5.2 #FIXME
jetAna.addJECShifts = True
jetAna.doQG = False
jetAna.smearJets = False #should be false in susycore, already

jetAna.calculateSeparateCorrections = True #should be true if recalibrate, otherwise L1 inconsistent
jetAna.calculateType1METCorrection = True

isFastSim = False

#jetAna.dataGT = "Summer16_23Sep2016BCDV3_DATA Summer16_23Sep2016EFV3_DATA Summer16_23Sep2016GV3_DATA Summer16_23Sep2016HV3_DATA"
#jetAna.runsDataJEC = [276811, 278801, 280385]
jetAna.dataGT = [ ( -1, "Summer16_23Sep2016BCDV3_DATA"), (276811, "Summer16_23Sep2016EFV3_DATA"), (278801, "Summer16_23Sep2016GV3_DATA"), (280385, "Summer16_23Sep2016HV3_DATA") ]

#jetAna.dataGT   = "80X_dataRun2_2016SeptRepro_v3"
if isFastSim:
    jetAna.mcGT   = "Spring16_FastSimV1_MC"
else:
    jetAna.mcGT   = "Summer16_23Sep2016V3_MC"

# if isData: ## not going to work on MC
eventFlagsAna.triggerBits.update( {'badMuons':['Flag_badMuons'], 'duplicateMuons':['Flag_duplicateMuons'], 'noBadMuons':['Flag_noBadMuons'] })

#JECdb = '/afs/hephy.at/work/d/dspitzbart/stops/CMSSW_8_0_25/src/CMGTools/RootTools/data/jec/Summer16_25nsV5_MC.db'

isTTDM = False
if isTTDM:
    susyCoreSequence.remove( triggerFlagsAna )

metAna.recalibrate = "type1" 
#metAna.doTkMet = True # for chs met
from CMGTools.TTHAnalysis.analyzers.chsMETAnalyzer import chsMETAnalyzer
chsMETAna = cfg.Analyzer(
    chsMETAnalyzer,
    maxDz=0.1,
    packedCandidates = 'packedPFCandidates', 
    )
susyCoreSequence.append( chsMETAna )

## PHOTONS
doPhotonScaleCorrections = False

if doPhotonScaleCorrections:
    photonAna.doPhotonScaleCorrections = {
    'data' : 'EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_Golden22June_approval',
    'isSync': False
    }


isoTrackAna.setOff = False
genAna.allGenTaus  = True

from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## Insert the FatJet, SV, HeavyFlavour analyzers in the sequence
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHFatJetAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHSVAna)

#ISR jet counting
from CMGTools.TTHAnalysis.analyzers.nIsrAnalyzer import NIsrAnalyzer
nISRAna = cfg.Analyzer(
    NIsrAnalyzer, name="NIsrAnalyzer",
    minJets25 = 0,
    )
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        nISRAna)

# Tree Producer
from CMGTools.StopsDilepton.treeProducerStopsDilepton import *

if storePackedCandidates:
    from CMGTools.TTHAnalysis.analyzers.packedCandidateAnalyzer import packedCandidateAnalyzer
    packedCandidateAna = cfg.Analyzer(
        packedCandidateAnalyzer, name = 'packedCandidateAnalyzer',
        packedCandidates = 'packedPFCandidates',
    )
    susyCoreSequence.append( packedCandidateAna )

    susySingleLepton_collections.update( { "packedCandidates" : NTupleCollection("pf",     particleType, 15000, help="packed candidates (pf)")} )


from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer 
LHEAna = LHEAnalyzer.defaultConfig

#lheWeightAna.useLumiInfo=True # commented out to keep LHE weights in ttH signal (only works that way, no clue why)


from CMGTools.RootTools.samples.triggers_13TeV_DATA2016 import *
triggerFlagsAna.triggerBits = {
        # hadronic
        'HT350_MET100': triggers_HT350_MET100,
        "HT350":triggers_HT350,
        "HT475":triggers_HT475,
        "HT600":triggers_HT600,
        "dijet":triggers_dijet,
        "jet":triggers_jet,
        "dijet70met120": triggers_dijet70met120,
        "dijet55met110": triggers_dijet55met110,

        'HT900'                :triggers_HT900,
        'HT800'                :triggers_HT800,
        'MET170_NotCleaned'    :triggers_MET170_NotCleaned,
        'MET170_HBHECleaned'   :triggers_MET170_HBHECleaned,
        'MET170_BeamHaloCleaned':triggers_MET170_BeamHaloCleaned,
        'AllMET170'            :triggers_AllMET170,
        'AllMET300'            :triggers_AllMET300,
        'HT350_MET100'         :triggers_HT350_MET100,

        ## muon

        'SingleMu_iso'     :triggers_1mu_iso,
        'SingleMu_noniso'  :triggers_1mu_noniso ,

        'SingleEle_noniso'   :triggers_1e_noniso,
        'SingleEle'          :triggers_1e,

#mumu
        'mumuIso' : triggers_mumu_iso,
        'mumuNoiso' : triggers_mumu_noniso,
        'mumuSS' : triggers_mumu_ss,
        'mumuHT' : triggers_mumu_ht,
# ee
        'ee_DZ': triggers_ee,
        'ee_noDZ':triggers_ee_nodz ,
        'ee_noniso':triggers_ee_noniso,
        'ee_33': ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_v*'],
        'ee_33_MW': ['HLT_DoubleEle33_CaloIdL_GsfTrkIdVL_MW_v*'],
#mue
        'mue':triggers_mue,
        'mu30e30': ['HLT_Mu30_Ele30_CaloIdL_GsfTrkIdVL_v*'],
#dilepton+HT
        'ee_ht':triggers_ee_ht,
        'mue_ht':triggers_mue_ht,
#multi-lepton
        '3e':triggers_3e,
        '3mu':triggers_3mu,
        '3mu_alt':triggers_3mu_alt,
        '2mu1e':triggers_2mu1e,
        '2e1mu':triggers_2e1mu,
#fake rate
        'FR_1mu_iso':triggers_FR_1mu_iso,
        'FR_1mu_noiso':triggers_FR_1mu_noiso,
        'FR_1e_noiso':triggers_FR_1e_noiso,
        'FR_1e_iso':triggers_FR_1e_iso,
        'FR_1e_b2g':triggers_FR_1e_b2g,
#MET
        'Jet80MET90'       :triggers_Jet80MET90      ,
        'Jet80MET120'      :triggers_Jet80MET120     ,
        'MET120Mu5'        :triggers_MET120Mu5       ,

        }

# puppiMET
metPuppiAna = cfg.Analyzer(
    METAnalyzer, name="metPuppiAnalyzer",
    metCollection     = "slimmedMETsPuppi",
    noPUMetCollection = "slimmedMETsPuppi",
    copyMETsByValue = False,
    doTkMet = False,
    includeTkMetCHS = False,
    includeTkMetPVLoose = False,
    includeTkMetPVTight = False,
    doMetNoPU = False,
    doMetNoMu = False,
    doMetNoEle = False,
    doMetNoPhoton = False,
    recalibrate = False,
    applyJetSmearing = False, # does nothing unless the jet smearing is turned on in the jet analyzer
    old74XMiniAODs = False, # set to True to get the correct Raw MET when running on old 74X MiniAODs
    jetAnalyzerCalibrationPostFix = "",
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    dzMax = 0.1,
    collectionPostFix = "Puppi",
    )

## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusySingleLepton',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects = susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)

#!# #-------- SAMPLES AND SEQUENCE -----------

selectedComponents = [
        ]

sequence = cfg.Sequence(
  susyCoreSequence+
      [ 
        LHEAna,
        metPuppiAna,
        ttHEventAna,
        treeProducer,
        ])

#if True or getHeppyOption("loadSamples"):
if getHeppyOption("loadSamples"):
    #from CMGTools.RootTools.samples.samples_13TeV_RunIISpring16MiniAODv2 import *
    from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
    #from CMGTools.StopsDilepton.samplesReReco import *
    #from CMGTools.StopsDilepton.samples_13TeV_Moriond2017 import *
    from CMGTools.RootTools.samples.samples_13TeV_signals import *
    from CMGTools.StopsDilepton.TTbarDMJets_signals_RunIISummer16MiniAODv2 import *
    from CMGTools.StopsDilepton.Higgs_signals_RunIISummer16MiniAODv2 import *
    for sample in dataSamples:
        #sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-282092_13TeV_PromptReco_Collisions16_JSON.txt"
        sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
    from CMGTools.StopsDilepton.samples import *
    
    selectedComponents = [ttH_HToInvisible_M125]
    #selectedComponents = [TBar_tWch_ext]
    #selectedComponents = [TBar_tch_powheg]
    #selectedComponents = [TTbarDMJets_DiLept_scalar_NLO_Mchi_10_Mphi_100]
    #selectedComponents = [TTJets_LO]
    #selectedComponents = [TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_10]
    #selectedComponents = [SMS_T8bbllnunu_XCha0p5_XSlep0p5_mN1_700_1000]
    #selectedComponents = [SMS_T2bW]    
    #selectedComponents = [TTbarDMJets_scalar_Mchi_10_Mphi_100_ext1]
    #selectedComponents = [QCD_Pt_15to7000]
    #selectedComponents = [WJetsToLNu]
    #selectedComponents = [SMS_T2tt_mStop_150to250]
    #selectedComponents = [SMS_T8bbllnunu_XCha0p5_XSlep0p05]
    #selectedComponents = [SMS_T2tt_mStop_425_mLSP_325]
    #selectedComponents = [QCD_flat_80X_noPU]
    #selectedComponents = [DoubleMuon_Run2016E_03Feb2017]
    #selectedComponents = [DoubleEG_Run2016E_23Sep2016]
    #selectedComponents = [DoubleMuon_Run2016E_23Sep2016]
    #selectedComponents = [QCD_Pt_15to3000_M2_0_500, QCD_Pt_15to3000_M2_5_100]
    #selectedComponents = [ tWnunu ]
    #selectedComponents = [DoubleMuon_Run2016B_PromptReco_v2]
    for comp in selectedComponents:
            sample.json = None
            comp.files = comp.files[:1]
            #comp.files = ['root://eoscms.cern.ch//eos/cms/store/data/Run2016C/DoubleMuon/MINIAOD/23Sep2016-v1/80000/005599F4-5787-E611-A034-0025905C54C6.root']
            #comp.files = ['root://eoscms.cern.ch//store/group/phys_jetmet/MetScanners/bobak_pickevents_miniAOD.root']
            comp.splitFactor = 1

from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
event_class = Events
if getHeppyOption("fetch"):
  event_class = EOSEventsWithDownload

config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
#                     preprocessor=preprocessor, # comment if pre-processor non needed
                     events_class = event_class)

