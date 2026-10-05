provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Project     = "CloudDeployX"
      Environment = var.environment
      ManagedBy   = "Terraform"
    }
  }
}
