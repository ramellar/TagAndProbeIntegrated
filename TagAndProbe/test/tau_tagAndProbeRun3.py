import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
from Configuration.AlCa.autoCond import autoCond

isMC=False
doReEmulation=False
CALOPARAMS = "L1Trigger.L1TCalorimeter.caloParams_2025_v0_3_cfi"
# CALOPARAMS = "L1Trigger.L1TCalorimeter.caloParams_2025_v0_2_newTauIsoLUT_cfi"
# CALOPARAMS = "L1Trigger.L1TCalorimeter.caloParams_2025_v0_2_Iso_eff0p7_18_27_LUT_cfi"

options = VarParsing.VarParsing ('analysis')
options.register ('skipEvents',
                  -1, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "Number of events to skip")
options.register ('JSONfile',
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "JSON file (empty for no JSON)")
options.register ('caloParams',
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "which caloParams to use?")
options.register ('globalTag',
                  "150X_dataRun3_Prompt_v1", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "which globalTag to use?")
options.outputFile = 'NTuple_MC.root'
options.inputFiles = []
options.maxEvents  = -999
options.parseArguments()

process = cms.Process("TagAndProbe", eras.Run3)
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('TagAndProbeIntegrated.TagAndProbe.tau_tagAndProbeRun3_cff')

# process.load(options.caloParams)
process.GlobalTag.globaltag = options.globalTag

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2025C/Muon0/MINIAOD/PromptReco-v1/000/392/751/00000/41f801e8-a2cb-4fac-a8c8-a19157b8ac24.root'
    ),
)

if doReEmulation:
    process.source.secondaryFileNames = cms.untracked.vstring(
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/0363f108-02cc-4957-ac1e-90554b2b28b6.root",
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/078462ad-ea85-4775-9980-beb6efad43d6.root",
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/1860a11d-dccb-40b6-8a41-3589c9fd3a00.root",
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/39ff3c4d-477c-4f13-bd35-cea2c388dca4.root",
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/7bf79f4d-fd77-41ee-bdf4-de0901567233.root",
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/ae828996-09b1-44a6-b48b-7108e580446f.root",
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/c5633988-8898-49df-a1d5-9b6bcbb6f287.root",
        "/store/data/Run2025C/Muon0/RAW/v1/000/392/751/00000/c6bf4ab8-ae16-4902-a1ec-73eb0e05cc6b.root"
    )


if options.JSONfile:
    print("Using JSON: " , options.JSONfile)
    process.source.lumisToProcess = LumiList.LumiList(filename = options.JSONfile).getVLuminosityBlockRange()

if options.inputFiles:
    process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(150)
)

if options.maxEvents >= -1:
    process.maxEvents.input = cms.untracked.int32(options.maxEvents)
if options.skipEvents >= 0:
    print("Skipping ",options.skipEvents," events")
    process.source.skipEvents = cms.untracked.uint32(options.skipEvents)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

## L1 emulation stuff
process.p = cms.Path(
    process.TAndPseq +
    process.NtupleSeq
)

if doReEmulation:
    process.schedule = cms.Schedule()
    if not isMC:
        from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAWsimHcalTP
        process = L1TReEmulFromRAWsimHcalTP(process)
        process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
        process.HcalTPGCoderULUT.nPedWidthsForZS = cms.double(3)
        process.HcalTPGCoderULUT.overrideDBnPedWidthsForZS = cms.bool(True)
        print("From Re-emulation", L1TReEmulFromRAWsimHcalTP)
        # from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 
        # process = L1TReEmulFromRAW(process)
    else:
        from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAW
        process = L1TReEmulMCFromRAW(process) 
        from L1Trigger.Configuration.customiseUtils import L1TTurnOffUnpackStage2GtGmtAndCalo 
        process = L1TTurnOffUnpackStage2GtGmtAndCalo(process)
    process.load( CALOPARAMS )
    process.p = cms.Path(
        process.TAndPseq +
        process.RawToDigi +
        process.L1TReEmul +
        process.NtupleSeq
    )
process.schedule = cms.Schedule(process.p)


# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# Adding ntuplizer
process.TFileService=cms.Service('TFileService',fileName=cms.string(options.outputFile))
