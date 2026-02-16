# Salesforce-to-Azure Revenue Analytics Pipeline 🚀

## Project Overview
This project implements a professional **Medallion Architecture** to automate the ingestion and transformation of Salesforce CRM data. By bridging Salesforce with Azure Cloud infrastructure, the pipeline enables dynamic tracking of key revenue metrics like Net Revenue Retention (NRR) and sales velocity.



## 🏗️ Architecture
- **Bronze (Ingestion):** Raw Opportunity records extracted via Python (Simple-Salesforce) and stored as timestamped JSON in **Azure Blob Storage**.
- **Silver (Transformation):** Data cleaning, schema enforcement, and standardization handled via **Azure Data Factory** and **Python**.
- **Gold (Analytics):** Aggregated revenue datasets ready for visualization in **Power BI** to drive executive decision-making.

## 🛠️ Tech Stack
- **Source:** Salesforce CRM (REST API)
- **Languages:** Python (Pandas, Requests), SQL
- **Cloud:** Azure Blob Storage, Azure Data Factory
- **Security:** Managed via `.env` secrets and GitHub Actions environment variables.

## 📈 Business Impact
- **Automation:** Replaces manual CSV exports with a serverless cloud-native workflow.
- **Data Integrity:** Implements automated checks to ensure revenue records are cleaned and standardized before reaching stakeholders.
- **Scalability:** Built to handle thousands of global records while maintaining a low-cost footprint on Azure.

## 📂 Project Structure
- `/src`: Python ingestion scripts.
- `/config`: JSON schemas and API configurations.
- `requirements.txt`: Python dependency management.
- `.gitignore`: Ensures security of environment variables.

## 📖 Data Dictionary (Bronze Layer)
The ingestion engine currently captures the following key fields from the Salesforce `Opportunity` object:

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `Name` | String | The unique identifier for the sales deal. |
| `Amount` | Decimal | The projected revenue value used for **NRR** calculations. |
| `StageName` | Picklist | Current sales phase (e.g., Closed Won, Prospecting). |
| `CloseDate` | Date | Expected or actual date of revenue realization. |
| `Probability` | Percentage | The likelihood of the deal closing, used for weighted forecasting. |
