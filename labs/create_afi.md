# Creating an Amazon FPGA Image (AFI)

This document guides you through the steps to create an AWS Amazon FPGA Image (AFI) which can run on AWS EC2 F1 instance to verify that the design works in hardware. It assumes that a full system (Vitis project) is built which consists of an *host* application (executable file) and an FPGA binary file (.xclbin).

This guide is part of the 2022 XACC winter school.

### Create an AFI

To execute the application on F1, the following files are needed:

- Host application (executable file)
- Amazon FPGA Image (awsxclbin)

The awsxclbin is an Amazon specific version of the FPGA binary file (xclbin) produced by the Vitis software.

The awsxclbin can be created by running the *create\_vitis\_afi.sh* script which is included in the [aws-fpga GitHub repository](https://github.com/aws/aws-fpga).

1. Open a new terminal (`Terminator`)

1. Navigate to the folder where the (Hardware) xclbin is located

    ```sh
    cd ~/workspace/<application_name>/Hardware/
    ```

1. Source `vitis_setup.sh`

    ```sh
    source $AWS_FPGA_REPO_DIR/vitis_setup.sh
    ```

1. Configure bucket region

    ```sh
    aws configure set region us-east-1
    ```

1. Rename the xclbin file to a meaningful name. This name is used in the AFI name/description

   For instance for a vision application:

   ```sh
   cp binary_container_1.xclbin vision_filter2d.xclbin
   ```

1. Include your name in the AFI description

   To make your AFI more easily identifiable, include your name in the description field

   ```sh
   export DESC="XACC School 2022 <YOUR NAME GOES HERE>"
   sed -i "s/--description\ \${stripped_xclbin}/--description\ '$DESC'/g" $VITIS_DIR/tools/create_vitis_afi.sh
   ```

1. Create an AFI by running the `create_vitis_afi.sh` script

    ```sh
    $VITIS_DIR/tools/create_vitis_afi.sh -xclbin=<xclbin_file>.xclbin -s3_bucket=xilinx-labs-virginia -s3_dcp_key=dcp -s3_logs_key=log
    ```
    
    In the above command, set your *xclbin* file as `<filename>`. Note that the `s3_bucket=xilinx-labs-virginia` is only valid for the XACC 2022 winter school

    The `create_vitis_afi.sh` script does the following:

    - Starts a background process to create the AFI
    - Generates a `*_afi_id.txt` which contains the FPGA Image Identifier (or AFI ID) and Global FPGA Image Identifier (or AGFI ID) of the generated AFIs
    - Creates the `*.awsxclbin` AWS FPGA binary file which is passed to the host application to determine which AFI should be loaded to the FPGA.
    - Uploads the `*.xclbin` to the AWS cloud for processing.

    Learn more about setting up S3 buckets [here](https://github.com/aws/aws-fpga/blob/master/Vitis/docs/Setup_AWS_CLI_and_S3_Bucket.md)  

## Check the AFI status

The AFI will become available after some time (30 minutes at least) in the AWS cloud and can then be used to program the FPGA in an AWS EC2 F1 instance. To check the AFI status, the AFI ID is required.

* In the directory the `create_vitis_afi.sh` script was run, enter the following command to find the AFI ID  

```sh
cat *afi_id.txt
```

* Enter the `describe-fpga-images` API command to check the status of the AFI generation process:

```sh
aws ec2 describe-fpga-images --fpga-image-ids <AFI_ID>
```

You can use a handy shortcut to pass the AFI id directly to the command.

```sh
aws ec2 describe-fpga-images --fpga-image-ids $(cat *afi_id.txt | sed -n '2p' | tr -d '",' | sed 's/.*://')
```

Note: When AFI creation is in progress, the *State* will be `pending`. When the AFI creation is finished, the output should show `available`:

```sh
   ...
   "State": {
       "Code": "available"
   },

   ...
```

Wait until the AFI becomes available before proceeding to execute on the F1 instance.

## Regenerate .awsxclbin

If for some reason you delete the `.awsxclbin`, you can regenerate the file as long as `*agfi_id.txt` and `*.xclbin` are present

1. Edit these variable with the corresponding name
    
    ```sh
    export xclbin=<xclbin_filename>
    export agfi_id=<*_agfi_id.txt>
    export awsxclbin=<output_name>
    ```
    
1. Generate `.awsxclbin` file

    ```sh
    xclbinutil -i $xclbin --remove-section PARTITION_METADATA --remove-section SYSTEM_METADATA --replace-section BITSTREAM:RAW:${agfi_id} -o ${awsxclbin}.awsxclbin
    ```


## Get AGFI ID from .awsxclbin

If you do not have the AGFI ID, you can get it from the `.awsxclbin` file

```sh
xclbinutil -i <filename>.awsxclbin --dump-section BITSTREAM:RAW:afgi_id.txt
```

The file `afgi_id.txt` will contain the AGFI ID

Then you can search for this AGFI in the list that is returned by this command.

```sh
aws ec2 describe-fpga-images --owners self --region us-east-1
```

## References

- https://github.com/aws/aws-fpga/tree/master/Vitis#2-create-an-amazon-fpga-image-afi
- https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-fpga-images.html

---------------------------------------
<p align="center">Copyright&copy; 2022 Xilinx</p>
