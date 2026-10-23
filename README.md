SRID Azure Data Platform

An end-to-end Azure data engineering platform demonstrating infrastructure as code, cloud data-lake architecture, medallion transformations, data quality controls, dimensional modelling, Microsoft Fabric semantic modelling and interactive Power BI analytics.

Data: This project uses synthetically generated business data designed to simulate a South African industrial distribution company.

Project Overview

The SRID Azure Data Platform demonstrates how operational data can be ingested, governed, transformed and exposed as business-ready analytical datasets.

The platform follows this flow:

Source Data
    │
    ▼
ADLS Gen2 - Landing
    │
    ▼
Bronze Layer
    │
    ▼
Silver Layer
    │
    ├── Data Quality Validation
    │
    └── Quarantine
    │
    ▼
Gold Layer
    │
    ▼
Microsoft Fabric / OneLake
    │
    ▼
Semantic Model
    │
    ▼
Power BI Analytics

The solution combines Azure infrastructure, Databricks/Delta processing and Microsoft Fabric reporting into a single portfolio project.

Technology Stack

Area

Technology

Cloud

Microsoft Azure

Infrastructure as Code

Terraform

Storage

Azure Data Lake Storage Gen2

Orchestration

Azure Data Factory

Data Processing

Azure Databricks

Languages

Python, PySpark, SQL, DAX

Data Format

Delta Lake

Secrets

Azure Key Vault

Identity & Access

Microsoft Entra ID / Azure RBAC

Monitoring

Azure Log Analytics

Analytics Platform

Microsoft Fabric

Semantic Modelling

Power BI Semantic Model

Reporting

Power BI

Source Control

Git / GitHub

Azure Infrastructure

The development environment is provisioned using Terraform.

Key resources include:

Resource

Development Resource

Resource Group

rg-srid-data-dev-zan

ADLS Gen2 Storage

stsriddatadevzan01

Azure Data Factory

adf-srid-data-dev-zan

Azure Databricks

dbw-srid-data-dev-zan

Databricks Access Connector

ac-srid-dbw-dev-zan

Azure Key Vault

kv-srid-data-dev-zan

Log Analytics Workspace

law-srid-data-dev-zan

The storage account uses separate containers for:

landing
bronze
silver
gold
quarantine

This separation provides clear lifecycle boundaries across ingestion, processing and analytics.

Source Data

The source layer represents a South African industrial distribution business.

Ten business datasets were generated:

Dataset

Business Domain

customers

Customer master data

products

Product master data

suppliers

Supplier master data

sales_orders

Sales order headers

sales_order_lines

Sales transaction detail

invoices

Customer invoicing

payments

Customer payments

inventory_snapshots

Inventory balances

purchase_orders

Procurement activity

shipment_events

Distribution and logistics events

Source files are uploaded to the ADLS Gen2 landing container and retained as the original source representation.

Detailed dataset definitions and volumes are documented in:

docs/dataset_inventory.md

Medallion Architecture

Landing

The landing layer preserves incoming source files in their original form.

No business transformations are performed at this stage.

Bronze

Bronze provides a raw persisted representation of source datasets for traceability, replayability and downstream processing.

Silver

Silver applies cleansing, standardisation, type handling and validation.

Data-quality checks include:

Primary-key validation

Null checks

Data-type validation

Numerical business rules

Transaction calculation checks

Referential integrity checks

Records that fail validation rules can be isolated through the quarantine layer rather than silently entering trusted analytical datasets.

Gold

Gold contains business-ready datasets designed for analytics, dimensional modelling and reporting.

The Gold layer supports:

Sales analytics

Customer analytics

Finance and receivables

Inventory reporting

Procurement reporting

Supplier analysis

Microsoft Fabric Integration

Gold datasets are exposed in Microsoft Fabric through OneLake shortcuts, allowing Fabric to work with the analytical data without unnecessarily duplicating the underlying Gold datasets.

The Fabric Lakehouse provides the analytical surface used by the semantic model and Power BI report.

The model contains the following primary analytical tables:

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

The model follows a star-schema pattern with active, single-direction relationships from dimensions to fact tables.

Date Dimension Design

A dedicated date dimension is used across the reporting model.

The date dimension supports common reporting attributes including:

Date

Year

Quarter

Month number

Month name

Year-month

Week number

Day

Day name

The date dimension was registered through the Fabric SQL analytics endpoint and brought into the semantic model as dim_date_import.

It is related to the fact tables through:

fact_sales[order_date]

fact_inventory[snapshot_date]

fact_finance[invoice_date]

fact_procurement[order_date]

Semantic Model Measures

Reusable DAX measures provide a governed business metrics layer for the Power BI report.

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

These measures are reused across report pages rather than recreating calculation logic inside individual visuals.

Power BI Analytics

The final report, SRID Executive Analytics, contains four interactive analytical pages.

Executive Overview

The Executive Overview provides a management-level view across sales, finance, inventory and procurement.

Key KPIs include:

Total Sales

Sales Orders

Average Order Value

Total Invoiced

Outstanding Receivables

Inventory Value

Procurement Spend

The page also includes:

Monthly Sales Trend

Sales by Product Category

Sales by Province

Outstanding Receivables by Status

Month and province slicers



Sales & Customers

The Sales & Customers page provides deeper analysis of customer and sales performance.

Key visuals include:

Top 10 Customers by Sales

Sales by Order Channel

Sales by Industry

Monthly Sales Trend

Month slicer

Province slicer



Inventory & Procurement

The Inventory & Procurement page provides visibility into stock position, supplier activity and procurement trends.

Key visuals include:

Inventory Value by Product Category

Stock On Hand by Product Category

Procurement Spend by Supplier

Purchase Orders by Supplier

Inventory Value by Location

Procurement Spend Trend

Month slicer

Product-category slicer



Finance & Receivables

The Finance & Receivables page provides an accounts-receivable and invoicing view.

Key visuals include:

Total Invoiced

Total Paid

Outstanding Receivables

Invoice Count

Outstanding Receivables by Status

Invoiced vs Paid by Month

Top 10 Customers by Outstanding Receivables

Invoice Count by Status

Month slicer

Province slicer



Example Platform Metrics

The analytical model currently produces approximately:

KPI

Value

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

Security and Governance

Security controls are designed around Azure-native identity and access management.

The implementation includes:

Microsoft Entra-based authentication

Azure RBAC

Azure Key Vault for secrets

Controlled storage permissions

Databricks access connector

Managed access to analytical resources

Security design notes are documented in:

docs/security.md

Monitoring and Operations

Azure Log Analytics is included in the platform architecture to support operational visibility and troubleshooting.

The platform separates infrastructure, ingestion, transformation, storage and reporting concerns so that failures can be investigated at the appropriate layer rather than treating the pipeline as a single black box.

Repository Structure

srid-azure-data-platform/
│
├── docs/
│   ├── images/
│   │   ├── Exec Overview.png
│   │   ├── Sales & Cust.png
│   │   ├── Inv & Proc.png
│   │   └── Finance & Recv.png
│   │
│   ├── architecture.md
│   ├── dataset_inventory.md
│   └── security.md
│
├── scripts/
│   └── generate_srid_data.py
│
├── terraform/
│   └── environments/
│       └── dev/
│           └── main.tf
│
├── .gitignore
├── LICENSE
└── README.md

Architecture Documentation

Detailed architecture decisions are documented separately:

docs/architecture.md

The documentation covers platform components, data flow and the main engineering design decisions used across the Azure environment.

Engineering Principles

The project was built around production-style engineering principles:

Infrastructure should be repeatable and version controlled.

Source data should remain immutable after landing.

Raw, cleansed and analytical datasets should remain logically separated.

Invalid records should be quarantined rather than silently discarded.

Business logic should be applied before data reaches reporting.

Shared business metrics should be defined once in the semantic layer.

Analytical models should use clear star-schema relationships.

Security and monitoring should be designed into the platform.

Reporting should expose governed measures rather than duplicate calculation logic.

What This Project Demonstrates

This project demonstrates practical experience across the full data-platform lifecycle:

Terraform-based Azure provisioning

ADLS Gen2 architecture

Python-based data generation

Azure Data Factory

Azure Databricks

PySpark

Delta Lake

Data-quality engineering

Medallion architecture

Azure security and RBAC

Microsoft Fabric

OneLake

SQL analytics

Dimensional modelling

DAX

Power BI dashboard development

Git and GitHub

The project is designed as an end-to-end data engineering portfolio solution rather than an isolated notebook or standalone dashboard.

Author

Takudzwa Mhandire

Azure Data Engineering | Microsoft Fabric | Databricks | Terraform | Power BI
