import PhysicsTools.HeppyCore.framework.config as cfg
import os

from CMGTools.StopsDilepton.helper import makeMyPrivateMCComponentFromDPM

TTZToLLNuNuXsec = 0.2728

ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 0.8641 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 0.9281 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000',
                        dataset = '/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.6832 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll',
                        dataset = '/ewkDM_ttZ_ll/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_noH = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_noH',
                        dataset = '/ewkDM_ttZ_ll_noH/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_noH_DC2V_0p050000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_noH_DC2V_0p050000',
                        dataset = '/ewkDM_ttZ_ll_noH_DC2V_0p050000/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.02 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_noH_DC2V_0p100000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_noH_DC2V_0p100000',
                        dataset = '/ewkDM_ttZ_ll_noH_DC2V_0p100000/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.08 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_noH_DC2V_0p200000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_noH_DC2V_0p200000',
                        dataset = '/ewkDM_ttZ_ll_noH_DC2V_0p200000/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.32 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_noH_DC2V_0p300000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_noH_DC2V_0p300000',
                        dataset = '/ewkDM_ttZ_ll_noH_DC2V_0p300000/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.71 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_noH_DC2V_m0p150000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_noH_DC2V_m0p150000',
                        dataset = '/ewkDM_ttZ_ll_noH_DC2V_m0p150000/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.17 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_noH_DC2V_m0p250000 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_noH_DC2V_m0p250000',
                        dataset = '/ewkDM_ttZ_ll_noH_DC2V_m0p250000/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.48 * TTZToLLNuNuXsec,
                    )

# x-sec without nunu part
TTZToLLXsec = 1.24 * 0.8393 * 3 * 0.03366 # x-sec increased by 1.24 from gamma*, NLO x-sec from 1610.07922

ewkDM_TTZToLL_LO = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_TTZToLL_LO',
                        dataset = '/ewkDM_TTZToLL_LO_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1. * TTZToLLXsec,
                    )

ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2',
                        dataset = '/ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1.6832 * TTZToLLXsec,
                    )

ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_0p50 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_0p50',
                        dataset = '/ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_0p50_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1. * TTZToLLXsec,
                    )

ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_m1p00 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_m1p00',
                        dataset = '/ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_m1p00_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1. * TTZToLLXsec,
                    )

ewkDM_TTZToLL_LO_DC1A_0p60_DC1V_m0p24_DC2A0p25 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_TTZToLL_LO_DC1A_0p60_DC1V_m0p24_DC2A0p25',
                        dataset = '/ewkDM_TTZToLL_LO_DC1A_0p60_DC1V_m0p24_DC2A0p25_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1. * TTZToLLXsec,
                    )

ewkDM_TTZToLL_LO_DC1A_1p00_DC1V_0p00 = makeMyPrivateMCComponentFromDPM(
                        name    = 'ewkDM_TTZToLL_LO_DC1A_1p00_DC1V_0p00',
                        dataset = '/ewkDM_TTZToLL_LO_DC1A_1p00_DC1V_0p00_slc6_amd64_gcc481_CMSSW_7_1_30_tarball/dspitzba-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        xSec    = 1. * TTZToLLXsec,
                    )

signalSamples = [\
    ewkDM_ttZ_ll,
    ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700,
    ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000,
    ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000,
    ewkDM_ttZ_ll_noH,
    ewkDM_ttZ_ll_noH_DC2V_0p050000,
    ewkDM_ttZ_ll_noH_DC2V_0p100000,
    ewkDM_ttZ_ll_noH_DC2V_0p200000,
    ewkDM_ttZ_ll_noH_DC2V_0p300000,
    ewkDM_ttZ_ll_noH_DC2V_m0p150000,
    ewkDM_ttZ_ll_noH_DC2V_m0p250000,
    ewkDM_TTZToLL_LO,
    ewkDM_TTZToLL_LO_DC2A0p2_DC2V0p2,
    ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_0p50,
    ewkDM_TTZToLL_LO_DC1A_0p50_DC1V_m1p00,
    ewkDM_TTZToLL_LO_DC1A_0p60_DC1V_m0p24_DC2A0p25,
    ewkDM_TTZToLL_LO_DC1A_1p00_DC1V_0p00
]
