# AWS Python Job Processing Proof of Concept

## Overview
This project is a simple Python proof of concept that simulates
a job-based, event-driven compute workload.

The goal is to demonstrate how a task is:
- received
- processed
- output generated
- and exited cleanly

This directly maps to AWS services such as:
API Gateway → SQS → ECS / EC2 / Batch → S3

## Workflow
1. A job ID is generated
2. Input data is processed (simulated heavy work)
3. Output is written to a file
4. Process exits successfully

## AWS Mapping
- Job ID → SQS Message ID
- Processing → ECS / EC2 task
- Output file → S3 object
- Script exit → Auto-termination of compute
