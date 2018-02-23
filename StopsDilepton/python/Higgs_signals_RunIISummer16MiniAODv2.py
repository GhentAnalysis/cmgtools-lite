import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- 25 ns ----------------------------------------
# TTbar cross section: NNLO, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (172.5)


## https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV

ttH_HToInvisible_M125   = kreator.makeMCComponent("ttH_HToInvisible_M125", "/ttH_HToInvisible_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.5071, useAAA=True )

ZH_ZToMM_HToInvisible_M110 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M110", "/ZH_ZToMM_HToInvisible_M110_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*1.309E+00 , useAAA=True )
ZH_ZToMM_HToInvisible_M125 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M125", "/ZH_ZToMM_HToInvisible_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*9.095E-01 , useAAA=True )
ZH_ZToMM_HToInvisible_M150 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M150", "/ZH_ZToMM_HToInvisible_M150_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*5.279E-01 , useAAA=True )
ZH_ZToMM_HToInvisible_M200 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M200", "/ZH_ZToMM_HToInvisible_M200_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*2.054E-01 , useAAA=True )
ZH_ZToMM_HToInvisible_M300 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M300", "/ZH_ZToMM_HToInvisible_M300_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*4.132E-02 , useAAA=True )
ZH_ZToMM_HToInvisible_M400 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M400", "/ZH_ZToMM_HToInvisible_M400_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*1.273E-02 , useAAA=True )
ZH_ZToMM_HToInvisible_M500 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M500", "/ZH_ZToMM_HToInvisible_M500_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*5.256E-03 , useAAA=True )
ZH_ZToMM_HToInvisible_M600 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M600", "/ZH_ZToMM_HToInvisible_M600_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*2.544E-03 , useAAA=True )
ZH_ZToMM_HToInvisible_M800 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M800", "/ZH_ZToMM_HToInvisible_M800_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",    0.3366*7.842E-04 , useAAA=True )
ZH_ZToMM_HToInvisible_M1000 = kreator.makeMCComponent("ZH_ZToMM_HToInvisible_M1000", "/ZH_ZToMM_HToInvisible_M1000_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM", "CMS", ".*root", 0.3366*2.977E-04 , useAAA=True )

ZH_ZToEE_HToInvisible_M110  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M110",  "/ZH_ZToEE_HToInvisible_M110_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*1.309E+00 , useAAA=True )
ZH_ZToEE_HToInvisible_M125  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M125",  "/ZH_ZToEE_HToInvisible_M125_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*9.095E-01 , useAAA=True )
ZH_ZToEE_HToInvisible_M150  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M150",  "/ZH_ZToEE_HToInvisible_M150_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*5.279E-01 , useAAA=True )
ZH_ZToEE_HToInvisible_M200  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M200",  "/ZH_ZToEE_HToInvisible_M200_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*2.054E-01 , useAAA=True )
ZH_ZToEE_HToInvisible_M300  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M300",  "/ZH_ZToEE_HToInvisible_M300_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*4.132E-02 , useAAA=True )
ZH_ZToEE_HToInvisible_M400  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M400",  "/ZH_ZToEE_HToInvisible_M400_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*1.273E-02 , useAAA=True )
ZH_ZToEE_HToInvisible_M500  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M500",  "/ZH_ZToEE_HToInvisible_M500_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*5.256E-03 , useAAA=True )
ZH_ZToEE_HToInvisible_M600  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M600",  "/ZH_ZToEE_HToInvisible_M600_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM",  "CMS", ".*root", 0.3363*2.544E-03 , useAAA=True )
ZH_ZToEE_HToInvisible_M800  = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M800",  "/ZH_ZToEE_HToInvisible_M800_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM",  "CMS", ".*root", 0.3363*7.842E-04 , useAAA=True )
ZH_ZToEE_HToInvisible_M1000 = kreator.makeMCComponent("ZH_ZToEE_HToInvisible_M1000", "/ZH_ZToEE_HToInvisible_M1000_13TeV_powheg_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2/MINIAODSIM", "CMS", ".*root", 0.3363*2.977E-04 , useAAA=True )




samples = [ZH_ZToMM_HToInvisible_M110,ZH_ZToMM_HToInvisible_M125,ZH_ZToMM_HToInvisible_M150,ZH_ZToMM_HToInvisible_M200,ZH_ZToMM_HToInvisible_M300,ZH_ZToMM_HToInvisible_M400,ZH_ZToMM_HToInvisible_M500,ZH_ZToMM_HToInvisible_M600,ZH_ZToMM_HToInvisible_M800,ZH_ZToMM_HToInvisible_M1000]

samples += [ZH_ZToEE_HToInvisible_M110,ZH_ZToEE_HToInvisible_M125,ZH_ZToEE_HToInvisible_M150,ZH_ZToEE_HToInvisible_M200,ZH_ZToEE_HToInvisible_M300,ZH_ZToEE_HToInvisible_M400,ZH_ZToEE_HToInvisible_M500,ZH_ZToEE_HToInvisible_M600,ZH_ZToEE_HToInvisible_M800,ZH_ZToEE_HToInvisible_M1000]

samples += [ttH_HToInvisible_M125]

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in samples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
