# SRID Azure Data Platform

End-to-end Azure data engineering platform covering infrastructure provisioning, data ingestion, medallion architecture, data quality, dimensional modelling, Microsoft Fabric and Power BI reporting.

The project models a South African industrial distribution business using synthetically generated data.

## Architecture

```text
Source Data
    |
    v
ADLS Gen2 Landing
    |
    v
Bronze
    |
    v
Silver
    |
    +----> Quarantine
    |
    v
Gold
    |
    v
Microsoft Fabric / OneLake
    |
    v
Semantic Model
    |
    v
Power BI
```

The platform separates raw source data, validated datasets and business-ready analytical models so that each stage can be managed independently.

## Technology

| Area | Technology |
|---|---|
| Cloud | Microsoft Azure |
| Infrastructure | Terraform |
| Storage | ADLS Gen2 |
| Orchestration | Azure Data Factory |
| Processing | Azure Databricks / PySpark |
| Data format | Delta Lake |
| Security | Entra ID, RBAC, Key Vault |
| Monitoring | Azure Log Analytics |
| Analytics | Microsoft Fabric / OneLake |
| Reporting | Power BI |
| Source control | GitHub |

## Data Platform

The storage layer uses separate containers for:

```text
landing
bronze
silver
gold
quarantine
```

The source datasets cover:

- customers
- products
- suppliers
- sales orders
- sales order lines
- invoices
- payments
- inventory snapshots
- purchase orders
- shipment events

The data generator is stored in:

[`scripts/generate_srid_data.py`](scripts/generate_srid_data.py)

Dataset definitions and volumes are documented in:

[`docs/dataset_inventory.md`](docs/dataset_inventory.md)

## Processing

The platform follows a medallion architecture.

**Bronze** preserves the raw source representation.

**Silver** applies cleansing, type handling and data-quality checks, including primary-key validation, null checks, transaction rules and referential integrity.

Records that fail validation can be routed to the quarantine layer.

**Gold** contains business-ready datasets for sales, finance, inventory and procurement reporting.

## Microsoft Fabric and Semantic Model

Gold datasets are exposed to Microsoft Fabric through OneLake.

The reporting model uses a star-schema design:

| Dimensions | Facts |
|---|---|
| `dim_customer` | `fact_sales` |
| `dim_product` | `fact_finance` |
| `dim_supplier` | `fact_inventory` |
| `dim_date_import` | `fact_procurement` |

The date dimension supports consistent filtering across sales, finance, inventory and procurement.

Reusable DAX measures include:

### Sales

- Total Sales
- Sales Orders
- Units Sold
- Average Order Value

### Finance

- Total Invoiced
- Total Paid
- Outstanding Receivables
- Invoice Count

### Inventory

- Inventory Value
- Stock On Hand
- Available Stock

### Procurement

- Procurement Spend
- Purchase Orders
- Quantity Ordered

## Power BI Report

The final report contains four pages.

### Executive Overview

Management-level view across sales, finance, inventory and procurement.

![Executive Overview](docs/images/Exec%20Overview.png)

### Sales & Customers

Customer performance, sales channels, industry analysis and monthly sales trends.

![Sales and Customers](docs/images/Sales%20%26%20Cust.png)

### Inventory & Procurement

Inventory position, supplier activity, purchasing and procurement trends.

![Inventory and Procurement](docs/images/Inv%20%26%20Proc.png)

### Finance & Receivables

Invoicing, payments, outstanding receivables and customer exposure.

![Finance and Receivables](docs/images/Finance%20%26%20Recv.png)

## Example Metrics

| Metric | Result |
|---|---:|
| Total Sales | R7.40bn |
| Sales Orders | 15K |
| Average Order Value | R497.82K |
| Total Invoiced | R7.98bn |
| Total Paid | R6.23bn |
| Outstanding Receivables | R1.74bn |
| Inventory Value | R62.51bn |
| Procurement Spend | R5.32bn |

## Security and Monitoring

The platform uses Azure-native security controls including Entra ID, RBAC, Key Vault and controlled storage access.

Azure Log Analytics provides the monitoring foundation for the environment.

More detail is available in:

- [`docs/architecture.md`](docs/architecture.md)
- [`docs/security.md`](docs/security.md)
- [`docs/dataset_inventory.md`](docs/dataset_inventory.md)

## Repository Structure

```text
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
```

## What This Project Demonstrates

- Azure infrastructure provisioning with Terraform
- ADLS Gen2 data-lake design
- Azure Data Factory orchestration
- Databricks and PySpark processing
- Delta Lake
- Medallion architecture
- Data-quality and quarantine patterns
- Azure security and RBAC
- Microsoft Fabric and OneLake
- Dimensional modelling
- Power BI semantic modelling
- DAX measures
- Executive reporting and analytics

## Author

**Takudzwa Mhandire**

Azure Data Engineering | Microsoft Fabric | Databricks | Terraform | Power BI
