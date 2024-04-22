source /opt/exp_soft/cms/t3/t3setup

## AVAILABLE COMMAND OPTIONS
## python submitOnTier3.py --inFileList \
##                         --inJson \
##                         --outFolder \
##                         --nJobs \
##                         --run \
##                         --queue \
##                         --objType \
##                         --jobType \
##                         --allBXs \
##                         --simHcalTP \
##                         --caloParams \
##                         --globalTag

python submitOnTier3.py --inFileList muon_datasets_Run3/Muon_Run2024B-PromptReco-v1_MINIAOD.txt \
                        --outFolder Run3_2024/Muon_Run2024B-v1_RAW_379243_252_253/ntuples \
                        --objType tau \
                        --jobType tagAndProbe \
                        --inJson Collisions24_13p6TeV_378981_379253_DCSOnly_TkPx.json \
                        --nJobs 100 \
                        --run Run3 \
                        --queue short \
                        --globalTag 140X_dataRun3_Prompt_v2 \
                        --caloParams L1Trigger.L1TCalorimeter.caloParams_2023_v0_4_cfi

# ########################################################################################
# ################################ DYToLL MC productions #################################
# ########################################################################################
# 
# ## MINIAOD -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList MC_for_taus/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8__Run3Winter24_MINIAOD.txt \
#                         --outFolder Run3_2024/2024W-MC_caloParams_2023_v0_4_cfi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8__Run3Winter24_MINIAOD \
#                         --objType tau \
#                         --jobType noTagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 140X_mcRun3_2023_realistic_v1 \
#                         --caloParams None
# 
# ## RAW -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList MC_for_taus/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8__Run3Winter24_GEN-SIM-RAW.txt \
#                         --outFolder Run3_2024/2024W-MC_caloParams_2023_v0_4_cfi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8__Run3Winter24_GEN-SIM-RAW \
#                         --jobType reEmulL1_MC \
#                         --inJson None \
#                         --nJobs 500 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 140X_mcRun3_2023_realistic_v1 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2023_v0_4_cfi
# 
# 
# ##############################################################################################
# ################################ VBFHToTauTau MC productions #################################
# ##############################################################################################
# 
# ## MINIAOD -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList MC_for_taus/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_MINIAOD.txt \
#                         --outFolder Run3_2024/2024W-MC_caloParams_2023_v0_4_cfi/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_MINIAOD \
#                         --objType tau \
#                         --jobType noTagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 140X_mcRun3_2023_realistic_v1 \
#                         --caloParams None
# 
# ## RAW -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList MC_for_taus/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_GEN-SIM-RAW.txt \
#                         --outFolder Run3_2024/2024W-MC_caloParams_2023_v0_4_cfi/VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_GEN-SIM-RAW \
#                         --jobType reEmulL1_MC \
#                         --inJson None \
#                         --nJobs 500 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 140X_mcRun3_2023_realistic_v1 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2023_v0_4_cfi
# 
# 
# #################################################################################################
# ################################ GluGluHToTauTau MC productions #################################
# #################################################################################################
# 
# ## MINIAOD -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList MC_for_taus/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_MINIAOD.txt \
#                         --outFolder Run3_2024/2024W-MC_caloParams_2023_v0_4_cfi/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_MINIAOD \
#                         --objType tau \
#                         --jobType noTagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 140X_mcRun3_2023_realistic_v1 \
#                         --caloParams None
# 
# ## RAW -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList MC_for_taus/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_GEN-SIM-RAW.txt \
#                         --outFolder Run3_2024/2024W-MC_caloParams_2023_v0_4_cfi/GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8__Run3Winter24_GEN-SIM-RAW \
#                         --jobType reEmulL1_MC \
#                         --inJson None \
#                         --nJobs 500 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 140X_mcRun3_2023_realistic_v1 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2023_v0_4_cfi


##############################################################################################
############################### SingleMuon 13TeV - ERA 2023D #################################
##############################################################################################

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon_Run2023D-v1_RAW.txt \
#                         --outFolder Run3_2024/Muon_Run2023D/Muon_Run2023D-v1_RAW \
#                         --objType tau \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson Cert_Collisions2023_eraD_369803_370790_Golden.json \
#                         --nJobs 5000 \
#                         --queue short \
#                         --globalTag 133X_dataRun3_Prompt_v2 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2023_v0_4_cfi
# 
# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon_Run2023D-PromptReco-v1_MINIAOD.txt \
#                         --outFolder Run3_2024/Muon_Run2023D/Muon_Run2023D-PromptReco-v1_MINIAOD \
#                         --objType tau \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2023_eraD_369803_370790_Golden.json \
#                         --nJobs 150 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 133X_dataRun3_Prompt_v2 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2023_v0_4_cfi
# 
##############################################################################################
############################### SingleMuon 13TeV - single runs ###############################
##############################################################################################

## MINIAOD -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList muon_datasets_Run2/Run323775__Run2018D__SingleMuon__UL2018_MiniAODv2-v3__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Run323775__SingleMuon__Run2018D-v1__MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 300 \
#                         --run Run2 \
#                         --queue short \
#                         --globalTag 124X_dataRun2_v2 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2018_v1_3_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run2/SingleMuon__Run2018D-PromptReco-v2__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon__Run2018D-PromptReco-v2__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 300 \
#                         --run Run2 \
#                         --queue short \
#                         --globalTag 124X_dataRun2_v2 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2018_v1_3_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run2/SingleMuon__Run2018D-UL2018_MiniAODv2-v3__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon__Run2018D-UL2018_MiniAODv2-v3__MINIAOD__GoldenJSON__WMassCutFalse__ZMassCutFalse \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 300 \
#                         --run Run2 \
#                         --queue short \
#                         --globalTag 124X_dataRun2_v2 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2018_v1_3_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run2/SingleMuon__Run2018A-UL2018_MiniAODv2-v3__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2018A_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 300 \
#                         --run Run2 \
#                         --queue short \
#                         --globalTag 124X_dataRun2_v2 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2018_v1_3_cfi

## RAW -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList muon_datasets_Run2/Run323775__SingleMuon__Run2018D-v1__RAW.txt \
#                         --outFolder Run3preparation_2022/Run323775__SingleMuon__Run2018D-v1__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run2 \
#                         --queue short \
#                         --globalTag 124X_dataRun2_v2 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2018_v1_3_cfi


##############################################################################################
############################## SingleMuon 13.6TeV - single runs ##############################
##############################################################################################

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022B-PromptReco-v1__Run355414__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022B_Run355414_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022B-PromptReco-v1__Run355417__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022B_Run355417_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022B-PromptReco-v1__Run355418__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022B_Run355418_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022B-PromptReco-v1__Run355769__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022B_Run355769_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022C-PromptReco-v1__Run355865__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022C_Run355865_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022C-PromptReco-v1__Run355872__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022C_Run355872_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022C-PromptReco-v1__Run355913__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022C_Run355913_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022C-PromptReco-v1__Run356375__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022C_Run356375_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022C-PromptReco-v1__Run356378__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022C_Run356378_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/SingleMuon__Run2022C-PromptReco-v1__Run356381__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/SingleMuon_Run2022C_Run356381_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_1_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022G-PromptReco-v1__Run362696__MINIAOD.txt \
#                         --outFolder Run3preparation_2023/2023_02_10_optimizationV0/Muon_Run2022G-PromptReco-v1_Run362696_MINIAOD \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_eraG_362433_362760_Golden.json \
#                         --nJobs 231 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

## RAW -----------------------------------------------------------------------------------
# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022G-v1__RAW.txt \
#                         --outFolder Run3preparation_2023/Muon_Run2022G-v1__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --allBXs 0 \
#                         --inJson Cert_Collisions2022_355100_362760_Golden.json \
#                         --nJobs 8200 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi


##############################################################################################
############################### SingleMuon 13.6TeV - full eras ###############################
##############################################################################################

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022C-PromptReco-v1__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Muon__Run2022Cpre-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_eraC_355862_357482_Golden_pre.json \
#                         --nJobs 250 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_2_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022C-PromptReco-v1__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Muon__Run2022Cpost-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_eraC_355862_357482_Golden_post.json \
#                         --nJobs 250 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_4_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022D-PromptReco-v1-2__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Muon__Run2022D-PromptReco-v1-2__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_eraD_357538_357900_Golden.json \
#                         --nJobs 150 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_4_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022E-PromptReco-v1__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Muon__Run2022E-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_eraE_359022_360331_Golden.json \
#                         --nJobs 250 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_4_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022F-PromptReco-v1__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Muon__Run2022F-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_eraF_360390_362167_Golden.json \
#                         --nJobs 500 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022G-PromptReco-v1__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Muon__Run2022G-PromptReco-v1__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_eraG_362433_362760_Golden.json \
#                         --nJobs 100 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

# python submitOnTier3.py --inFileList muon_datasets_Run3/Muon__Run2022BtoG-PromptReco__MINIAOD.txt \
#                         --outFolder Run3preparation_2022/Muon__Run2022FullRun3BtoG-PromptReco__MINIAOD__GoldenJSON__WMassCutTrue__ZMassCutTrue \
#                         --jobType tagAndProbe \
#                         --inJson Cert_Collisions2022_355100_362760_Golden.json \
#                         --nJobs 2000 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi


##############################################################################################
####################################### ZeroBias 13TeV #######################################
##############################################################################################

# python submitOnTier3.py --inFileList EphemeralZeroBias_Run2/EphemeralZeroBias_2018D_Run323775.txt \
#                         --outFolder Run3preparation_2022/EphemeralZeroBias_2018D_Run323775_allBXbits__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 361 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

# python submitOnTier3.py --inFileList EphemeralZeroBias_Run2/EphemeralZeroBias_2018D_Run323755.txt \
#                         --outFolder Run3preparation_2022/EphemeralZeroBias_2018D_Run323755_allBXbits__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 361 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi


##############################################################################################
###################################### ZeroBias 13.6TeV ######################################
##############################################################################################

# there are also the ZeroBias* datasets --> they can be used only after requiring the HLT_ZeroBias_v* path to be true !!

# python submitOnTier3.py --inFileList EphemeralZeroBias_Run3/EphemeralZeroBias0__Run2022D-v1__Run357696__RAW.txt \
#                         --outFolder Run3preparation_2022/EphemeralZeroBias0__Run2022D_Run357696__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

# python submitOnTier3.py --inFileList EphemeralZeroBias_Run3/EphemeralZeroBias0__Run2022E-v1__Run359998__RAW.txt \
#                         --outFolder Run3preparation_2022/EphemeralZeroBias0__Run2022E_Run359998__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

# python submitOnTier3.py --inFileList EphemeralZeroBias_Run3/EphemeralZeroBias0__Run2022F-v1__Run360820__RAW.txt \
#                         --outFolder Run3preparation_2022/EphemeralZeroBias0__Run2022F_Run360820__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 50 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

# python submitOnTier3.py --inFileList EphemeralZeroBias_Run3/EphemeralZeroBias0__Run2022G-v1__Run362616__RAW.txt \
#                         --outFolder Run3preparation_2023/EphemeralZeroBias0__Run2022G_Run362616__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 279 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi

# python submitOnTier3.py --inFileList EphemeralZeroBias_Run3/EphemeralZeroBias0__Run2022G-v1__Run362617__RAW.txt \
#                         --outFolder Run3preparation_2023/EphemeralZeroBias0__Run2022G_Run362617__RAW \
#                         --jobType reEmulL1_zeroBias \
#                         --inJson None \
#                         --nJobs 245 \
#                         --run Run3 \
#                         --queue short \
#                         --globalTag 124X_dataRun3_Prompt_v10 \
#                         --caloParams L1Trigger.L1TCalorimeter.caloParams_2022_v0_6_cfi


