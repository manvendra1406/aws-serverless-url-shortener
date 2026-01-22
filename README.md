# Serverless URL Shortener on AWS

A simple serverless URL shortener built using core AWS services, designed to demonstrate cloud-native architecture and CCP-level concepts.

## Architecture
API Gateway → AWS Lambda → DynamoDB

## AWS Services Used
- AWS Lambda (Python)
- Amazon API Gateway (REST API)
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## How It Works
- POST request creates a short URL
- GET request redirects to the original URL
- DynamoDB stores URL mappings
- API Gateway handles routing
- Lambda contains business logic

## Security
- IAM role with least-privilege (DynamoDB access)
- API Gateway invokes Lambda via resource-based policy

## Cost
Runs on AWS Free Tier / near-zero cost.

## Possible Improvements
- Custom domain with Route53
- DynamoDB TTL for link expiry
- Infrastructure as Code (SAM / Terraform)
- Rate limiting
