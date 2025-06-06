import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
from Configuration.AlCa.autoCond import autoCond

isMC=True
doReEmulation=True
CALOPARAMS = "L1Trigger.L1TCalorimeter.caloParams_2025_v0_2_cfi"
CALOPARAMS = "L1Trigger.L1TCalorimeter.caloParams_2025_v0_2_newTauIsoLUT_cfi"


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
options.register ('globalTag',
                  "142X_mcRun3_2025_realistic_v1", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "which globalTag to use?")
options.outputFile = 'NTuple.root'
options.inputFiles = []
options.maxEvents  = -999
options.parseArguments()

process = cms.Process("TagAndProbe", eras.Run3)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('TagAndProbeIntegrated.TagAndProbe.tau_noTagAndProbe_MC_cff')

process.GlobalTag.globaltag = options.globalTag

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # dummy for creation
        '/store/mc/Run3Winter25MiniAOD/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/MINIAODSIM/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/052c86f3-0c74-417e-b2e2-119b77b89be1.root'
    )
)

if doReEmulation:
    process.source.secondaryFileNames = cms.untracked.vstring(
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/51bcce0f-dbb2-4c30-9dcd-2321eccd4348.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/647ca0ca-f309-428a-9aa6-250b86c668a5.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/ba602454-8680-4229-8fde-61157571f9f3.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/c31ab358-9788-4da0-9384-b96b018b0711.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/ca95a3b8-e082-4aae-a439-728df6252c17.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/10db875a-9a58-40b7-ac55-fb3a77676fd5.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/25679207-8c68-4b9c-bbc1-ac34d1dc8ae6.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/ca527f56-756e-4295-852c-942d9320a707.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/cd0814ff-845f-4c13-8bfd-a26e8e73b65d.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/e2a92be9-bde4-455e-a999-374ac026c733.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/5d4df0f5-46d6-432f-8e04-1d0ad244a203.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/768396dc-dda6-4899-be5b-cef709cf57f4.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/8ac73202-2dd8-4277-b830-1430b5280a92.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/9e93970a-d63e-4437-a5b9-06dcac68dab1.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/f1a728e2-7a90-41b3-9d28-3575a192170e.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/360d4b94-e26a-419b-9e2c-e71cbba396de.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/656f19e4-6424-4754-9d58-4f34f7c7f78a.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/bb7440c2-df14-4899-9226-a0c55ab03c87.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/c7f752ff-f4cf-4c96-bf17-57cb27eb1e10.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/faf00df1-1c9b-4dfe-92cf-ecf16c6c3e68.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/11511cb0-19dc-497a-9742-f36faa7326cb.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/546330e5-d2b2-4e67-a10a-8aa50e0e7379.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/5ce0dd28-67ad-4ffa-86d0-cb2fb84eb4d8.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/dcedde4f-2714-4a30-be89-94612edb80b3.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/f29b2ea1-df20-4989-a053-c927d88b039c.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/28147d40-45b5-4e25-909e-303729cc4c39.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/4756fe33-f814-44fa-813a-aa7ff9491cc3.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/54c90600-8f61-43fa-8def-86aad47ef074.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/6b2f0654-6895-4566-a106-ebc6ee8b9fba.root",
    "/store/mc/Run3Winter25Digi/GluGluHto2Tau_Par-MH-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/GEN-SIM-RAW/142X_mcRun3_2025_realistic_v7_ext1-v2/140000/e0c3f0d7-2f07-4ac0-993f-a12f4f1152d9.root",

    )


if options.JSONfile:
    print("Using JSON: " , options.JSONfile)
    process.source.lumisToProcess = LumiList.LumiList(filename = options.JSONfile).getVLuminosityBlockRange()

if options.inputFiles:
    process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

if options.maxEvents >= -1:
    process.maxEvents.input = cms.untracked.int32(options.maxEvents)
if options.skipEvents >= 0:
    process.source.skipEvents = cms.untracked.uint32(options.skipEvents)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.p = cms.Path(
    process.TAndPseq +
    process.NtupleSeq
)

if doReEmulation:
    process.schedule = cms.Schedule()
    if not isMC:
        from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 
        print(L1TReEmulFromRAW)
        process = L1TReEmulFromRAW(process)
    else:
        from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAW
        process = L1TReEmulMCFromRAW(process) 
        from L1Trigger.Configuration.customiseUtils import L1TTurnOffUnpackStage2GtGmtAndCalo 
        process = L1TTurnOffUnpackStage2GtGmtAndCalo(process)
    process.load( CALOPARAMS )
    process.p = cms.Path(
        process.TAndPseq +
        process.RawToDigi +
        process.caloStage2Digis +
        process.L1TReEmul +
        process.NtupleSeq
    )

process.schedule = cms.Schedule(process.p)




# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# Adding ntuplizer
process.TFileService=cms.Service('TFileService',fileName=cms.string(options.outputFile))
