HRMS ON AWS
# HRMS on AWS : Human Resource Management System

This project is a cloud-based **Human Resource Management System (HRMS)** built using AWS Free Tier services. It aims to streamline HR tasks such as employee record management, role assignment, and attendance tracking using scalable and cost-effective AWS solutions.

---

# Project Overview

- A serverless HRMS system designed to operate entirely within the **AWS Free Tier**
- Demonstrates how to architect, develop, and deploy cloud-native business applications
- Focuses on integrating key AWS services like:
  - **Amazon S3** (data storage and static website hosting)
  - **AWS Lambda** (serverless compute)
  - **Amazon DynamoDB** (NoSQL database)
  - **Amazon API Gateway** (REST API endpoints)
  - **IAM Roles & Policies** (secure access management)

---

# Features

- Add, update, and remove employee records
- Role-based access control (Admin vs Employee)
- Track attendance and leave applications
- Simple frontend connected via REST API
- Fully deployed without using paid AWS services

---

# Tech Stack

- **Frontend:** HTML, CSS, JavaScript (to be hosted on S3)
- **Backend:** AWS Lambda (Python)
- **Database:** Amazon DynamoDB
- **API Management:** Amazon API Gateway
- **Authentication:** AWS IAM (basic role segregation)
- **Deployment:** AWS Console and CLI

---


## Security Considerations

- IAM policies are scoped using the principle of least privilege
- API endpoints are secured via key-based access (or Cognito, if added)
- No sensitive data is stored or shared publicly

---

## What I Learned

- Practical use of AWS services in building a production-style system
- API management and authentication via IAM
- Serverless backend deployment and scaling concepts
- Structuring cloud-native applications using best practices

---

## How to Deploy

1. Clone this repo
2. Set up S3 static hosting for the frontend
3. Deploy Lambda functions and link with API Gateway
4. Configure DynamoDB tables
5. Test endpoints and connect frontend



