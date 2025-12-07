# pyspark-etl-pipeline
End-to-end PySpark ETL pipeline using DataFrames for cleaning, enrichment, analytics, and export. Includes schema definition, joins, aggregations, and final dataset extraction.


PySpark ETL Pipeline

An end-to-end PySpark data engineering project showcasing data ingestion, cleaning, enrichment, transformations, aggregations, and final dataset extraction.

This project demonstrates essential Data Engineering skills using Apache Spark and PySpark DataFrames.

🧱 Project Architecture

Input → Clean → Enrich → Transform → Aggregate → Export

raw CSVs
    ↓
schema definition (StructType)
    ↓
data cleaning & type casting
    ↓
data enrichment (JOIN with customers)
    ↓
transformations (new columns, normalization)
    ↓
analytics aggregations (SUM, AVG, COUNT)
    ↓
final dataset export (CSV)
