# XACC school 2022

24 - 28 January 2022

This is a temporary repository for the XACC school and includes links to relevant presentation material (pdf, videos) and resources (lab instructions, source code) for the 2022 XACC winter school and will be updated during the school. 

**Please do NOT fork this repository**

## Schedule

[Week schedule](./schedule.md)

## Instance details

- username: centos
- password: xup_vitis2022

## Vitis setup environment

When you launch a new terminal, you always have to setup the environment to be able to use the FPGA. Run this:

```sh
source ~/aws-fpga/vitis_setup.sh
source ~/aws-fpga/vitis_runtime_setup.sh
```

If you see `No device found` error, running the previous commands most likely will solve it.

## PYNQ setup environment

Before launching the Jupyter lab to use PYNQ, you have to setup the environment. In a new terminal run:

```sh
source ~/aws-fpga/vitis_runtime_setup.sh
source ~/anaconda3/bin/activate
cd ~/pynq-notebooks
jupyter lab
```

## "AttributeError: module 'pynq' has no attribute 'ps'"

Solution, close the browser and stop jupyter lab, then run:

```sh
source ~/aws-fpga/vitis_runtime_setup.sh
jupyter lab
```

## Day 1

Day 1 lab instructions: [https://xilinx.github.io/xup_compute_acceleration/](https://xilinx.github.io/xup_compute_acceleration/)

Day 1: [Video Presentations and PDF files](https://xilinx.github.io/xup_compute_acceleration/presentations.html)

### Issues: PYNQ 

#### ModuleNotFoundError: No module named 'nest_asyncio'

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

## Day 2

- [Vision lab](https://xilinx.github.io/xup_compute_acceleration/Vision_lab.html)

- [Project 1 description](labs/project_1.md)

## Project work

[Project 1 description](labs/project_1.md)

[Teams and projects](./projects_and_teams.md)

[Single Slide PowerPoint template](./project_template.pptx)


## Support

[Vitis user guide](https://www.xilinx.com/html_docs/xilinx2021_1/vitis_doc/index.html) (We are using 2021.1)

Join the [XUP Slack workspace](https://join.slack.com/t/xupgroup/shared_invite/zt-y0zc1hqv-~Z~nYw6OMrdjXJ30IXungQ), and then join the [#xacc_school2022](https://xupgroup.slack.com/archives/C02ULU6LE21) channel. 

## Resources

[XACC resources page](https://xilinx.github.io/xacc/)

[OpenCL Khronos group](https://www.khronos.org/opencl/) (Xilinx supports OpenCL 2.X.)




---------------------------------------
<p align="center">Copyright&copy; 2022 Xilinx</p>
