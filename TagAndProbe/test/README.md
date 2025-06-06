## Making re-emulated Ntuples in CRAB

The file `tau_tagAndProbeRun3.py` can be configured to run unpacked or re-emulation. Only the events passing the TagAndProbe selection are re-emulated. The confuration on the top of `tau_tagAndProbeRun3.py` is self explanatory. Note : the GT and caloparams have to be set appropriately every time the re-emulation is done.

The same workflow for MC has been updated in the `tau_noTagAndProbe.py`. One can use this for making re-emulated taus using gen-matching procedure (insted of tag-and-probe).

For submission to crab we use the `secondaryInputDataset` feature available to pick up the parent RAW files of the input MiniAOD. To configure the submission populate the following appropriately in `crab3_config.py` : 
* `requestName`
* `inputDataset` , `secondaryInputDataset`
* `outLFNDirBase`,`site`,`outLFNDirBase`,`storageSite`

A template setting is given in the `crab3_config.py`

To submit the job one can use
```
crab submit crab3_config.py
```
It is always good practice to submit the crab-job outside of `src` directory



## Making the MiniAOD-RAW skim
The `tau_tagAndProbeRun3_skimmer.py` can be used to make a skim of the events used for the re-emulation of L1 objects as well as do the offline selection on MiniAOD-Taus. The output file from this can be used to run `tau_tagAndProbeRun3.py`
This file can also be submitted to crab for skimming a good set of taus
