# Project 1 Description

- Chose a L1 primitive, or L2 kernel from Vision Libraries

- Emulate it either/or SW, HW

- Build hardware (xclbin) and then [create AFI](create_afi.md)

- You can use:
  
  - [Command line (v++ & gcc/g++)](https://xilinx.github.io/xup_compute_acceleration/Vision_lab.html)
  
  - [A PYNQ Notebook](https://github.com/Xilinx/xup_compute_acceleration/tree/master/sources/vision_lab/src/pynq)

  - [Vitis GUI](vitis_accelerated_libs.md)

**Note**: make sure you configure the aws region before generating the AFI 

## Use vision lab PYNQ notebooks on the PYNQ env

```sh
cp ~/xup_compute_acceleration/sources/vision_lab/src/pynq/* ~/pynq-notebooks/FCCM-Lab/
cp ~/xup_compute_acceleration/solutions/vision_lab/vision_example.awsxclbin ~/pynq-notebooks/FCCM-Lab/
```

Then you can start jupyter lab

---------------------------------------
<p align="center">Copyright&copy; 2022 Xilinx</p>