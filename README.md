# CampusConnect
### Opportunities Within Your Reach

CampusConnect is a serverless student opportunity and resource finder built with AWS.

It helps university students discover scholarships, internships, professional certifications, and free learning resources from one platform.

## Problem Statement

Students often struggle to find reliable information about scholarships, internships, and professional development opportunities because these resources are scattered across different platforms.

## Our Solution

CampusConnect provides a centralized platform where students can:
- Discover learning opportunities.
- Find scholarships and internships.
- Explore professional certifications.
- Search and filter available opportunities.
- Access external opportunity links.

## AWS Architecture

The project uses the following AWS services:

- **Amazon S3:** Hosts the static website.
- **Amazon API Gateway:** Provides HTTP API endpoints.
- **AWS Lambda:** Handles backend application logic using Python.
- **Amazon DynamoDB:** Stores opportunity records.

### How It Works

1. Students access the website hosted on Amazon S3.
2. The frontend sends requests to API Gateway.
3. API Gateway invokes the Lambda function.
4. Lambda retrieves opportunity records from DynamoDB.
5. The results are returned and displayed on the website.

## Technologies

- HTML
- CSS
- JavaScript
- Python
- AWS Boto3
- Amazon S3
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB

## Live Demo

http://campusconnect-studrnts-hub-2026-afe.s3-website-us-east-1.amazonaws.com/

## API Endpoint

https://0z8lml1mn3.execute-api.us-east-1.amazonaws.com/prod/opportunities

## Current Project Status

The frontend is deployed and connected to the AWS backend. Opportunity records are retrieved from DynamoDB and displayed dynamically on the website.

## Future Improvements

- Secure administrator dashboard.
- Authentication and authorization.
- Secure opportunity submission.
- CloudFront integration for HTTPS.
- Expanded opportunity listings.

## Project Vision

To make valuable educational and career opportunities easier for students to discover and access.

**Built with AWS. Designed for Students. Driven by Opportunities.**
