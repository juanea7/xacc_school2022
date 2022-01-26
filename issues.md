# Issues

## Running from command line

### Stuck at **Run vpl: Step synth: Started**

You can check for an error here `cat _x/link/vivado/vpl/runme.log | grep ERROR`. If the error message is `ERROR: /opt/Xilinx/Vitis_HLS/2021.1/bin/unwrapped/lnx64.o/vrs does not exist`

Solution

```sh
sudo cp /opt/Xilinx/Vitis/2021.1/bin/unwrapped/lnx64.o/vrs /opt/Xilinx/Vitis_HLS/2021.1/bin/unwrapped/lnx64.o/vrs
```

## Vitis

### Vitis setup environment

When you launch a new terminal, you always have to setup the environment to be able to use the FPGA. Run this:

```sh
source ~/aws-fpga/vitis_setup.sh
source ~/aws-fpga/vitis_runtime_setup.sh
```

If you see `No device found` error, running the previous commands most likely will solve it.

## PYNQ

### PYNQ setup environment

Before launching the Jupyter lab to use PYNQ, you have to setup the environment. In a new terminal run:

```sh
source ~/aws-fpga/vitis_runtime_setup.sh
source ~/anaconda3/bin/activate
cd ~/pynq-notebooks
jupyter lab
```

### "AttributeError: module 'pynq' has no attribute 'ps'"

Solution, close the browser and stop jupyter lab, then run:

```sh
source ~/aws-fpga/vitis_runtime_setup.sh
jupyter lab
```

### ModuleNotFoundError: No module named 'nest_asyncio'

When running the PYNQ installation instructions, **before** the last command to launch jupyter lab, run the following in the terminal:

```console
pip install nest_asyncio
```

If you already started Jupyter and see this error, open a new terminal and run the following: 

```console
   source ~/anaconda3/bin/activate
   pip install nest_asyncio
```

In Jupyter Lab, from the **Kernel** menu, click **Restart Kernel...** and then continue with the lab.