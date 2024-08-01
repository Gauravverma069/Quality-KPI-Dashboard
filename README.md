# Quality KPI Dashboard Project

This project involves creating a Quality KPI Dashboard using Power BI. The workflow includes collecting data about defects and production output through a Streamlit application, storing the data in a MySQL database, and then visualizing the data in a Power BI dashboard.

## Table of Contents

- [Overview](#overview)
- [Components](#components)
  - [Streamlit Application](#streamlit-application)
  - [MySQL Database](#mysql-database)
  - [Power BI Dashboard](#power-bi-dashboard)
- [Setup and Installation](#setup-and-installation)


## Overview

The goal of this project is to provide a comprehensive view of quality key performance indicators (KPIs) by integrating data collection, storage, and visualization processes.

## Components

### Streamlit Application

The Streamlit app serves as the user interface for inputting data related to production output and defects. It captures the following information:
- Date
- Reporting Area
- Component
- Category
- Sub-Category
- Defect
- Part Number
- Quantity
  

#### **Production Output to MySQL Server**
https://github.com/user-attachments/assets/69605d3b-c9c0-49c4-8d8d-3acbcb83e8c8

#### **Error incase of Multiple Entry on Same Date**
https://github.com/user-attachments/assets/b054c2a5-abde-470f-b424-f705d985dcfe

#### **Defect Logging**
https://github.com/user-attachments/assets/3f34ea8a-efd4-4a66-a98b-7644266066f5


#### **Data Append to MySQL Server**
https://github.com/user-attachments/assets/6957cad9-5fb2-40b3-99d3-3e76f522f29c


The data is then sent to a MySQL database for storage.

### MySQL Database

The MySQL database stores the data collected from the Streamlit application. The data schema includes:
- `id`: Primary key
- `date`: Date of production
- `reporting_area`: Area where the report is generated
- `component`: Component of the product
- `category`: Category of the defect
- `sub_category`: Sub-category of the defect
- `defect`: Description of the defect
- `part_no`: Part number
- `quantity`: Quantity of defective parts

#### **Data in MySQL**
https://github.com/user-attachments/assets/cac91043-b94f-4711-83ea-eb277d743070

### Power BI Dashboard

The Power BI dashboard is used to visualize the data stored in the MySQL database. It provides insights into:
- Production trends
- Defect trends
- Correlation between production output and defects
- Overall quality performance

## Setup and Installation

### Prerequisites

- Python 3.x
- Streamlit
- MySQL
- Power BI

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/quality-kpi-dashboard.git
   cd quality-kpi-dashboard
   
2. **Set up the MySQL database:**

- Create a new database in MySQL.
- Run the provided SQL script to set up the necessary tables.
  
3. **Install Python dependencies:**
  
-  Copy code
-  pip install -r requirements.txt

4. **Run the Streamlit application:**
-  Copy code
-  streamlit run app.py

5. **Set up the Power BI dashboard:**

- Connect Power BI to your MySQL database.
- Import the necessary data tables.
- Create visualizations based on your requirements.
