## Making re-emulated Ntuples in CRAB

The file `tau_tagAndProbeRun3.py` can be configured to run unpacked or re-emulation. Only the events passing the TagAndProbe selection are re-emulated. The confuration on the top of `tau_tagAndProbeRun3.py` is self explanatory. Note : the GT and caloparams have to be set appropriately every time the re-emulation is done

For submission to crab we use the `secondaryInputDataset` feature available to pick up the parent RAW files of the input MiniAOD. To configure the submission populate the following appropriately in `crab3_config.py` : 
* `requestName`
* `inputDataset` , `secondaryInputDataset`
* `outLFNDirBase`,`site`,`outLFNDirBase`,`storageSite`

A template setting is given in the `crab3_config.py`

To submit the job one can do 
```
crab submit crab3_config.py
```
It is always good practice to submit the crab-job outside of `src` directory

