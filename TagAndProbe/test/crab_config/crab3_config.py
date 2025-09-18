# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'ZeroBiasrun3_2025D_394959_1'
config.General.workArea = 'Crab3WorkArea'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'reEmulL1_zeroBias.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/EphemeralZeroBias1/Run2025D-v1/RAW'
# config.Data.secondaryInputDataset= '/DYto2Tau-4Jets_Bin-MLL-50_Fil-MuTauh_TuneCP5_13p6TeV_madgraphMLM-pythia8/Run3Winter25Digi-142X_mcRun3_2025_realistic_v7-v2/GEN-SIM-RAW'

config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 25000 #number of events per jobs
config.Data.totalUnits = -1 #number of event
config.Data.outLFNDirBase = '/store/user/ramellar/tau_run3_2025'
config.Data.runRange = '394959'
config.Data.lumiMask = '../DataCertificationJsons/Collisions25_13p6TeV_Latest.json'
config.Data.publication = False
config.Data.allowNonValidInputDataset = True
#config.Data.outputDatasetTag = 'TagAndProbe_TagAndProbe_RelValZEE_13UP16_2016_LATEST'
config.section_("Site")
config.Site.storageSite = 'T2_FR_GRIF_LLR'
