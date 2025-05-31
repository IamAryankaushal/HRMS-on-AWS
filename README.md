# HRMS on AWS – Human Resource Management System

## Project Overview

This project demonstrates the development of a **cloud-native, serverless Human Resource Management System (HRMS)** hosted entirely on **AWS Free Tier services**. The application offers secure authentication, role-based access, employee data management, leave tracking, and attendance monitoring—all built using scalable and cost-effective AWS components.

> This was a **group project** developed as part of an **AWS Cloud internship** during my time at **F13 Technologies**, guided by my mentor. Team members contributed across all stages including design, development, and deployment.

---

## Key Features

- Secure login and registration using **Amazon Cognito**
- **Role-based access control** (Admin, HR, Employee)
- CRUD operations for employee records
- Attendance and leave request tracking
- Document upload and storage functionality
- Static web UI hosted on Amazon S3
- Fully within **AWS Free Tier limits**

---

## System Architecture

The application uses a **serverless architecture**, modeled in Python and diagrammed using infrastructure-as-code practices.

### Components

| Layer | AWS Services |
|-------|---------------|
| **Frontend** | Amazon S3 (Static Website), JavaScript, HTML/CSS |
| **Authentication** | Amazon Cognito (User Pool, App Client) |
| **Backend** | AWS Lambda (Business Logic) |
| **APIs** | Amazon API Gateway (REST Endpoints) |
| **Database** | Amazon DynamoDB (NoSQL Tables) |
| **Document Storage** | Amazon S3 (Private Bucket for Documents) |
| **Access Control** | AWS IAM Policies and Roles |

---

## DynamoDB Sample Table Design

- `hrms-employees`: Employee profile data  
- `hrms-leave-requests`: Leave request history  
- `hrms-attendance`: Daily check-in/out logs  

Each table uses optimized partition/sort keys and indexes for efficient querying.

---

## Project Workflow

1. **Set up IAM users and roles**
2. **Create DynamoDB tables** for employees, leave, and attendance
3. **Configure Amazon S3 buckets** for frontend hosting and document storage
4. **Set up Cognito User Pool** with app client and role attributes
5. **Deploy REST APIs** using API Gateway for each module (employee, leave, attendance, document)
6. **Write Lambda functions** for all CRUD operations
7. **Build the frontend UI** (HTML/CSS/JS) and integrate with Cognito via `auth.js`
8. **Deploy the website** by uploading frontend to S3 and linking it with Cognito and API endpoints

---

## Security & Access Control

- **Amazon Cognito** handles all user authentication and token-based session management
- **IAM roles** enforce least-privilege access to Lambda, DynamoDB, and S3
- **API Gateway** integrates token validation for all endpoints
- **Private document bucket** ensures secure storage of employee uploads

---

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript  
- **Authentication**: Amazon Cognito + auth.js  
- **Backend**: AWS Lambda (Node.js/Python)  
- **Database**: Amazon DynamoDB  
- **APIs**: Amazon API Gateway  
- **Hosting**: Amazon S3  

---

## Deployment Checklist

- [x] Create DynamoDB tables for employee, leave, attendance  
- [x] Deploy Lambda functions with appropriate IAM policies  
- [x] Configure REST APIs in API Gateway and enable CORS  
- [x] Upload frontend files to S3 and enable public access  
- [x] Configure Cognito pool and app client  
- [x] Test authentication flow and CRUD APIs

---

## Acknowledgment

This project was built as part of a **collaborative group internship** under the supervision of an AWS mentor. Each team member contributed to designing, developing, and deploying the HRMS application on the AWS platform.

---

## License

This repository is intended for educational, demonstration, and portfolio use only.
