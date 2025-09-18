# TEMPLATE used for automatic script submission of multiple datasets

from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'Muon1-re-emu-2025C-caloparams-2025-LUT0p7-17-30'
config.General.workArea = 'Crab3WorkArea'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'tau_tagAndProbeRun3_calop0p7.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/Muon1/Run2025C-PromptReco-v1/MINIAOD'
config.Data.secondaryInputDataset= '/Muon1/Run2025C-v1/RAW'

config.Data.inputDBS = 'global'
config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 25000 #number of events per jobs
config.Data.totalUnits = -1 #number of event
config.Data.outLFNDirBase = '/store/user/ramellar/tau_run3_2025'
config.Data.runRange = '392672-392997'
config.Data.lumiMask = '../DataCertificationJsons/Collisions25_13p6TeV_Latest.json'
config.Data.publication = False
config.Data.allowNonValidInputDataset = True
#config.Data.outputDatasetTag = 'TagAndProbe_TagAndProbe_RelValZEE_13UP16_2016_LATEST'
config.section_("Site")
config.Site.storageSite = 'T2_FR_GRIF_LLR'
