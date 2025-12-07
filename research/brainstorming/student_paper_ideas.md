# Student Research Opportunities: Bridging the Cloud Gap at MIPRO Junior

This document provides an analysis of the MIPRO Junior papers from 2010-2025 and identifies a significant opportunity for mentorship and new research topics based on your expertise in AWS and cloud technologies.

## 1. Analysis of MIPRO Junior Paper Trends

A review of the papers in `mipro_junior_papers.md` reveals the following trends:

*   **Strong Focus on AI/ML:** Recent years show a surge in projects using Deep Learning, NLP (including LLMs and Transformers), and Computer Vision. This is the most popular advanced topic.
*   **Hardware-centric Projects:** A consistent number of papers involve physical hardware, most commonly Arduino, Raspberry Pi, and various sensors for IoT or robotics applications.
*   **Classic CS Topics:** Algorithm analysis, database design, and mobile/web application development remain popular and accessible topics for students.
*   **The "Cloud Gap":** There is a significant and consistent lack of papers that explore modern cloud computing infrastructure, services, and methodologies. While "cloud" is sometimes mentioned, papers rarely focus on the practical implementation, automation, or architecture of cloud services.

**Identified Gap:** Students are not yet fully exploring topics like **Infrastructure as Code (IaC), serverless architectures, container orchestration, or cloud security**. This is a major area where your expertise as an AWS Academy Educator can guide students to produce novel and highly relevant work.

## 2. Proposed Student Paper Topics (Leveraging AWS Academy & Learner Lab)

The following are concrete, actionable paper ideas that students could develop using the resources provided by the **AWS Academy** curriculum and the **AWS Learner Lab** sandbox environment.

---

### Cloud Deployment & Automation

*   **Topic Idea:** **From Zero to Production: A Case Study on Deploying a Scalable Web Application in the AWS Learner Lab**
    *   **Description:** Students would use the Learner Lab to deploy a simple web application (e.g., a Python/Flask or Node.js app) using multiple AWS services like **EC2, RDS, and an Elastic Load Balancer**. The paper would document the architecture, the deployment process, and a simple performance benchmark.
    *   **Why it fits:** Introduces students to core IaaS/PaaS concepts in a practical way.

*   **Topic Idea:** **Automating AWS Infrastructure with Terraform: A Student Project in Infrastructure as Code**
    *   **Description:** This paper would detail a project where students define the architecture from the previous idea entirely in **Terraform**. The focus would be on the principles of IaC, versioning infrastructure in Git, and the benefits of automated, repeatable deployments.
    *   **Why it fits:** Directly addresses the "Automation" and "DevOps" gap and is a critical, in-demand industry skill.

### Serverless & Modern Architectures

*   **Topic Idea:** **A Cost and Performance Comparison: Building a REST API with Serverless (AWS Lambda) vs. Containers (Amazon ECS)**
    *   **Description:** Students would build the same simple REST API using two different architectures within the Learner Lab: one using **API Gateway and Lambda functions**, and another using **Docker containers on ECS/Fargate**. The paper would compare development time, cold-start performance, and estimated cost under a simulated load.
    *   **Why it fits:** Explores the trade-offs between two dominant cloud-native patterns and introduces FinOps concepts.

*   **Topic Idea:** **Using AWS Amplify to Rapidly Prototype and Deploy a Full-Stack Mobile Application**
    *   **Description:** A project where students use the **AWS Amplify** framework to connect a simple mobile app to a cloud backend, implementing features like user authentication (Amazon Cognito) and data storage (Amazon DynamoDB).
    *   **Why it fits:** Shows students how high-level frameworks can accelerate development and leverages the mobile focus often seen in junior papers.

### Cloud Security & Management

*   **Topic Idea:** **Implementing Role-Based Access Control (RBAC) in AWS: A Security-Focused Student Project**
    *   **Description:** This paper would focus on security best practices. Students would set up an AWS organization and use **IAM (Identity and Access Management)** roles and policies to enforce the principle of least privilege for different "developer" and "admin" personas within a project.
    *   **Why it fits:** Directly tackles the "Security" evergreen theme but applies it to the cloud-native context, a critical and often overlooked area in student projects.

These topics are designed to be achievable within the scope of a student project, directly leverage the safe and accessible **AWS Learner Lab** environment, and would produce papers that are both educational for the student and novel for the MIPRO Junior conference.
