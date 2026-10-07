resource "azurerm_resource_group" "data_dev" {
  name     = var.resource_group_name
  location = var.location

  tags = {
    environment = var.environment
    project     = "srid-azure-data-platform"
    managed_by  = "terraform"
  }
}

resource "azurerm_storage_account" "data_lake" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.data_dev.name
  location                 = azurerm_resource_group.data_dev.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = true
  min_tls_version          = "TLS1_2"

  tags = {
    environment = var.environment
    project     = "srid-azure-data-platform"
    managed_by  = "terraform"
  }
}

data "azurerm_client_config" "current" {}

resource "azurerm_key_vault" "data_platform" {
  name                = var.key_vault_name
  location            = azurerm_resource_group.data_dev.location
  resource_group_name = azurerm_resource_group.data_dev.name
  tenant_id           = data.azurerm_client_config.current.tenant_id
  sku_name            = "standard"

  rbac_authorization_enabled = true

  tags = {
    environment = var.environment
    project     = "srid-azure-data-platform"
    managed_by  = "terraform"
  }
}