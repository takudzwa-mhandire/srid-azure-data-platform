🚀 SRID Azure Data Platform

End-to-End Azure Data Engineering & Analytics Platform

Terraform • ADLS Gen2 • Azure Data Factory • Databricks • Delta Lake • Microsoft Fabric • Power BI

<br>

An enterprise-style cloud data platform demonstrating infrastructure as code,
medallion architecture, data quality engineering, dimensional modelling,
semantic modelling and interactive business analytics.

</div>

Data: This project uses synthetically generated business data designed to simulate a South African industrial distribution company.

✨ Project Highlights

☁️ Azure infrastructure provisioned using Terraform

🗄️ Multi-layer ADLS Gen2 medallion architecture

⚙️ Data transformation using Databricks, PySpark and Delta Lake

✅ Data quality validation with a dedicated quarantine layer

🔐 Azure-native security using RBAC, Entra ID and Key Vault

📊 Business-ready Gold dimensional models

🔗 Integration with Microsoft Fabric and OneLake

🧠 Reusable Power BI semantic model and DAX measures

📈 Four-page interactive executive analytics report

📁 Source-controlled engineering artefacts in GitHub

🏗️ Architecture

flowchart LR

    A[Source Data] --> B[ADLS Gen2<br/>Landing]
    B --> C[Bronze Layer]
    C --> D[Silver Layer]
    D --> E{Data Quality}

    E -->|Valid| F[Gold Layer]
    E -->|Invalid| Q[Quarantine]

    F --> G[Microsoft Fabric<br/>OneLake]
    G --> H[Semantic Model]
    H --> I[Power BI<br/>Analytics]

Data Flow

Source → Landing → Bronze → Silver → Gold → Fabric → Semantic Model → Power BI

The platform separates raw ingestion, validated data and business-ready analytics into independent layers so each stage can be governed, monitored and maintained separately.

🧰 Technology Stack

<p>









</p>

Layer

Technology

☁️ Cloud

Microsoft Azure

🏗️ Infrastructure as Code

Terraform

🗄️ Data Lake

Azure Data Lake Storage Gen2

🔄 Orchestration

Azure Data Factory

⚙️ Processing

Azure Databricks

🧮 Languages

Python, PySpark, SQL, DAX

🧱 Data Format

Delta Lake

🔐 Secrets

Azure Key Vault

👤 Identity

Microsoft Entra ID / Azure RBAC

📋 Monitoring

Azure Log Analytics

🟦 Analytics

Microsoft Fabric / OneLake

🧠 Semantic Layer

Power BI Semantic Model

📊 Reporting

Power BI

🔧 Source Control

Git / GitHub

☁️ Azure Infrastructure

The development environment is provisioned using Terraform.

Core Resources

Azure Resource

Purpose

rg-srid-data-dev-zan

Development resource group

stsriddatadevzan01

ADLS Gen2 data lake

adf-srid-data-dev-zan

Data orchestration

dbw-srid-data-dev-zan

Databricks processing

ac-srid-dbw-dev-zan

Databricks access connector

kv-srid-data-dev-zan

Secrets management

law-srid-data-dev-zan

Centralised logging

Storage Containers

landing
├── Raw source files

bronze
├── Raw persisted datasets

silver
├── Cleansed and validated data

gold
├── Business-ready analytical data

quarantine
└── Records failing quality validation

📦 Source Data

The platform models the operations of a South African industrial distribution company.

Business Datasets

Dataset

Domain

customers

Customer master

products

Product master

suppliers

Supplier master

sales_orders

Sales headers

sales_order_lines

Sales transactions

invoices

Customer invoicing

payments

Customer payments

inventory_snapshots

Inventory

purchase_orders

Procurement

shipment_events

Logistics

The source-generation logic is version controlled in:

scripts/generate_srid_data.py

Detailed dataset structures and volumes are documented in:

docs/dataset_inventory.md

🥉🥈🥇 Medallion Architecture

🥉 Bronze — Raw

The Bronze layer preserves source records in their raw analytical representation.

It provides:

Traceability

Replayability

Historical source preservation

Separation between ingestion and transformation

🥈 Silver — Validated

The Silver layer standardises and validates raw data.

Quality Controls

Primary-key validation

Null checks

Data-type validation

Numerical business rules

Transaction calculation checks

Referential integrity checks

Records failing validation can be routed to the quarantine layer instead of entering trusted downstream datasets.

🥇 Gold — Business Ready

The Gold layer transforms validated records into analytical structures optimised for reporting.

Business domains include:

Sales

Customers

Finance

Receivables

Inventory

Procurement

Suppliers

🟦 Microsoft Fabric Integration

Gold datasets are exposed to Microsoft Fabric through OneLake shortcuts.

This allows the analytics layer to work with Gold data while avoiding unnecessary duplication of the underlying analytical datasets.

The Fabric environment provides the analytical surface used by the semantic model and Power BI report.

Analytical Model

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

The model follows a star-schema approach with active, single-direction relationships from dimensions to fact tables.

Relationship Pattern

dim_customer
      │
      ├──────────────▶ fact_sales
      │
      └──────────────▶ fact_finance


dim_product
      │
      ├──────────────▶ fact_sales
      ├──────────────▶ fact_inventory
      └──────────────▶ fact_procurement


dim_supplier
      │
      └──────────────▶ fact_procurement


dim_date_import
      │
      ├──────────────▶ fact_sales
      ├──────────────▶ fact_inventory
      ├──────────────▶ fact_finance
      └──────────────▶ fact_procurement

📅 Date Dimension

A dedicated date dimension supports consistent analysis across business domains.

It includes:

Date

Year

Quarter

Month number

Month name

Year-month

Week number

Day

Day name

dim_date_import is related to:

fact_sales[order_date]
fact_inventory[snapshot_date]
fact_finance[invoice_date]
fact_procurement[order_date]

This enables consistent filtering and trend analysis across the sales, finance, inventory and procurement domains.

🧠 Semantic Model

Reusable DAX measures provide a governed business-metrics layer.

💰 Sales

Total Sales

Sales Orders

Units Sold

Average Order Value

💳 Finance

Total Invoiced

Total Paid

Outstanding Receivables

Invoice Count

📦 Inventory

Inventory Value

Stock On Hand

Available Stock

🚚 Procurement

Procurement Spend

Purchase Orders

Quantity Ordered

The same measures are reused across all report pages instead of embedding calculation logic into individual visuals.

📊 SRID Executive Analytics

The Power BI reporting solution contains four interactive analytical views.

1️⃣ Executive Overview

A consolidated management view across sales, finance, inventory and procurement.

Key KPIs

R7.40bn Total Sales • 15K Sales Orders • R497.82K AOV • R7.98bn Invoiced • R1.74bn Outstanding Receivables

Analysis

Monthly Sales Trend

Sales by Product Category

Sales by Province

Outstanding Receivables by Status

Interactive Month and Province filters

<br>



2️⃣ Sales & Customers

Detailed customer and commercial-performance analysis.

Analysis

Top 10 Customers by Sales

Sales by Order Channel

Sales by Industry

Monthly Sales Trend

Province filtering

Month filtering

<br>



3️⃣ Inventory & Procurement

Operational visibility across inventory, suppliers and purchasing.

Analysis

Inventory Value by Product Category

Stock On Hand by Product Category

Procurement Spend by Supplier

Purchase Orders by Supplier

Inventory Value by Location

Procurement Spend Trend

Month filtering

Product-category filtering

<br>



4️⃣ Finance & Receivables

Accounts-receivable and invoicing analytics.

Key KPIs

R7.98bn Invoiced • R6.23bn Paid • R1.74bn Outstanding • 14K Invoices

Analysis

Outstanding Receivables by Status

Invoiced vs Paid by Month

Top 10 Customers by Outstanding Receivables

Invoice Count by Status

Province filtering

Month filtering

<br>



📈 Platform Metrics

Metric

Result

💰 Total Sales

R7.40bn

🧾 Sales Orders

15K

📊 Average Order Value

R497.82K

💳 Total Invoiced

R7.98bn

✅ Total Paid

R6.23bn

⚠️ Outstanding Receivables

R1.74bn

📦 Inventory Value

R62.51bn

🚚 Procurement Spend

R5.32bn

🔐 Security & Governance

Security is designed around Azure-native identity and access management.

Implemented controls include:

Microsoft Entra authentication

Azure RBAC

Azure Key Vault

Controlled ADLS permissions

Databricks access connector

Managed analytical access

More detail:

docs/security.md

📡 Monitoring & Operations

Azure Log Analytics provides a foundation for operational monitoring and troubleshooting.

The platform separates:

Infrastructure
      ↓
Ingestion
      ↓
Storage
      ↓
Transformation
      ↓
Data Quality
      ↓
Analytics

This allows failures to be investigated at the appropriate engineering layer rather than treating the platform as a single black box.

📁 Repository Structure

srid-azure-data-platform
│
├── docs
│   ├── images
│   │   ├── Exec Overview.png
│   │   ├── Sales & Cust.png
│   │   ├── Inv & Proc.png
│   │   └── Finance & Recv.png
│   │
│   ├── architecture.md
│   ├── dataset_inventory.md
│   └── security.md
│
├── scripts
│   └── generate_srid_data.py
│
├── terraform
│   └── environments
│       └── dev
│           └── main.tf
│
├── .gitignore
├── LICENSE
└── README.md

📚 Documentation

Document

Description

architecture.md

Platform architecture and engineering design

dataset_inventory.md

Dataset definitions and volumes

security.md

Identity, RBAC and security controls

🧭 Engineering Principles

This platform was built around production-style engineering principles:

Infrastructure should be repeatable and version controlled.

Source data should remain immutable after landing.

Raw, validated and analytical datasets should remain separated.

Invalid records should be quarantined rather than silently discarded.

Business logic should be applied before reporting.

Metrics should be defined once and reused.

Analytical models should follow clear dimensional relationships.

Security and monitoring should be designed into the platform.

🎯 What This Project Demonstrates

This project demonstrates hands-on capability across the complete modern data-platform lifecycle.

☁️ Cloud Engineering

Azure resource design

Terraform

Infrastructure as Code

Microsoft Entra ID

Azure RBAC

Key Vault

Log Analytics

Access control

⚙️ Data Engineering

ADLS Gen2

Azure Data Factory

Databricks

Python

PySpark

Delta Lake

Medallion architecture

Data-quality engineering

Quarantine patterns

Business transformations

🟦 Analytics Engineering

Microsoft Fabric

OneLake

SQL analytics

Dimensional modelling

Star schema design

Semantic modelling

Date dimensions

DAX measures

📊 Business Intelligence

Power BI

KPI development

Interactive slicers

Executive dashboards

Sales analytics

Customer analytics

Finance analytics

Inventory analytics

Procurement analytics

🔧 Engineering Workflow

Git

GitHub

Version control

Documentation

Reusable infrastructure

Source-controlled data-generation logic

🚀 Key Outcomes

The project demonstrates an end-to-end flow from cloud infrastructure through to business intelligence:

Terraform
    ↓
Azure Infrastructure
    ↓
ADLS Gen2
    ↓
Landing
    ↓
Bronze
    ↓
Silver
    ↓
Gold
    ↓
Microsoft Fabric
    ↓
Semantic Model
    ↓
Power BI
    ↓
Business Insights

Rather than focusing on one isolated technology, the project demonstrates how multiple Azure and Microsoft analytics services can work together as a complete modern data platform.

<div align="center">

👤 Author

Takudzwa Mhandire

Azure Data Engineering • Microsoft Fabric • Databricks • Terraform • Power BI
