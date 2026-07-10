🏡 Airbnb Data Warehouse Project

This project demonstrates an end-to-end Data Warehouse solution using the Medallion Architecture (Bronze → Silver → Gold) on the Airbnb Prices in European Citiesdataset.
The objective of this project was to simulate a real-world business workflow, starting from raw CSV files and ending with an interactive Power BI dashboard for business analysis and decision-making.
Project Workflow

🥉 Bronze Layer – Raw Data Ingestion

Loaded all raw Airbnb CSV files from multiple European cities.
Verified that all datasets shared a common schema.
Standardized data types across files.
Preserved the raw data without modifications to ensure data traceability.
🥈 Silver Layer – Data Cleaning & Feature Engineering

Performed data quality assessment for each dataset individually.
Removed duplicate records.
Validated data types and checked for invalid values.
Analyzed missing values and confirmed data completeness.
Explored numerical distributions and detected potential outliers.
Added several engineered features to improve business analysis, including:
Country
Weekend Indicator
Price per Person
Accommodation Size
Host Type
Distance Category
Metro Distance Category
Guest Satisfaction Category
Cleanliness Category
Combined all cleaned datasets into a single master dataset.
🥇 Gold Layer – Data Warehouse Design

Imported the master dataset into SQL Server.
Designed and implemented a Star Schema.
Built dimension tables including:
DimCity
DimProperty
DimHost
DimStayType
DimLocation
Created the FactListings table with appropriate primary and foreign key relationships.
Populated all dimension and fact tables using SQL joins.
📊 Power BI Dashboard

Connected Power BI to SQL Server.
Built a relational data model based on the Star Schema.
Created interactive dashboards with KPIs, filters, and business insights.
Developed multiple analytical pages, including:
Executive Dashboard
City Analysis
Property Analysis
Location Analysis
Host & Customer Analysis
Technologies Used

Python
Pandas
SQL Server
Power BI
Git & GitHub
Jupyter Notebook
This project demonstrates the complete lifecycle of building a modern Data Warehouse, from raw data ingestion to interactive business intelligence dashboards, following industry-standard Medallion Architecture principles.