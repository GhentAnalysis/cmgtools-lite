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

lepAna.rhoMuon = 'fixedGridRhoFastjetAll'
lepAna.rhoElectron = 'fixedGridRhoFastjetAll'

## ELECTRONS
lepAna.loose_electron_pt  = 5
doElectronScaleCorrections = False
lepAna.doMiniIsolation = True

lepAna.loose_electron_id  = ""
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.

keepLHEWeights =  getHeppyOption("keepLHEweights",True)

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
  lepAna.mu_isoCorr = "rhoArea" # this is new!

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
metAna.storePuppiExtra = False # False for MC, True for re-MiniAOD??
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
        'SingleMuTTZ'      :triggers_1mu_iso_TTZ,

        'SingleEle_noniso'   :triggers_1e_noniso,
        'SingleEle'          :triggers_1e,
        'SingleEleTTZ'       :triggers_1e_iso_TTZ,

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
        'eeSS' : triggers_ee_ss,
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

        'DoubleMu3_PFMET50' : ['HLT_DoubleMu3_PFMET50_v*'],
        'Mu6_PFHT200_PFMET100' : ['HLT_Mu6_PFHT200_PFMET100_v*'],
        'PFMET110_PFMHT110_IDTight': ['HLT_PFMET110_PFMHT110_IDTight_v*'], #prescaled
        'PFMET120_PFMHT120_IDTight': ['HLT_PFMET120_PFMHT120_IDTight_v*'],

        "MET_had": [ "HLT_MET200_v*", "HLT_MET250_v*", "HLT_MET300_v*", "HLT_PFMET100_PFMHT100_IDTight_v*", "HLT_PFMET110_PFMHT110_IDTight_v*", "HLT_PFMET120_BTagCSV0p72_v*", "HLT_PFMET120_PFMHT120_IDTight_v*", "HLT_PFMET170_HBHECleaned_v*", "HLT_PFMET170_JetIdCleaned_v*", "HLT_PFMET170_NoiseCleaned_v*", "HLT_PFMET170_v*", "HLT_PFMET300_v*", "HLT_PFMET400_v*", "HLT_PFMET90_PFMHT90_IDTight_v*", "HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_v*", "HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72_v*", "HLT_QuadPFJet_VBF_v*"],
        "MET_IsoTrk":[ "HLT_MET60_IsoTrk35_Loose_v*", "HLT_MET75_IsoTrk50_v*", "HLT_MET90_IsoTrk50_v*"], 
        "MET_PFMETNoMu": ["HLT_MonoCentralPFJet80_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*", "HLT_MonoCentralPFJet80_PFMETNoMu120_PFMHTNoMu120_IDTight_v*", "HLT_MonoCentralPFJet80_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*", "HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
        "MET_PFMETNoMu_JetIdCleaned":[ "HLT_PFMETNoMu120_JetIdCleaned_PFMHTNoMu120_IDTight_v*", "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v*", "HLT_PFMETNoMu90_JetIdCleaned_PFMHTNoMu90_IDTight_v*", "HLT_PFMETNoMu90_PFMHTNoMu90_IDTight_v*"],
        "MET_MuXer": ["HLT_Mu14er_PFMET100_v*", "HLT_Mu3er_PFHT140_PFMET125_v*", "HLT_Mu6_PFHT200_PFMET100_v*", "HLT_Mu6_PFHT200_PFMET80_BTagCSV0p72_v*", "HLT_PFMET120_Mu5_v*"],

        "HTMHT_had": [ "HLT_DiCentralPFJet55_PFMET110_v*", "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v*", "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v*", "HLT_PFHT200_PFAlphaT0p51_v*", "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v*", "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v*", "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v*", "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v*", "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v*", "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v*", "HLT_PFHT350_PFMET100_v*", "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v*", "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v*", "HLT_Rsq0p25_v*", "HLT_Rsq0p30_v*", "HLT_RsqMR240_Rsq0p09_MR200_4jet_v*", "HLT_RsqMR240_Rsq0p09_MR200_v*", "HLT_RsqMR270_Rsq0p09_MR200_4jet_v*", "HLT_RsqMR270_Rsq0p09_MR200_v*"],
        "HTMHT_PFMETNoMu":[ "HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu140_v*", "HLT_DiPFJet40_DEta3p5_MJJ600_PFMETNoMu80_v*"],

# individual triggers
        'Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ': ['HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*'],
        'Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ': ['HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*'],
        'IsoMu22': ['HLT_IsoMu22_v*'],
        'IsoTkMu22': ['HLT_IsoTkMu22_v*'],
        'IsoMu22_eta2p1': ['HLT_IsoMu22_eta2p1_v*'],
        'IsoTkMu22_eta2p1': ['HLT_IsoTkMu22_eta2p1_v*'],
        'IsoMu24': ['HLT_IsoMu24_v*'],
        'IsoTkMu24': ['HLT_IsoTkMu24_v*'],
        'Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
        'Ele27_WPTight_Gsf': ['HLT_Ele27_WPTight_Gsf_v*'],
        'Ele25_eta2p1_WPTight_Gsf': ['HLT_Ele25_eta2p1_WPTight_Gsf_v*'],
        'Ele27_eta2p1_WPLoose_Gsf': ['HLT_Ele27_eta2p1_WPLoose_Gsf_v*'],
        'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL': ['HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_v*'],
        'Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
        'Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL': ['HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*'],
        'Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ': ['HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*'],
        'DiMu9_Ele9_CaloIdL_TrackIdL': ['HLT_DiMu9_Ele9_CaloIdL_TrackIdL_v*'],
        'Mu8_DiEle12_CaloIdL_TrackIdL': ['HLT_Mu8_DiEle12_CaloIdL_TrackIdL_v*'],
        'TripleMu_12_10_5': ['HLT_TripleMu_12_10_5_v*'],
        'Ele16_Ele12_Ele8_CaloIdL_TrackIdL': ['HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v*'],
}

trigMatcher1Mu = cfg.Analyzer(
    TriggerMatchAnalyzer, name="trigMatcher1Mu",
    label='1Mu',
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    unpackPathNames = True,
    #trgObjSelectors = [ lambda t : t.path("HLT_IsoMu22_v*",1,0) or t.path("HLT_IsoMu20_v*",1,0) ],
    trgObjSelectors = [ lambda t : t.path("HLT_IsoMu22_v*",1,0) or t.path("HLT_IsoTkMu22_v*",1,0) or t.path("HLT_IsoMu22_eta2p1_v*",1,0) or t.path("HLT_IsoTkMu22_eta2p1_v*",1,0) or t.path("HLT_IsoTkMu24_v*",1,0)  ],#"HLT_IsoMu22", "HLT_IsoTkMu22", "HLT_IsoMu22_eta2p1", "HLT_IsoTkMu22_eta2p1", "HLT_IsoMu24", "HLT_IsoTkMu24"
    collToMatch = 'selectedLeptons',
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 13 ],
    collMatchDRCut = 0.3,
    univoqueMatching = True,
    verbose = False,
)
trigMatcher1El = trigMatcher1Mu.clone(
    name="trigMatcher1El",
    label='1El',
    #trgObjSelectors = [ lambda t : t.path("HLT_Ele27_eta2p1_WP75_Gsf_v*",1,0) or t.path("HLT_Ele27_eta2p1_WPLoose_Gsf_v*",1,0) ],
    #"HLT_Ele27_WPTight_Gsf", "HLT_Ele25_eta2p1_WPTight_Gsf", "HLT_Ele27_eta2p1_WPLoose_Gsf"
    trgObjSelectors = [ lambda t : t.path("HLT_Ele27_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele25_eta2p1_WPTight_Gsf_v*",1,0) or t.path("HLT_Ele27_eta2p1_WPLoose_Gsf_v*",1,0) ],
    collMatchSelectors = [ lambda l,t : abs(l.pdgId()) == 11 ],
)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1Mu)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        trigMatcher1El)

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
    storePuppiExtra = False,
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
    from CMGTools.StopsDilepton.ttX0j_5f_MLM_signals_RunIISummer16MiniAODv2 import *
    from CMGTools.StopsDilepton.ewkDM_signals_RunIISummer16MiniAODv2 import *
    from CMGTools.StopsDilepton.samples import *
    from CMGTools.StopsDilepton.Higgs_signals_RunIISummer16MiniAODv2 import *
    for sample in dataSamples + samples_data_private:
        #sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-282092_13TeV_PromptReco_Collisions16_JSON.txt"
        sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
    
    #selectedComponents = [ttH_HToInvisible_M125]
    #selectedComponents = [TBar_tWch_ext]
    #selectedComponents = [TBar_tch_powheg]
    #selectedComponents = [TTbarDMJets_DiLept_scalar_NLO_Mchi_10_Mphi_100]
    #selectedComponents = [TTJets_LO]
    #selectedComponents = [DYJetsToLL_M50_LO_ext]
    #selectedComponents = [SingleElectron_Run2016H_03Feb2017_v3]
    #selectedComponents = [ttZ0j_ll]
    #selectedComponents = [WpWpJJ]
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
    selectedComponents = [MET_Run2016B_03Feb2017_v2]
    #selectedComponents = [DoubleEG_Run2016E_23Sep2016]
    #selectedComponents = [DoubleMuon_Run2016E_23Sep2016]
    #selectedComponents = [QCD_Pt_15to3000_M2_0_500, QCD_Pt_15to3000_M2_5_100]
    #selectedComponents = [ tWnunu ]
    #selectedComponents = [JetHT_Run2016H_22Feb2017]
    #from files import doubleMu_files
    #DoubleMuon_Run2016B_23Sep2016.files = ['root://cms-xrd-global.cern.ch/%s'%s for s in doubleMu_files]
    #print DoubleMuon_Run2016B_23Sep2016.files
    #DoubleMuon_Run2016B_23Sep2016.json="$CMSSW_BASE/src/CMGTools/StopsDilepton/cfg/json.json"
    #selectedComponents = [DoubleMuon_Run2016B_23Sep2016]
    for comp in selectedComponents:
            comp.files = comp.files[:1]
            #comp.files = []
            #for i in range(41):
            #    if i == 39: continue #missing file
            #    fn = 'event_%s.root'%i
            #    comp.files.append(fn)
            comp.files = ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/3E1DE3B8-87C0-E611-8733-00145EDD74ED.root']
            #comp.files = ['root://eoscms.cern.ch//store/group/phys_jetmet/MetScanners/bobak_pickevents_miniAOD.root']
            comp.splitFactor = 1

from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
event_class = Events
if getHeppyOption("fetch"):
  event_class = EOSEventsWithDownload

preprocessorFile = "$CMSSW_BASE/python/CMGTools/StopsDilepton/preprocessor/runBTaggingSlimPreprocessor_cfg.py"
from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
preprocessor = CmsswPreprocessor(preprocessorFile)
jetAna.jetCol = 'selectedUpdatedPatJets'

config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     preprocessor=preprocessor, # comment if pre-processor non needed
                     events_class = event_class)

