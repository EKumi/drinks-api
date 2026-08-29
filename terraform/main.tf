terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "drinks_api" {
  ami           = "ami-07b8fb6bd3e9627a6"
  instance_type = "t3.micro"

  tags = {
    Name = "drinks-api-server"
  }
}