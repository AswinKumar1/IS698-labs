provider "aws" {
  region 	= "us-east-2"
}

resource "aws_instance" "web" {
  count 	= 3
  ami		= "ami-0030e9fc5c777545a"
  instance_type	= "t2.micro"
  tags = {
    Name = "IS698-Terraform-Instance-${count.index}"
  }
}
