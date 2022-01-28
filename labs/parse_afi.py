# Copyright (C) 2022 Xilinx, Inc
#
# SPDX-License-Identifier: BSD-3-Clause

import subprocess
import json
import warnings

__author__ = "Mario Ruiz"
__copyright__ = "Copyright 2022, Xilinx"

class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

output = subprocess.run(['aws', 'ec2', 'describe-fpga-images', '--owners',
    'self', '--region', 'us-east-1'], stdout=subprocess.PIPE, 
    universal_newlines=True)

if output.returncode != 0:
    warnings.warn('aws ec2 describe-fpga-images did not work')

details = json.loads(output.stdout)

afis = details['FpgaImages']


xacc_afis = list()
for afi in afis:
    desc = afi['Description']
    create_time = afi['CreateTime']
    if "2022" in create_time:
        fpga_image = afi['FpgaImageId']
        xacc_afis.append(fpga_image)
        print(bcolors.OKGREEN + bcolors.UNDERLINE +
            f"AFI ID: {fpga_image}" + bcolors.ENDC +
            f"; name: {afi['Name']}; "
            f"create time: {afi['CreateTime']}; description: {desc};")

print(f"XACC AFIs {len(xacc_afis)}, total AFIs {len(afis)}")
print(f"list of AFIs {xacc_afis}")