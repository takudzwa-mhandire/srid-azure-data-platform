\# SRID Azure Data Platform — Security Design



\## DEV Security Approach



The DEV environment uses Azure identity and RBAC wherever practical rather than embedded credentials.



\### Azure Data Factory



Azure Data Factory uses a system-assigned managed identity.



Assigned permissions:



\- Storage Blob Data Contributor on the SRID ADLS Gen2 account

\- Key Vault Secrets User on the SRID Key Vault



This allows ADF to access platform resources without storing account keys or passwords in source code.



\### Azure Databricks



An Azure Databricks Access Connector with a system-assigned managed identity is used for secure storage access.



Assigned permission:



\- Storage Blob Data Contributor on the SRID ADLS Gen2 account



This provides an identity-based foundation for Databricks access to the data lake without embedding storage credentials.



\### Azure Key Vault



Azure Key Vault uses the Azure RBAC authorization model.



Secrets must not be stored in Terraform source files, GitHub repositories, notebooks or pipeline definitions.



\### Storage Security



The ADLS Gen2 account is configured with:



\- HTTPS-only access enabled

\- Minimum TLS version 1.2

\- Azure RBAC for data-plane permissions



\### Network Security Decision



Public network access remains enabled for the DEV environment to support development connectivity and avoid unnecessary private networking cost and complexity.



Access is still protected through:



\- Azure RBAC

\- Managed identities

\- HTTPS

\- TLS 1.2

\- Key Vault



For a production environment, the recommended hardening path would include:



\- Private Endpoints

\- Virtual Network integration

\- Restricted storage firewall rules

\- Restricted Key Vault network access

\- Controlled Databricks network connectivity



The DEV configuration therefore balances security, cost and development accessibility while preserving a clear production hardening path.

