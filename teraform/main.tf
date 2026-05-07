provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "insecure_sg" {
  name = "insecure-security-group"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "bad_bucket" {
  bucket = "aegisflow-public-bucket"

  tags = {
    Name = "AegisFlow"
  }
}