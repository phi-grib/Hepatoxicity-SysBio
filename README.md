In this repository we provide the source code that computes the hepatoxicity for certain compounds based on the......

We provide a script to compute the FVA analysis of the human hepatocytes based on the Recon 2 metabolic models using the COBRA package in [recon2_fva](recon2_fva)

We provide a smaple jupyter notebook that performs the hepatoxocity calculations for 3 statins in [statins_notebook](notebook)

All the python scripts and the jupyter notebook can be run on a conda environment that specifies completely the dependencies needed.

The conda environment can be created from them yml file provided

```bash
conda env create --name sysbio_hptx -f sysbio_hptx.yml
```
once the environment is created can be activated in Linux

```bash
source activate sysbio_hptx
```

This environment has been tested in Linux64 platforms
