# 🚀 PySpark ETL Pipeline

An end-to-end **PySpark data engineering project** showcasing data ingestion, schema enforcement, cleaning, enrichment, transformations, aggregations, and final dataset extraction.

This project demonstrates essential **Data Engineering skills** using Apache Spark and PySpark DataFrames.

---

## 📁 Project Structure

pyspark-etl-pipeline/
│
├── datasets/
│ ├── customers.csv
│ ├── transactions.csv
│
├── output/
│ ├── data_agg.csv
│
├── project_1.ipynb
├── environ_setup.py
├── README.md



---

## 🧱 ETL Workflow

The project follows a complete **Extract → Transform → Load** workflow:

1. **Extract**
   - Load raw CSV datasets using PySpark
   - Apply explicit schema definitions with `StructType`

2. **Transform**
   - Clean and cast data types
   - Convert timestamps → dates → year/month columns
   - Normalize text fields (region, payment_method)
   - Enrich data using a left join with customer info
   - Create business logic columns (is_high_value)
   - Perform groupBy aggregations (SUM, AVG, COUNT)

3. **Load**
   - Export final aggregated dataset to CSV (`output/data_agg.csv`)

---

## 🔧 Technologies Used

- **Python**
- **Apache Spark**
- **PySpark (DataFrame API)**
- **Jupyter Notebook / PyCharm**
- **Pandas (only for final CSV export)**

---

## 📊 Aggregation Metrics

The aggregated dataset groups transactions by:
region, year, month


With the following metrics:

- `total_amount`
- `avg_amount`
- `transaction_count`
- `high_value_count`

---

## 🧠 Key Data Engineering Concepts Demonstrated

✔ Explicit schema definition (StructType)  
✔ Data cleaning & type conversions  
✔ Extracting date components (year/month)  
✔ Data enrichment via left join  
✔ Business logic column creation  
✔ Aggregations using groupBy  
✔ Exporting final dataset as CSV  
✔ Clean, modular pipeline design  

---

## ▶️ How to Run

1. Install required dependencies:
   ```bash
   pip install pyspark pandas

Open:
project_1.ipynb
Run all cells.
The final dataset will be saved as:

output/data_agg.csv
