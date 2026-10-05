# CloudDeployX — Automated AWS Cloud Deployment Platform

End-to-end AWS + DevOps portfolio project:
GitHub → Jenkins → Docker → Amazon ECR → Amazon EKS → LoadBalancer → Flask application.

## Stack
AWS, Terraform, Jenkins, Docker, ECR, EKS, Kubernetes, Python/Flask, IAM, VPC.

## Repository
- application/ — Flask app and tests
- docker/ — Dockerfile
- terraform/ — VPC and EKS infrastructure
- kubernetes/ — namespace, deployment, service
- jenkins/ — CI/CD pipeline
- docs/ — architecture documentation

## First setup
```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars
# Edit admin_cidr_blocks to your own public IP/CIDR.
terraform init
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
```

Then:
```bash
aws eks update-kubeconfig --region ap-south-1 --name clouddeployx-eks
kubectl get nodes
```

Never commit AWS credentials, .tfstate files, kubeconfig files, passwords, or Jenkins secrets.

## Interview summary
I built CloudDeployX as an end-to-end AWS DevOps project. Terraform provisions the infrastructure, Jenkins implements CI/CD, Docker packages the application, ECR stores the image, and EKS runs it using Kubernetes. A LoadBalancer exposes the application.

## Future improvements
HTTPS/ACM, Route 53, CloudWatch dashboards, HPA, Helm, Trivy, SonarQube, remote Terraform state, blue/green deployment.
