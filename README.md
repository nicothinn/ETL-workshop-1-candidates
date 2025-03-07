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
