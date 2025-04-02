terraform {
  backend "s3" {
    bucket	= "is698-lab7-terraform-state"
    key		= "terraform/state.tfstate"
    region	= "us-east-2"
    encrypt	= true
    dynamodb_table	= "is698-lab7a-terraform-lock"
  }
}

resource "aws_instance" "is698-lab7" {
  ami	= "ami-0030e9fc5c777545a"
  instance_type	= "t2.micro"
  tags = {
    Name = "IS698-lab7-Terraform-test-instance"
  }
}

