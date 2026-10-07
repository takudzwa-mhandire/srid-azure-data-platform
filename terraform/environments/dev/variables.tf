variable "environment" {
  description = "Deployment environment name"
  type        = string
}

variable "location" {
  description = "Azure region used for SRID resources"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the Azure Resource Group"
  type        = string
}

variable "storage_account_name" {
  description = "Name of the DEV ADLS Gen2 storage account"
  type        = string
}

variable "key_vault_name" {
  description = "Name of the DEV Azure Key Vault"
  type        = string
}