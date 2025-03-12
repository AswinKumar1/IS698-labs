provider "aws" {
 region = "us-east-2"
}

resource "aws_instance" "my-ec2" {
 ami		= "ami-0030e9fc5c777545a"
 instance_type	= "t2.micro"
 tags = {
   Name = "terraform-IS-698-lab5"
 }
}

