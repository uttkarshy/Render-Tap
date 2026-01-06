# AWS Job-Based Compute – Python Proof of Concept

## Overview
This repository contains a Python proof of concept that simulates a
job-based, event-driven compute workload aligned with AWS best practices.

The POC demonstrates how a short-lived compute task:
- receives a job
- performs processing
- generates output
- exits cleanly

This pattern is suitable for workloads such as rendering, automation,
and batch data processing.

---

## Architecture Mapping (AWS)

| Component | AWS Service |
|---------|-------------|
| Job submission | API Gateway |
| Job queue | Amazon SQS |
| Compute execution | Amazon ECS / EC2 / AWS Batch |
| Output storage | Amazon S3 |
| Monitoring & logs | Amazon CloudWatch |

---

## Workflow
1. A unique job ID is generated
2. Input data is received
3. Processing is simulated
4. Output is written to a file
5. Process terminates automatically

---

## Design Principles
- Stateless execution
- Short-lived compute
- Cost-optimized scaling
- Secure, role-based access
- No persistent infrastructure

---

## How to Run Locally

```bash
python job_processor.py
