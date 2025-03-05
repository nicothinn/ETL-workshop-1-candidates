# Step-by-Step Guide: Creating Dashboards with Power BI and Tableau (Connected to PostgreSQL)

This guide provides a detailed walkthrough of how to create interactive dashboards using **Power BI** and **Tableau**, connecting to a **PostgreSQL** database. It includes step-by-step instructions, code snippets, and screenshots to help you replicate the process.

---

## **Table of Contents**
1. [Prerequisites](#prerequisites)
2. [Setting Up PostgreSQL](#setting-up-postgresql)
3. [Connecting Power BI to PostgreSQL](#connecting-power-bi-to-postgresql)
4. [Connecting Tableau to PostgreSQL](#connecting-tableau-to-postgresql)
5. [Creating Dashboards in Tableau](#creating-dashboards-in-tableau)
6. [Sample Dashboards](#sample-dashboards)
7. [Conclusion](#conclusion)

---

## **Prerequisites**
Before starting, ensure you have the following:
- **PostgreSQL** installed and running.
- A dataset loaded into PostgreSQL (e.g., `hired_candidates.csv`).
- **Power BI Desktop** installed.
- **Tableau Desktop** installed.
- Basic knowledge of SQL, Power BI, and Tableau.

---

## **Setting Up PostgreSQL**
1. **Install PostgreSQL**: Download and install PostgreSQL from the [official website](https://www.postgresql.org/download/).
2. **Create a Database**:
   ```sql
   CREATE DATABASE hiring_analysis;

   