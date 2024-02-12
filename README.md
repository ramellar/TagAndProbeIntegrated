# TagAndProbe
Set of tools to evaluate eg/tau trigger performance on T&amp;P, and produce Layer-2 calibrations
This is based on the following two prior tools:
1. [TauTagAndProbe](https://github.com/jonamotta/TauTagAndProbe)
2. [TauObjectsOptimization](https://github.com/jonamotta/TauObjectsOptimization)

## Install instructions
```bash
cmsrel CMSSW_13_3_0
cd CMSSW_13_3_0/src
cmsenv
git cms-init
git cms-addpkg L1Trigger/L1TCalorimeter
git cms-addpkg L1Trigger/L1TNtuples
git cms-addpkg L1Trigger/Configuration
git cms-addpkg L1Trigger/L1TGlobal
git cms-addpkg L1Trigger/L1TCommon
git cms-addpkg L1Trigger/L1TZDC
mkdir L1Trigger/L1TZDC/data
cd L1Trigger/L1TZDC/data
wget https://raw.githubusercontent.com/cms-data/L1Trigger-L1TCalorimeter/master/zdcLUT_HI_v0_1.txt
cd -
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TCalorimeter.git L1Trigger/L1TCalorimeter/data

git clone git@github.com:mchiusi/TagAndProbeIntegrated.git -b CMSSW_13_3_0

git cms-checkdeps -A -a
scram b -j 8
```

L1T emulation relevant GlobalTags in CMSSW_13_3_0 are stored [here](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TStage2Instructions). 
* for run3 data, use latest prompt GT [here](https://twiki.cern.ch/twiki/bin/view/CMS/LatestOnlineGTs)

## Tool utilization
To do the optimization two things are needed:
* L1 objects (sometimes re-emulated) that are extracted from the RAW tier (in principle, non-re-emulated L1 objects can also be extracted from MiniAOD, but for consistency we never do that)
* Offline objects that are extracted from the AOD or MiniAOD tier

### Production of the input objects
To produce the input NTuples to the optimization the `TauTagAndProbe` package is used. The useful scripts for this are mainly in the `test` subfolder.

Jobs on ***RAW*** are submitted using `submitOnTier3_reEmulL1_zeroBias.py` which in turn launches `reEmulL1_X.py`
Before launching this you need to fix
* the Global Tag
* the configuration of the L1Calorimeter (`process.load("L1Trigger.L1TCalorimeter.caloStage2Params_20XX_vX_X_XXX_cfi")`)

Jobs on ***MiniAOD*** are submitted using `submitOnTier3.py` which in turn launches `test_noTagAndProbe.py`
Before launching this you need to fix
* the Global Tag

Jobs on ***Data*** are submitted using `submitOnTier3_reEmulL1_zeroBias.py` which in turn launches `reEmulL1_X.py`.
Before launching this you need to fix
* the `isMC` flag
* the input folder and file list

For Monte Carlo (MC), we implemented a truth matching rather than a Tag & Probe technique which would dramatically and artificially decrease the available statistics.

After having produced the input object `hadd` all the files.

### Optimization
The optimization is run in several sequential steps:
* Merge of the two inputs, match of the L1 objects to the offline ones, compression of the variables
* Calculation of the calibration, pruduction of its LUTs, and its application
* Calculation of the isolation, pruduction of its LUTs, and its application
* Prodution of turnon curves
* Evaluation of the L1 rate

Due to the package's lack of forward-compatibility with CMSSW, the optimzation is run into CMSSW_11_0_2.
Check [this](https://twiki.cern.ch/twiki/bin/view/CMSPublic/FWMultithreadedFrameworkModuleTypes#EDFilters) link in order to keep track of the lastest updates in CMSSW.
