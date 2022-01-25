# Delete an Amazon FPGA Image (AFI)

The number of AFIs that can be stored in the  S3 bucket is limited. For this reason, when you are done with an AFI, please delete it.

## Check AFI Status

To make sure you are deleting the correct AFI, first check the status.

```sh
aws ec2 describe-fpga-images --fpga-image-ids <AFI_ID>
```

Your name should appear here


## Delete AFI

```sh
aws ec2 delete-fpga-image --dry-run --fpga-image-id <AFI_ID>
```

### Output 

Return -> (boolean)

> Is true if the request succeeds, and an error otherwise.


## References

https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-fpga-image.html

---------------------------------------
<p align="center">Copyright&copy; 2022 Xilinx</p>
