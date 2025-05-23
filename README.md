#  HRMS on AWS : Human Resource Management System

This project is a cloud-based **Human Resource Management System (HRMS)** built entirely using AWS Free Tier services. It enables secure employee management with authentication, record keeping, and REST API access—all deployed on a serverless architecture.

---

## Project Overview

- A serverless HRMS system designed to run cost-effectively within AWS Free Tier
- Uses **Amazon Cognito** for secure user authentication
- Built using AWS services like:
  - **Amazon S3** (static hosting)
  - **AWS Lambda** (serverless compute)
  - **Amazon DynamoDB** (NoSQL database)
  - **Amazon API Gateway** (REST APIs)
  - **Amazon Cognito** (authentication and user pools)
  - **IAM** (access control)

---

## Features

- Secure login and registration via Amazon Cognito
- Role-based user access (Admin and Employee)
- CRUD operations for employee records
- Attendance and leave tracking
- Responsive frontend with integrated authentication flow
- No paid services—fully AWS Free Tier compatible

---

## Authentication

- **Amazon Cognito** is used for managing user sign-up, sign-in, and token-based session management.
- A custom `auth.js` script is included in the frontend to integrate with Cognito’s hosted UI and SDK.
- Users are assigned roles post-login to control access (Admin or Employee).

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Amazon Cognito (`auth.js`)
- **Backend:** AWS Lambda (Node.js/Python)
- **Database:** Amazon DynamoDB
- **APIs:** Amazon API Gateway
- **Hosting:** Amazon S3 (Static website)

---

## Security

- Cognito handles authentication securely using industry best practices.
- IAM roles ensure minimal privileges for Lambda/API access.
- API Gateway endpoints are protected using Cognito token validation.

---

## What I Learned

- End-to-end serverless app development with AWS
- Secure authentication using Amazon Cognito
- Role-based access control for multi-user systems
- Hands-on experience with AWS Lambda, API Gateway, and DynamoDB
- Best practices for building cloud-native applications
- Static website hosting using S3 

---

## How to Deploy

1. Clone the repo and set up S3 for frontend hosting
2. Deploy Lambda functions and APIs
3. Create and configure Cognito user pool and app client
4. Connect `auth.js` to your Cognito app
5. Launch the frontend and test the flow