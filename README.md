# **Candidates Hiring Analysis**

## Introduction

This project aims to analyze a dataset of candidates who have applied for various positions at a company. The dataset contains detailed information about each candidate, including their name, email, country, application date, years of experience, seniority level, technology specialization, technical test scores, interview scores, and more.

The analysis focuses on identifying patterns and trends in the data to answer key questions such as:
   - What are the most in-demand technologies among hired candidates?
   - How has the number of hires changed over the years?
   - What is the distribution of hires by seniority level (Junior, Mid, Senior)?
   - How have hires evolved in specific countries (USA, Brazil, Colombia, and Ecuador) over time?


## Dataset

The dataset contains **50,000 rows** and the following columns:

- **First Name**: Candidate's first name.
- **Last Name**: Candidate's last name.
- **Email**: Candidate's email address.
- **Country**: Candidate's country of origin.
- **Application Date**: Date the candidate applied.
- **YOE (Years of Experience)**: Candidate's years of experience.
- **Seniority**: Candidate's seniority level (Junior, Mid, Senior).
- **Technology**: Technology in which the candidate specializes.
- **Code Challenge Score**: Score obtained in the technical test.
- **Technical Interview Score**: Score obtained in the technical interview.

### Hiring Criteria
A candidate is considered **hired** if they meet the following conditions:
- `Code Challenge Score >= 7`
- `Technical Interview Score >= 7`

## Exploratory Data Analysis (EDA)

### Tools Used
- **Python**: For data processing and analysis.
- **Polars**: A fast and efficient data manipulation library.
- **Tableu**: For creating interactive visualizations.
- **Matplotlib**: For creating static visualizations.
- **Seaborn**: For creating informative and attractive statistical graphics.
- **Pandas**: For data manipulation and analysis.
- **psycopg2**: For conecting the transformed data in postgres.
- **potsgreSQL**: As the database chosen. 

- **Jupyter Notebook**: For executing and documenting the code.

## Final Objective

The primary goal of this project is to perform data analysis and manipulations on a dataset of candidate applications to derive meaningful insights. This exercise is designed to simulate real-world data engineering tasks, providing hands-on experience in data processing, transformation, and visualization.

As part of this project, you will:
1. **Clean and Prepare the Data**: Handle missing values, convert data types, and ensure the dataset is ready for analysis.
2. **Perform Exploratory Data Analysis (EDA)**: Identify trends, patterns, and anomalies in the data.
3. **Apply Business Logic**: Filter and transform the data based on specific criteria (e.g., identifying hired candidates).
4. **Create Visualizations**: Generate charts and graphs to communicate insights effectively.


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

# 1. ETL Pipeline Explained Execution

Execute the notebooks and scripts step by step:

1. **Exploratory Data Analysis (EDA):**  
   Run: `notebooks/eda.ipynb`

2. **Database Connection and Data Extraction:**  
   Run: `notebooks/database_connection.ipynb`

3. **Transformations and Data Cleaning:**  
   Run: `ETL_Pipeline/transformations.py`

4. **Load Process:**  
   Run: `ETL_Pipeline/load_data.py`

## 2. Candidate Hiring Analysis

### 2.1 Introduction

This project analyzes a dataset of candidates applying for various positions. The dataset includes details such as **name, country, experience, seniority level, technology specialization, and interview scores**.

### 2.2 Key Questions

- What are the most in-demand technologies?
- How have hiring trends evolved over time?
- What is the distribution of seniority levels (Junior, Mid, Senior)?
- How have hires varied in specific countries (USA, Brazil, Colombia, Ecuador)?

## 3. Database Connection

- The data is stored in **PostgreSQL** using `psycopg2`.
- The `candidates` table contains the relevant data, imported from `hired_candidates.csv` to facilitate queries and visualizations.

## 4. Summary of Exploratory Data Analysis (EDA)

During the EDA, the following steps were performed:

1. **Variable Analysis:**  
   - **Numerical Variables:**  
     Distribution, central tendencies, and variability of fields such as Years of Experience, Code Challenge Score, and Technical Interview Score were analyzed.  
   - **Categorical Variables:**  
     Variables such as Seniority, Technology, and Country were evaluated by counting occurrences and identifying dominant categories.  
   - **Date Fields:**  
     Dates were reviewed to identify trends in application submissions over time.

2. **Insight Generation:**  
   - Insights regarding candidate demographics, performance metrics, and application trends were obtained.  
   - It was observed that most candidates have between 8 and 23 years of experience, and the score distributions are relatively uniform.  
   - The data highlighted the most popular technologies and significant geographic diversity.

3. **Data Filtering:**  
   - Filters were applied to include only candidates meeting the hiring criteria (scores ≥ 7 on both tests).  
   - This subset is used to populate the database and build dashboards.

4. **Data Quality Assurance:**  
   - Data integrity and quality were verified to ensure effective analysis and visualization.
     
# 5. Instructions for Use

## 5.1 Windows Setup

### 5.1.1 Create a Virtual Environment

Run the following commands to create and activate a virtual environment:
```plaintext
python -m venv venv
venv\Scripts\activate
```
### 5.1.2 Install Dependencies

Install the required dependencies:

```plaintext
pip install -r requirements.txt
```
### 5.1.3 Configure Environment Variables

Create a `.env` file in the root directory and add the following:
```sql
DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name

   ```
### 5.1.4 Run Notebooks

- **EDA and Data Extraction:** `notebooks/eda.ipynb`  
- **Database Connection:** `notebooks/database_connection.ipynb`  
- **Load Process:** `notebooks/data_loading_py`

# 6. Step-by-Step Guide: Creating Dashboards with Tableau (Connected to PostgreSQL)

This section explains how to create interactive dashboards using Tableau connected to PostgreSQL.

## 6.1 Table of Contents

1. Prerequisites  
2. PostgreSQL Setup  
3. JDBC Driver and Java Download  
4. Connecting Tableau to PostgreSQL  
5. Creating Dashboards in Tableau  
6. Sample Dashboards  
7. Conclusion

## 6.2 Prerequisites

Before you begin, ensure you have:
- PostgreSQL installed and running.
- A dataset loaded into PostgreSQL (e.g., `hired_candidates.csv`).
- Tableau Desktop installed.
- Basic knowledge of SQL and Tableau.

## 6.3 PostgreSQL Setup

**PostgreSQL Installation:**  
Download and install PostgreSQL from the [official website](https://www.postgresql.org/).

**Database Creation:**  
Open your PostgreSQL client and run:

CREATE DATABASE hiring_analysis;

## 6.4 JDBC Driver and Java Download

**Download the JDBC Driver:**  
Visit the [download page](https://jdbc.postgresql.org/download/) to obtain the appropriate driver.  
*Note:* Make sure the driver is compatible with your Java version.

**Verify Java Installation:**  
If Java is installed, check the version by running:

## 6.5 Connecting Tableau to PostgreSQL

1. Open Tableau Desktop.  
2. Under **Connect Server**, select **PostgreSQL**.  
3. Enter the server details:
   - **Server:** `your_database_host`
   - **Database:** `hiring_analysis`
   - **Authentication:** Enter your PostgreSQL username and password.
4. Click **Connect** to establish the connection.

## 6.6 Creating Dashboards in Tableau

Use Tableau tools to build the following dashboards:

- **Hires by Technology (Pie Chart):**  
  Visualize the proportion of hires by technology.
- **Hires by Year (Horizontal Bar Chart):**  
  Display the number of hires per year.
- **Hires by Seniority (Bar Chart):**  
  Show the distribution of hires by seniority level.
- **Hires by Country Over the Years (Multiline Chart):**  
  Analyze the hiring trends for countries such as USA, Brazil, Colombia, and Ecuador.


## 6.7 Sample Dashboards

- **Dashboard 1:** Summary of hiring metrics (total candidates, average scores, geographic distribution).
- **Dashboard 2:** Detailed analysis of candidate performance by technology and seniority.
- **Dashboard 3:** Time series analysis of application submissions and hiring trends.




