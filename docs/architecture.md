# SRID Azure Data Platform Architecture

## Overview

Sable Ridge Industrial Distribution (SRID) is implementing an Azure-based data platform to support finance, sales, inventory and logistics reporting.

The platform is designed as an enterprise-style portfolio implementation using synthetic business data.

The solution separates infrastructure provisioning, ingestion, transformation, security, monitoring and analytics into reusable components.

## Business Data Period

Operational source data:

`2025-10-01 to 2026-03-31`

Primary reporting period:

`2026-03-31`

Primary Azure region:

`South Africa North`

## High-Level Architecture

```text
Source Systems
     │
     ├── ERP CSV extracts
     ├── SQL source data
     ├── Supplier files
     └── Logistics REST API
            │
            ▼
     Azure Data Factory
            │
            ▼
       ADLS Gen2
        Landing
            │
            ▼
         Bronze
            │
            ▼
 Azure Databricks / PySpark
            │
            ▼
         Silver
            │
      Data Quality
       Quarantine
            │
            ▼
          Gold
            │
            ▼
   Power BI / Fabric
