# CloudDeployX Architecture

```text
Developer
   |
   | git push
   v
GitHub
   |
   v
Jenkins
   +-- tests
   +-- Docker build
   +-- ECR push
   v
Amazon ECR
   |
   v
Amazon EKS
   +-- Deployment
   +-- Pods
   +-- LoadBalancer Service
   |
   v
CloudDeployX Application
```

Terraform creates the VPC, public/private subnets, NAT Gateway, EKS cluster and managed nodes.

Security:
- EKS API access is restricted by admin_cidr_blocks.
- Worker nodes run in private subnets.
- Terraform state is ignored by Git.
- Use IAM roles instead of long-lived AWS keys where possible.
