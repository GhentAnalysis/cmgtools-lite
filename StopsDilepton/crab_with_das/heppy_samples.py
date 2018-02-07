#-------- SAMPLES AND TRIGGERS -----------
#from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
from CMGTools.StopsDilepton.samples import *
#from CMGTools.RootTools.samples.samples_13TeV_RunIISpring16MiniAODv2 import *
from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
from CMGTools.RootTools.samples.samples_13TeV_signals import *
from CMGTools.StopsDilepton.TTbarDMJets_signals_RunIISummer16MiniAODv2 import *
from CMGTools.StopsDilepton.Higgs_signals_RunIISummer16MiniAODv2 import *
#from CMGTools.StopsDilepton.samples_13TeV_Moriond2017 import *

#from CMGTools.RootTools.samples.TTbarDMJets_signals_RunIISpring15MiniAODv2 import *
#from CMGTools.RootTools.samples.samples_13TeV_DATA2015 import *
#from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import *
#from CMGTools.RootTools.samples.triggers_13TeV_Spring15_1l import *
#from CMGTools.RootTools.samples.samples_13TeV_signals import *
##applying the correct json files to PrompReco and July17 samples

#for sample in dataSamples_Run2016B_v2 + dataSamples_Run2016C_v2 + dataSamples_Run2016D_v2:
#    sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt"

for sample in dataSamples:
    sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"
