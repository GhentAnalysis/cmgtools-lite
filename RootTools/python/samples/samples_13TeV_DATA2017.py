import PhysicsTools.HeppyCore.framework.config as cfg
import os

#/MET/Run2017B-12Sep2017-v1/MINIAOD Set complete?
#/MET/Run2017C-12Sep2017-v1/MINIAOD
#/MET/Run2017D-PromptReco-v1/MINIAOD
#/MET/Run2017E-PromptReco-v1/MINIAOD
#/MET/Run2017F-PromptReco-v1/MINIAOD

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

json='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294927-305364_13TeV_PromptReco_Collisions17_JSON.txt'

### ----------------------------- Run2017B 12Sep2017  ----------------------------------------

JetHT_Run2017B_12Sep2017          = kreator.makeDataComponent("JetHT_Run2017B_12Sep2017"         , "/JetHT/Run2017B-12Sep2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
HTMHT_Run2017B_12Sep2017          = kreator.makeDataComponent("HTMHT_Run2017B_12Sep2017"         , "/HTMHT/Run2017B-12Sep2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
MET_Run2017B_12Sep2017            = kreator.makeDataComponent("MET_Run2017B_12Sep2017"           , "/MET/Run2017B-12Sep2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
SingleElectron_Run2017B_12Sep2017 = kreator.makeDataComponent("SingleElectron_Run2017B_12Sep2017", "/SingleElectron/Run2017B-12Sep2017-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
SingleMuon_Run2017B_12Sep2017     = kreator.makeDataComponent("SingleMuon_Run2017B_12Sep2017"    , "/SingleMuon/Run2017B-12Sep2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
SinglePhoton_Run2017B_12Sep2017   = kreator.makeDataComponent("SinglePhoton_Run2017B_12Sep2017"  , "/SinglePhoton/Run2017B-12Sep2017-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
DoubleEG_Run2017B_12Sep2017       = kreator.makeDataComponent("DoubleEG_Run2017B_12Sep2017"      , "/DoubleEG/Run2017B-12Sep2017-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
MuonEG_Run2017B_12Sep2017         = kreator.makeDataComponent("MuonEG_Run2017B_12Sep2017"        , "/MuonEG/Run2017B-12Sep2017-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017B_12Sep2017     = kreator.makeDataComponent("DoubleMuon_Run2017B_12Sep2017"    , "/DoubleMuon/Run2017B-12Sep2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
Tau_Run2017B_12Sep2017            = kreator.makeDataComponent("Tau_Run2017B_12Sep2017"           , "/Tau/Run2017B-12Sep2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

dataSamples_Run2017B = [JetHT_Run2017B_12Sep2017, HTMHT_Run2017B_12Sep2017, MET_Run2017B_12Sep2017, SingleElectron_Run2017B_12Sep2017, SingleMuon_Run2017B_12Sep2017, SinglePhoton_Run2017B_12Sep2017, DoubleEG_Run2017B_12Sep2017, MuonEG_Run2017B_12Sep2017, DoubleMuon_Run2017B_12Sep2017, Tau_Run2017B_12Sep2017]

### ----------------------------- Run2017C 12Sep2017  ----------------------------------------

JetHT_Run2017C_12Sep2017          = kreator.makeDataComponent("JetHT_Run2017C_12Sep2017"         , "/JetHT/Run2017C-12Sep2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
HTMHT_Run2017C_12Sep2017          = kreator.makeDataComponent("HTMHT_Run2017C_12Sep2017"         , "/HTMHT/Run2017C-12Sep2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
MET_Run2017C_12Sep2017            = kreator.makeDataComponent("MET_Run2017C_12Sep2017"           , "/MET/Run2017C-12Sep2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
SingleElectron_Run2017C_12Sep2017 = kreator.makeDataComponent("SingleElectron_Run2017C_12Sep2017", "/SingleElectron/Run2017C-12Sep2017-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
SingleMuon_Run2017C_12Sep2017     = kreator.makeDataComponent("SingleMuon_Run2017C_12Sep2017"    , "/SingleMuon/Run2017C-12Sep2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
SinglePhoton_Run2017C_12Sep2017   = kreator.makeDataComponent("SinglePhoton_Run2017C_12Sep2017"  , "/SinglePhoton/Run2017C-12Sep2017-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
DoubleEG_Run2017C_12Sep2017       = kreator.makeDataComponent("DoubleEG_Run2017C_12Sep2017"      , "/DoubleEG/Run2017C-12Sep2017-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
MuonEG_Run2017C_12Sep2017         = kreator.makeDataComponent("MuonEG_Run2017C_12Sep2017"        , "/MuonEG/Run2017C-12Sep2017-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017C_12Sep2017     = kreator.makeDataComponent("DoubleMuon_Run2017C_12Sep2017"    , "/DoubleMuon/Run2017C-12Sep2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
Tau_Run2017C_12Sep2017            = kreator.makeDataComponent("Tau_Run2017C_12Sep2017"           , "/Tau/Run2017C-12Sep2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

dataSamples_Run2017C = [JetHT_Run2017C_12Sep2017, HTMHT_Run2017C_12Sep2017, MET_Run2017C_12Sep2017, SingleElectron_Run2017C_12Sep2017, SingleMuon_Run2017C_12Sep2017, SinglePhoton_Run2017C_12Sep2017, DoubleEG_Run2017C_12Sep2017, MuonEG_Run2017C_12Sep2017, DoubleMuon_Run2017C_12Sep2017, Tau_Run2017C_12Sep2017]
### ----------------------------- Run2017C 12Sep2017  ----------------------------------------

JetHT_Run2017Cv2          = kreator.makeDataComponent("JetHT_Run2017Cv2"         , "/JetHT/Run2017C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
HTMHT_Run2017Cv2          = kreator.makeDataComponent("HTMHT_Run2017Cv2"         , "/HTMHT/Run2017C-PromptReco-v2/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
MET_Run2017Cv2            = kreator.makeDataComponent("MET_Run2017Cv2"           , "/MET/Run2017C-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
SingleElectron_Run2017Cv2 = kreator.makeDataComponent("SingleElectron_Run2017Cv2", "/SingleElectron/Run2017C-PromptReco-v2/MINIAOD", "CMS", ".*root", json, useAAA=True )
SingleMuon_Run2017Cv2     = kreator.makeDataComponent("SingleMuon_Run2017Cv2"    , "/SingleMuon/Run2017C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
SinglePhoton_Run2017Cv2   = kreator.makeDataComponent("SinglePhoton_Run2017Cv2"  , "/SinglePhoton/Run2017C-PromptReco-v2/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
DoubleEG_Run2017Cv2       = kreator.makeDataComponent("DoubleEG_Run2017Cv2"      , "/DoubleEG/Run2017C-PromptReco-v2/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
MuonEG_Run2017Cv2         = kreator.makeDataComponent("MuonEG_Run2017Cv2"        , "/MuonEG/Run2017C-PromptReco-v2/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017Cv2     = kreator.makeDataComponent("DoubleMuon_Run2017Cv2"    , "/DoubleMuon/Run2017C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
Tau_Run2017Cv2            = kreator.makeDataComponent("Tau_Run2017Cv2"           , "/Tau/Run2017C-PromptReco-v2/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

dataSamples_Run2017Cv2 = [JetHT_Run2017Cv2, HTMHT_Run2017Cv2, MET_Run2017Cv2, SingleElectron_Run2017Cv2, SingleMuon_Run2017Cv2, SinglePhoton_Run2017Cv2, DoubleEG_Run2017Cv2, MuonEG_Run2017Cv2, DoubleMuon_Run2017Cv2, Tau_Run2017Cv2]

### ----------------------------- Run2017D PromptReco  ----------------------------------------

JetHT_Run2017D          = kreator.makeDataComponent("JetHT_Run2017D"         , "/JetHT/Run2017D-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
HTMHT_Run2017D          = kreator.makeDataComponent("HTMHT_Run2017D"         , "/HTMHT/Run2017D-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
MET_Run2017D            = kreator.makeDataComponent("MET_Run2017D"           , "/MET/Run2017D-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
SingleElectron_Run2017D = kreator.makeDataComponent("SingleElectron_Run2017D", "/SingleElectron/Run2017D-PromptReco-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
SingleMuon_Run2017D     = kreator.makeDataComponent("SingleMuon_Run2017D"    , "/SingleMuon/Run2017D-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
SinglePhoton_Run2017D   = kreator.makeDataComponent("SinglePhoton_Run2017D"  , "/SinglePhoton/Run2017D-PromptReco-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
DoubleEG_Run2017D       = kreator.makeDataComponent("DoubleEG_Run2017D"      , "/DoubleEG/Run2017D-PromptReco-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
MuonEG_Run2017D         = kreator.makeDataComponent("MuonEG_Run2017D"        , "/MuonEG/Run2017D-PromptReco-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017D     = kreator.makeDataComponent("DoubleMuon_Run2017D"    , "/DoubleMuon/Run2017D-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
Tau_Run2017D            = kreator.makeDataComponent("Tau_Run2017D"           , "/Tau/Run2017D-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

dataSamples_Run2017D = [JetHT_Run2017D, HTMHT_Run2017D, MET_Run2017D, SingleElectron_Run2017D, SingleMuon_Run2017D, SinglePhoton_Run2017D, DoubleEG_Run2017D, MuonEG_Run2017D, DoubleMuon_Run2017D, Tau_Run2017D]

### ----------------------------- Run2017E PromptReco  ----------------------------------------

JetHT_Run2017E          = kreator.makeDataComponent("JetHT_Run2017E"         , "/JetHT/Run2017E-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
HTMHT_Run2017E          = kreator.makeDataComponent("HTMHT_Run2017E"         , "/HTMHT/Run2017E-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
MET_Run2017E            = kreator.makeDataComponent("MET_Run2017E"           , "/MET/Run2017E-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
SingleElectron_Run2017E = kreator.makeDataComponent("SingleElectron_Run2017E", "/SingleElectron/Run2017E-PromptReco-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
SingleMuon_Run2017E     = kreator.makeDataComponent("SingleMuon_Run2017E"    , "/SingleMuon/Run2017E-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
SinglePhoton_Run2017E   = kreator.makeDataComponent("SinglePhoton_Run2017E"  , "/SinglePhoton/Run2017E-PromptReco-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
DoubleEG_Run2017E       = kreator.makeDataComponent("DoubleEG_Run2017E"      , "/DoubleEG/Run2017E-PromptReco-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
MuonEG_Run2017E         = kreator.makeDataComponent("MuonEG_Run2017E"        , "/MuonEG/Run2017E-PromptReco-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017E     = kreator.makeDataComponent("DoubleMuon_Run2017E"    , "/DoubleMuon/Run2017E-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
Tau_Run2017E            = kreator.makeDataComponent("Tau_Run2017E"           , "/Tau/Run2017E-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

dataSamples_Run2017E = [JetHT_Run2017E, HTMHT_Run2017E, MET_Run2017E, SingleElectron_Run2017E, SingleMuon_Run2017E, SinglePhoton_Run2017E, DoubleEG_Run2017E, MuonEG_Run2017E, DoubleMuon_Run2017E, Tau_Run2017E]

### ----------------------------- Run2017F PromptReco  ----------------------------------------

JetHT_Run2017F          = kreator.makeDataComponent("JetHT_Run2017F"         , "/JetHT/Run2017F-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
HTMHT_Run2017F          = kreator.makeDataComponent("HTMHT_Run2017F"         , "/HTMHT/Run2017F-PromptReco-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
MET_Run2017F            = kreator.makeDataComponent("MET_Run2017F"           , "/MET/Run2017F-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
SingleElectron_Run2017F = kreator.makeDataComponent("SingleElectron_Run2017F", "/SingleElectron/Run2017F-PromptReco-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
SingleMuon_Run2017F     = kreator.makeDataComponent("SingleMuon_Run2017F"    , "/SingleMuon/Run2017F-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
SinglePhoton_Run2017F   = kreator.makeDataComponent("SinglePhoton_Run2017F"  , "/SinglePhoton/Run2017F-PromptReco-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
DoubleEG_Run2017F       = kreator.makeDataComponent("DoubleEG_Run2017F"      , "/DoubleEG/Run2017F-PromptReco-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
MuonEG_Run2017F         = kreator.makeDataComponent("MuonEG_Run2017F"        , "/MuonEG/Run2017F-PromptReco-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017F     = kreator.makeDataComponent("DoubleMuon_Run2017F"    , "/DoubleMuon/Run2017F-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
Tau_Run2017F            = kreator.makeDataComponent("Tau_Run2017F"           , "/Tau/Run2017F-PromptReco-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

dataSamples_Run2017F = [JetHT_Run2017F, HTMHT_Run2017F, MET_Run2017F, SingleElectron_Run2017F, SingleMuon_Run2017F, SinglePhoton_Run2017F, DoubleEG_Run2017F, MuonEG_Run2017F, DoubleMuon_Run2017F, Tau_Run2017F]

dataSamples = dataSamples_Run2017B + dataSamples_Run2017C + dataSamples_Run2017Cv2 + dataSamples_Run2017D + dataSamples_Run2017E + dataSamples_Run2017F

### ----------------------------- Run2017B 17Nov2017  ----------------------------------------

#JetHT_Run2017B_17Nov2017          = kreator.makeDataComponent("JetHT_Run2017B_17Nov2017"         , "/JetHT/Run2017B-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#HTMHT_Run2017B_17Nov2017          = kreator.makeDataComponent("HTMHT_Run2017B_17Nov2017"         , "/HTMHT/Run2017B-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#MET_Run2017B_17Nov2017            = kreator.makeDataComponent("MET_Run2017B_17Nov2017"           , "/MET/Run2017B-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
#SingleElectron_Run2017B_17Nov2017 = kreator.makeDataComponent("SingleElectron_Run2017B_17Nov2017", "/SingleElectron/Run2017B-17Nov2017-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
#SingleMuon_Run2017B_17Nov2017     = kreator.makeDataComponent("SingleMuon_Run2017B_17Nov2017"    , "/SingleMuon/Run2017B-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#SinglePhoton_Run2017B_17Nov2017   = kreator.makeDataComponent("SinglePhoton_Run2017B_17Nov2017"  , "/SinglePhoton/Run2017B-17Nov2017-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
#DoubleEG_Run2017B_17Nov2017       = kreator.makeDataComponent("DoubleEG_Run2017B_17Nov2017"      , "/DoubleEG/Run2017B-17Nov2017-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
#MuonEG_Run2017B_17Nov2017         = kreator.makeDataComponent("MuonEG_Run2017B_17Nov2017"        , "/MuonEG/Run2017B-17Nov2017-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017B_17Nov2017     = kreator.makeDataComponent("DoubleMuon_Run2017B_17Nov2017"    , "/DoubleMuon/Run2017B-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#Tau_Run2017B_17Nov2017            = kreator.makeDataComponent("Tau_Run2017B_17Nov2017"           , "/Tau/Run2017B-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

#dataSamples_Run2017B_17Nov2017 = [JetHT_Run2017B_17Nov2017, HTMHT_Run2017B_17Nov2017, MET_Run2017B_17Nov2017, SingleElectron_Run2017B_17Nov2017, SingleMuon_Run2017B_17Nov2017, SinglePhoton_Run2017B_17Nov2017, DoubleEG_Run2017B_17Nov2017, MuonEG_Run2017B_17Nov2017, DoubleMuon_Run2017B_17Nov2017, Tau_Run2017B_17Nov2017]
dataSamples_Run2017B_17Nov2017 = [ DoubleMuon_Run2017B_17Nov2017 ]

### ----------------------------- Run2017C 17Nov2017  ----------------------------------------

#JetHT_Run2017C_17Nov2017          = kreator.makeDataComponent("JetHT_Run2017C_17Nov2017"         , "/JetHT/Run2017C-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#HTMHT_Run2017C_17Nov2017          = kreator.makeDataComponent("HTMHT_Run2017C_17Nov2017"         , "/HTMHT/Run2017C-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#MET_Run2017C_17Nov2017            = kreator.makeDataComponent("MET_Run2017C_17Nov2017"           , "/MET/Run2017C-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
#SingleElectron_Run2017C_17Nov2017 = kreator.makeDataComponent("SingleElectron_Run2017C_17Nov2017", "/SingleElectron/Run2017C-17Nov2017-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
#SingleMuon_Run2017C_17Nov2017     = kreator.makeDataComponent("SingleMuon_Run2017C_17Nov2017"    , "/SingleMuon/Run2017C-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#SinglePhoton_Run2017C_17Nov2017   = kreator.makeDataComponent("SinglePhoton_Run2017C_17Nov2017"  , "/SinglePhoton/Run2017C-17Nov2017-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
#DoubleEG_Run2017C_17Nov2017       = kreator.makeDataComponent("DoubleEG_Run2017C_17Nov2017"      , "/DoubleEG/Run2017C-17Nov2017-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
#MuonEG_Run2017C_17Nov2017         = kreator.makeDataComponent("MuonEG_Run2017C_17Nov2017"        , "/MuonEG/Run2017C-17Nov2017-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017C_17Nov2017     = kreator.makeDataComponent("DoubleMuon_Run2017C_17Nov2017"    , "/DoubleMuon/Run2017C-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#Tau_Run2017C_17Nov2017            = kreator.makeDataComponent("Tau_Run2017C_17Nov2017"           , "/Tau/Run2017C-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

#dataSamples_Run2017C_17Nov2017 = [JetHT_Run2017C_17Nov2017, HTMHT_Run2017C_17Nov2017, MET_Run2017C_17Nov2017, SingleElectron_Run2017C_17Nov2017, SingleMuon_Run2017C_17Nov2017, SinglePhoton_Run2017C_17Nov2017, DoubleEG_Run2017C_17Nov2017, MuonEG_Run2017C_17Nov2017, DoubleMuon_Run2017C_17Nov2017, Tau_Run2017C_17Nov2017]
dataSamples_Run2017C_17Nov2017 = [ DoubleMuon_Run2017C_17Nov2017 ]

### ----------------------------- Run2017D 17Nov2017  ----------------------------------------

#JetHT_Run2017D_17Nov2017          = kreator.makeDataComponent("JetHT_Run2017D_17Nov2017"         , "/JetHT/Run2017D-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#HTMHT_Run2017D_17Nov2017          = kreator.makeDataComponent("HTMHT_Run2017D_17Nov2017"         , "/HTMHT/Run2017D-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#MET_Run2017D_17Nov2017            = kreator.makeDataComponent("MET_Run2017D_17Nov2017"           , "/MET/Run2017D-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
#SingleElectron_Run2017D_17Nov2017 = kreator.makeDataComponent("SingleElectron_Run2017D_17Nov2017", "/SingleElectron/Run2017D-17Nov2017-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
#SingleMuon_Run2017D_17Nov2017     = kreator.makeDataComponent("SingleMuon_Run2017D_17Nov2017"    , "/SingleMuon/Run2017D-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#SinglePhoton_Run2017D_17Nov2017   = kreator.makeDataComponent("SinglePhoton_Run2017D_17Nov2017"  , "/SinglePhoton/Run2017D-17Nov2017-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
#DoubleEG_Run2017D_17Nov2017       = kreator.makeDataComponent("DoubleEG_Run2017D_17Nov2017"      , "/DoubleEG/Run2017D-17Nov2017-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
#MuonEG_Run2017D_17Nov2017         = kreator.makeDataComponent("MuonEG_Run2017D_17Nov2017"        , "/MuonEG/Run2017D-17Nov2017-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017D_17Nov2017     = kreator.makeDataComponent("DoubleMuon_Run2017D_17Nov2017"    , "/DoubleMuon/Run2017D-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#Tau_Run2017D_17Nov2017            = kreator.makeDataComponent("Tau_Run2017D_17Nov2017"           , "/Tau/Run2017D-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

#dataSamples_Run2017D_17Nov2017 = [JetHT_Run2017D_17Nov2017, HTMHT_Run2017D_17Nov2017, MET_Run2017D_17Nov2017, SingleElectron_Run2017D_17Nov2017, SingleMuon_Run2017D_17Nov2017, SinglePhoton_Run2017D_17Nov2017, DoubleEG_Run2017D_17Nov2017, MuonEG_Run2017D_17Nov2017, DoubleMuon_Run2017D_17Nov2017, Tau_Run2017D_17Nov2017]
dataSamples_Run2017D_17Nov2017 = [ DoubleMuon_Run2017D_17Nov2017 ]

### ----------------------------- Run2017E 17Nov2017  ----------------------------------------

#JetHT_Run2017E_17Nov2017          = kreator.makeDataComponent("JetHT_Run2017E_17Nov2017"         , "/JetHT/Run2017E-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#HTMHT_Run2017E_17Nov2017          = kreator.makeDataComponent("HTMHT_Run2017E_17Nov2017"         , "/HTMHT/Run2017E-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#MET_Run2017E_17Nov2017            = kreator.makeDataComponent("MET_Run2017E_17Nov2017"           , "/MET/Run2017E-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
#SingleElectron_Run2017E_17Nov2017 = kreator.makeDataComponent("SingleElectron_Run2017E_17Nov2017", "/SingleElectron/Run2017E-17Nov2017-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
#SingleMuon_Run2017E_17Nov2017     = kreator.makeDataComponent("SingleMuon_Run2017E_17Nov2017"    , "/SingleMuon/Run2017E-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#SinglePhoton_Run2017E_17Nov2017   = kreator.makeDataComponent("SinglePhoton_Run2017E_17Nov2017"  , "/SinglePhoton/Run2017E-17Nov2017-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
#DoubleEG_Run2017E_17Nov2017       = kreator.makeDataComponent("DoubleEG_Run2017E_17Nov2017"      , "/DoubleEG/Run2017E-17Nov2017-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
#MuonEG_Run2017E_17Nov2017         = kreator.makeDataComponent("MuonEG_Run2017E_17Nov2017"        , "/MuonEG/Run2017E-17Nov2017-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017E_17Nov2017     = kreator.makeDataComponent("DoubleMuon_Run2017E_17Nov2017"    , "/DoubleMuon/Run2017E-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#Tau_Run2017E_17Nov2017            = kreator.makeDataComponent("Tau_Run2017E_17Nov2017"           , "/Tau/Run2017E-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

#dataSamples_Run2017E_17Nov2017 = [JetHT_Run2017E_17Nov2017, HTMHT_Run2017E_17Nov2017, MET_Run2017E_17Nov2017, SingleElectron_Run2017E_17Nov2017, SingleMuon_Run2017E_17Nov2017, SinglePhoton_Run2017E_17Nov2017, DoubleEG_Run2017E_17Nov2017, MuonEG_Run2017E_17Nov2017, DoubleMuon_Run2017E_17Nov2017, Tau_Run2017E_17Nov2017]
dataSamples_Run2017E_17Nov2017 = [ DoubleMuon_Run2017E_17Nov2017 ]

### ----------------------------- Run2017F 17Nov2017  ----------------------------------------

#JetHT_Run2017F_17Nov2017          = kreator.makeDataComponent("JetHT_Run2017F_17Nov2017"         , "/JetHT/Run2017F-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#HTMHT_Run2017F_17Nov2017          = kreator.makeDataComponent("HTMHT_Run2017F_17Nov2017"         , "/HTMHT/Run2017F-17Nov2017-v1/MINIAOD"         , "CMS", ".*root", json, useAAA=True )
#MET_Run2017F_17Nov2017            = kreator.makeDataComponent("MET_Run2017F_17Nov2017"           , "/MET/Run2017F-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )
#SingleElectron_Run2017F_17Nov2017 = kreator.makeDataComponent("SingleElectron_Run2017F_17Nov2017", "/SingleElectron/Run2017F-17Nov2017-v1/MINIAOD", "CMS", ".*root", json, useAAA=True )
#SingleMuon_Run2017F_17Nov2017     = kreator.makeDataComponent("SingleMuon_Run2017F_17Nov2017"    , "/SingleMuon/Run2017F-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#SinglePhoton_Run2017F_17Nov2017   = kreator.makeDataComponent("SinglePhoton_Run2017F_17Nov2017"  , "/SinglePhoton/Run2017F-17Nov2017-v1/MINIAOD"  , "CMS", ".*root", json, useAAA=True )
#DoubleEG_Run2017F_17Nov2017       = kreator.makeDataComponent("DoubleEG_Run2017F_17Nov2017"      , "/DoubleEG/Run2017F-17Nov2017-v1/MINIAOD"      , "CMS", ".*root", json, useAAA=True )
#MuonEG_Run2017F_17Nov2017         = kreator.makeDataComponent("MuonEG_Run2017F_17Nov2017"        , "/MuonEG/Run2017F-17Nov2017-v1/MINIAOD"        , "CMS", ".*root", json, useAAA=True )
DoubleMuon_Run2017F_17Nov2017     = kreator.makeDataComponent("DoubleMuon_Run2017F_17Nov2017"    , "/DoubleMuon/Run2017F-17Nov2017-v1/MINIAOD"    , "CMS", ".*root", json, useAAA=True )
#Tau_Run2017F_17Nov2017            = kreator.makeDataComponent("Tau_Run2017F_17Nov2017"           , "/Tau/Run2017F-17Nov2017-v1/MINIAOD"           , "CMS", ".*root", json, useAAA=True )

#dataSamples_Run2017F_17Nov2017 = [JetHT_Run2017F_17Nov2017, HTMHT_Run2017F_17Nov2017, MET_Run2017F_17Nov2017, SingleElectron_Run2017F_17Nov2017, SingleMuon_Run2017F_17Nov2017, SinglePhoton_Run2017F_17Nov2017, DoubleEG_Run2017F_17Nov2017, MuonEG_Run2017F_17Nov2017, DoubleMuon_Run2017F_17Nov2017, Tau_Run2017F_17Nov2017]
dataSamples_Run2017F_17Nov2017 = [ DoubleMuon_Run2017F_17Nov2017 ]

dataSamples += dataSamples_Run2017B_17Nov2017 + dataSamples_Run2017C_17Nov2017 + dataSamples_Run2017D_17Nov2017 + dataSamples_Run2017E_17Nov2017 + dataSamples_Run2017F_17Nov2017

samples = dataSamples
### ---------------------------------------------------------------------

for comp in samples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples, useAAA=True )
