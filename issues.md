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

```sh
pip install nest_asyncio
```

If you already started Jupyter and see this error, open a new terminal and run the following: 

```sh
source ~/anaconda3/bin/activate
pip install nest_asyncio
```

In Jupyter Lab, from the **Kernel** menu, click **Restart Kernel...** and then continue with the lab.

### When AFI is created, the application cannot be run as it can't find the AWSXCLBIN

Some applications hard-code the name of an XCLBIN into the host code. The XCLBIN extension can't be changed, so this will not work for .AWSXCLBIN files.

E.g. In the following line, the kernel name is hardware coded. The `find_binary_file()` function will return a string with with the kernel name + .xclbin appended. This won't work for AWSXCLBIN files. 
https://github.com/Xilinx/Vitis_Libraries/blob/4bd100518d93a8842d1678046ad7457f94eb355c/vision/L2/examples/3dlut/xf_3dlut_tb.cpp#L247 

A better way is to allow the user to pass the XCLBIN or the AWSXCLBIN as a paramter to our application.
You might then call your application like this:
`my_application.exe my_binary.awsxclbin`

Example of hostcode that does this:
https://github.com/Xilinx/xup_compute_acceleration/blob/3e429ca20cd3bfe125b5aa2ca5a14d0b837442d4/sources/vadd_lab/vadd.cpp#L72
