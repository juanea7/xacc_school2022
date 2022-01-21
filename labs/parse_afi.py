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

for afi in afis:
    desc = afi['Description']
    if "XACC" in desc:
        print(bcolors.OKGREEN + bcolors.UNDERLINE +
            f"AFI ID: {afi['FpgaImageId']}" + bcolors.ENDC +
            f"; name: {afi['Name']}; "
            f"create time: {afi['CreateTime']}; description: {desc};")