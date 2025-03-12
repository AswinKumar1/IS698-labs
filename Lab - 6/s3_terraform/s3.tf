resource "aws_s3_bucket" "my_is698-lab6_bucket" {
 bucket = "is698lab6"
}

resource "aws_s3_bucket_versioning" "versioning_example" {
 bucket = aws_s3_bucket.my_is698-lab6_bucket.id
 versioning_configuration {
  status = "Enabled"
 }
}


