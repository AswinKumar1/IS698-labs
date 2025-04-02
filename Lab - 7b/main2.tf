provider "aws" {
  region 	= "us-east-2"
}

#resource "aws_instance" "web" {
 # count 	= 3
 # ami		= "ami-0030e9fc5c777545a"
 # instance_type	= "t2.micro"
 # tags = {
 #   Name = "IS698-Terraform-Instance-${count.index}"
 # }
#}

variable "instances" {
  type = map
  default = {
    "web1" = "t2.micro"
    "web2" = "t3.micro"
    "web3" = "t2.small"
  }
}

# Adding the resource for EC2 instances using for_each
resource "aws_instance" "web" {
  for_each = var.instances 
  ami           = "ami-0030e9fc5c777545a"  
  instance_type = each.value  
  tags = {
    Name = each.key  
  }
}

