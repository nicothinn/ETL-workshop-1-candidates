# ETL Pipeline Project

## Project Overview

This project is an **ETL (Extract, Transform, Load) Pipeline** designed for data processing and visualization. The pipeline is built using **Jupyter Notebooks**, connects to a **PostgreSQL** database, and generates dashboards using **Power BI** and **Tableau**.

## Project Structure

```plaintext
ETL_Pipeline/
│── .git/                 # Git repository metadata
│── data/                 # Raw and processed data
│── ETL_Pipeline/         # Main ETL pipeline scripts
│── looker/               # Visualization and reporting scripts
│── notebooks/            # Jupyter notebooks for analysis and development
│── venv/                 # Virtual environment for dependency management
│── .env                  # Environment variables (database credentials, etc.)
│── .gitignore            # Files and directories to ignore in Git
```

---

## Installation & Setup

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/ETL_Pipeline.git
cd ETL_Pipeline
```

### 2. Set up the virtual environment

#### On macOS/Linux:

```sh
python -m venv venv
source venv/bin/activate
```

#### On Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add:

```ini
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
```

---

## Running the ETL Pipeline

Execute the notebooks step by step:

1. **Exploratory Data Analysis (EDA):** `notebooks/eda.ipynb`
2. **Database Connection & Data Extraction:** `notebooks/database_connection.ipynb`
3. **Transformations & Data Cleaning:** `ETL_Pipeline/transformations.py`
4. **Load Process:** `ETL_Pipeline/load_data.py`

---

## Tools Used

- **Python**: For data processing and analysis.
- **Polars**: A fast and efficient data manipulation library.
- **Tableau**: For creating interactive visualizations.
- **Matplotlib**: For creating static visualizations.
- **Seaborn**: For creating informative and attractive statistical graphics.
- **Pandas**: For data manipulation and analysis.
- **psycopg2**: For connecting the transformed data in PostgreSQL.
- **PostgreSQL**: As the chosen database.

---

## Candidates Hiring Analysis

### Introduction

This project analyzes a dataset of candidates applying for various positions. The dataset contains details like **name, country, experience, seniority level, technology specialization, and interview scores**.

### Key Questions:

- What are the most in-demand technologies?
- How have hires evolved over time?
- What is the seniority distribution (Junior, Mid, Senior)?
- How have hires changed across different countries (USA, Brazil, Colombia, Ecuador)?

### Dataset Overview

- **50,000 rows** with candidate information.
- **Fields include:**
  - `name`, `email`, `country`, `application_date`, `experience`, `seniority`, `technology`, and `interview scores`.
- **Hiring Criteria:** Candidates must have:
  - Code Challenge Score **≥ 7**
  - Technical Interview Score **≥ 7**

---

## Database Connection

Data is stored in **PostgreSQL** using `psycopg2`. The `candidates` table contains relevant information, imported from `hired_candidates.csv` for efficient querying and visualization.

# EDA Summary

During the Exploratory Data Analysis (EDA), the following key steps were performed:

- **Variable Analysis:**  
  Each variable was examined in detail. Numerical variables (e.g., Years of Experience, Code Challenge Score, Technical Interview Score) were analyzed for distribution, central tendencies, and variability. Categorical variables (e.g., Seniority, Technology, Country) were evaluated by counting occurrences and identifying dominant categories. Date fields were reviewed to reveal trends in application submissions over time.

- **Insight Generation:**  
  The analysis provided insights into candidate demographics, performance metrics, and application trends. It revealed that most candidates have between 8 and 23 years of experience, and that test score distributions are relatively even. Categorical data highlighted popular technologies and a diverse geographical representation.

- **Data Filtering:**  
  Based on the hiring criteria (Code Challenge Score and Technical Interview Score both ≥ 7), the dataset was filtered to include only the candidates who met these thresholds. This transformed dataset is used to populate the database for building dashboards.

- **Data Quality and Relevance:**  
  Ensured that the data was complete and of high quality, focusing on the most relevant subset for visualization and decision-making.


# Windows Setup Instructions

## Create Virtual Environment
Run the following commands to create and activate a virtual environment on Windows:

    python -m venv venv
    venv\Scripts\activate

## Install Dependencies
Install the required dependencies by running:

    pip install -r requirements.txt

## Set Up Environment Variables
Create a `.env` file in the root directory and add the following:

    DB_HOST=your_database_host
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_NAME=your_database_name


## Execute the notebooks step by step:
- **Exploratory Data Analysis & Data Extraction (EDA):** `notebooks/eda.ipynb`
- **Database Connection:** `notebooks/database_connection.ipynb`
- **Load Process:** `notebooks/data_loading_py`

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

  

