# FinOps Metric Dictionary

## Overview

This document defines the key metrics used across FinOps dashboards and reporting.

The goal is to ensure **consistency, clarity, and trust** in how cloud cost data is interpreted and used for decision-making.

---

## Principles

- Every metric must have a clear definition
- Metrics must be reproducible and validated
- Stakeholders must understand how metrics are calculated
- Definitions must remain consistent across dashboards and reports

---

## Core Metrics

### 1. Total Cloud Spend

**Definition:**  
Total cost incurred across all cloud providers within a defined time period.

**Use Case:**  
- Executive reporting
- Budget tracking
- Trend analysis

---

### 2. Cost by Service

**Definition:**  
Breakdown of total spend by cloud service (e.g., EC2, S3, RDS, Kubernetes).

**Use Case:**  
- Identify major cost drivers
- Prioritize optimization efforts

---

### 3. Cost by Team / Application

**Definition:**  
Cloud cost allocated to teams, products, or applications based on tagging or allocation rules.

**Use Case:**  
- Accountability and ownership
- Showback and chargeback models

---

### 4. Cost Variance

**Definition:**  
Difference between actual spend and expected spend (budget or forecast).

**Formula:**  
Actual Cost – Expected Cost

**Use Case:**  
- Detect anomalies
- Support variance investigations
- Drive corrective actions

---

### 5. Cost per Unit (Unit Economics)

**Definition:**  
Cost associated with a business or technical unit (e.g., cost per request, user, transaction).

**Use Case:**  
- Connect infrastructure cost to business value
- Support pricing and margin analysis

---

### 6. Time-to-Detect

**Definition:**  
Time taken to identify a cost anomaly or variance from when it occurs.

**Use Case:**  
- Measure monitoring effectiveness
- Improve detection systems

---

### 7. Time-to-Act

**Definition:**  
Time taken from detection of a cost issue to initiation of corrective action.

**Use Case:**  
- Measure operational efficiency
- Improve response workflows

---

### 8. Savings Realized

**Definition:**  
Measured reduction in cloud spend resulting from optimization actions.

**Use Case:**  
- Track FinOps impact
- Support ROI reporting

---

### 9. Commitment Coverage

**Definition:**  
Percentage of eligible cloud usage covered by Savings Plans or Reserved Instances.

**Use Case:**  
- Optimize pricing efficiency
- Identify underutilized commitment opportunities

---

### 10. Resource Utilization

**Definition:**  
Actual usage of provisioned resources (e.g., CPU, memory) relative to capacity.

**Use Case:**  
- Identify overprovisioning
- Support rightsizing decisions

---

## Data Quality Considerations

- Ensure tagging completeness and accuracy
- Validate allocation logic regularly
- Reconcile data with billing sources (AWS CUR, Azure Cost Management, GCP Billing)
- Monitor for anomalies in data pipelines

---

## Governance

- Metric definitions are version-controlled
- Changes require review and stakeholder alignment
- All dashboards must reference this dictionary
