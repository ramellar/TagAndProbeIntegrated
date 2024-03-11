import FWCore.Utilities.FileUtils as FileUtils
from Configuration.AlCa.autoCond import autoCond
import FWCore.ParameterSet.VarParsing as VarParsing
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

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
                  "", # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.string,          # string, int, or float
                  "which globalTag to use?")
options.register ('allBXs',
                  0, # default value
                  VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                  VarParsing.VarParsing.varType.int,          # string, int, or float
                  "store information for all BXs?")
options.outputFile = 'NTuple_ZeroBias.root'
options.inputFiles = []
options.maxEvents  = -999
options.parseArguments()

process = cms.Process("ZeroBias",eras.Run3)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
if options.allBXs: process.load('TagAndProbeIntegrated.TagAndProbe.zeroBias_allbx_cff')
else:              process.load('TagAndProbeIntegrated.TagAndProbe.zeroBias_cff')

process.GlobalTag.globaltag = options.globalTag

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # dummy for creation
        '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/755/00000/02506E54-CE47-A649-9F80-117E978DC69E.root'
    ),
)

process.schedule = cms.Schedule()

# re-emulate starting from TPs (here we re-emulate also the TPs)
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAWsimHcalTP
process = L1TReEmulFromRAWsimHcalTP(process)

process.load(options.caloParams)

############################

if options.JSONfile:
    print("Using JSON: " , options.JSONfile)
    process.source.lumisToProcess = LumiList.LumiList(filename = options.JSONfile).getVLuminosityBlockRange()

if options.inputFiles:
    process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

if options.maxEvents >= -1:
    process.maxEvents.input = cms.untracked.int32(options.maxEvents)
if options.skipEvents >= 0:
    process.source.skipEvents = cms.untracked.uint32(options.skipEvents)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

# ################# Activating the latest (02/24) HCAL response corrections ############
# CONDDIR="/grid_mnt/vol_home/llr/cms/mchiusi/Run3preparation/Run3_2024/CMSSW_13_3_0/src/TagAndProbeIntegrated/HCAL_corr"
# 
# process.load('EventFilter.L1TRawToDigi.caloStage2Digis_cfi')
# process.caloStage2Digis.InputLabel = cms.InputTag('rawDataCollector')
# 
# process.es_prefer = cms.ESPrefer('HcalTextCalibrations','es_ascii')
# process.es_ascii = cms.ESSource('HcalTextCalibrations',
#    input = cms.VPSet(
#       cms.PSet(
#          object = cms.string('RespCorrs'),
# 	 file   = cms.FileInPath(CONDDIR+'/RespCorrs/HcalRespCorrs_2023_v3.0_data.txt')
#       ),
#       cms.PSet(
#          object = cms.string('Gains'),
#          file   = cms.FileInPath(CONDDIR+'/Gains/HcalGains_2023_v2.0_data.txt')
#       ),
#    )
# )
# #######################################################################################

process.p = cms.Path (
    process.RawToDigi +
    # process.caloStage2Digis +
    process.L1TReEmul +
    process.NtupleZeroBiasSeq
)
process.schedule = cms.Schedule(process.p) # do my sequence pls

# Silence output
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

# Adding ntuplizer
process.TFileService=cms.Service('TFileService',fileName=cms.string(options.outputFile))
