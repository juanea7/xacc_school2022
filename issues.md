# Issues

## Running from command line

### Stuck at **Run vpl: Step synth: Started**

You can check for an error here `cat _x/link/vivado/vpl/runme.log | grep ERROR`. If the error message is `ERROR: /opt/Xilinx/Vitis_HLS/2021.1/bin/unwrapped/lnx64.o/vrs does not exist`

Solution

```sh
sudo cp /opt/Xilinx/Vitis/2021.1/bin/unwrapped/lnx64.o/vrs /opt/Xilinx/Vitis_HLS/2021.1/bin/unwrapped/lnx64.o/vrs
```