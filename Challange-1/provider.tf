terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = var.region
  access_key = "AKIARQVTVXZVMSKWHJMJ"
  secret_key = "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"
}
