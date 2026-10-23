

Terraform

Storage

ADLS Gen2

Orchestration

Azure Data Factory

Processing

Azure Databricks, PySpark

Data format

Delta Lake

Security

Entra ID, RBAC, Key Vault

Monitoring

Log Analytics

Analytics

Microsoft Fabric, OneLake

Semantic model

Power BI

Reporting

Power BI

Source control

GitHub

Data Platform

The platform uses separate ADLS Gen2 containers for:

landing
bronze
silver
gold
quarantine

The source datasets cover:

customers

products

suppliers

sales orders

sales order lines

invoices

payments

inventory snapshots

purchase orders

shipment events

The source-data generator is available at:

scripts/generate_srid_data.py

Dataset details are documented in:

docs/dataset_inventory.md

Data Processing

The processing design follows a medallion pattern.

Bronze preserves the raw source representation.

Silver performs cleansing, type handling and data-quality validation, including primary-key checks, null validation, transaction rules and referential-integrity checks.

Records that fail validation can be separated into the quarantine layer.

Gold provides business-ready models for sales, finance, inventory and procurement reporting.

Microsoft Fabric and Semantic Model

Gold datasets are exposed to Microsoft Fabric through OneLake.

The reporting model uses a star-schema design with the following core tables:

Dimensions

Facts

dim_customer

fact_sales

dim_product

fact_finance

dim_supplier

fact_inventory

dim_date_import

fact_procurement

The date dimension is related to the fact tables through sales order date, invoice date, inventory snapshot date and procurement order date.

Reusable DAX measures include:

Sales

Total Sales

Sales Orders

Units Sold

Average Order Value

Finance

Total Invoiced

Total Paid

Outstanding Receivables

Invoice Count

Inventory

Inventory Value

Stock On Hand

Available Stock

Procurement

Procurement Spend

Purchase Orders

Quantity Ordered

Power BI Report

The final report contains four pages.

Executive Overview

Management-level view of sales, finance, inventory and procurement.



Sales & Customers

Customer performance, sales channels, industries and monthly sales trends.



Inventory & Procurement

Inventory position, supplier activity, purchasing and procurement trends.



Finance & Receivables

Invoicing, payments, outstanding receivables and customer exposure.



Example Metrics

Metric

Result

Total Sales

R7.40bn

Sales Orders

15K

Average Order Value

R497.82K

Total Invoiced

R7.98bn

Total Paid

R6.23bn

Outstanding Receivables

R1.74bn

Inventory Value

R62.51bn

Procurement Spend

R5.32bn

Security and Monitoring

The platform uses Azure-native security controls including Entra ID, RBAC, Key Vault and controlled storage access.

Azure Log Analytics provides the monitoring foundation for the environment.

More detail is available in:

docs/architecture.md

docs/security.md

docs/dataset_inventory.md

Repository Structure

srid-azure-data-platform/
├── docs/
│   ├── images/
│   ├── architecture.md
│   ├── dataset_inventory.md
│   └── security.md
├── scripts/
│   └── generate_srid_data.py
├── terraform/
│   └── environments/
│       └── dev/
│           └── main.tf
├── .gitignore
├── LICENSE
└── README.md

What This Project Demonstrates

Azure infrastructure provisioning with Terraform

ADLS Gen2 data-lake design

Medallion architecture

Databricks and PySpark processing

Delta Lake

Data-quality and quarantine patterns

Azure security and RBAC

Microsoft Fabric and OneLake

Dimensional modelling

Power BI semantic modelling

DAX measures

Executive reporting and business analytics

Author

Takudzwa Mhandire

Azure Data Engineering | Microsoft Fabric | Databricks | Terraform | Power BI
