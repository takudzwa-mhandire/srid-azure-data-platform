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

resource "azurerm_data_factory" "data_factory" {
  name                = var.data_factory_name
  location            = azurerm_resource_group.data_dev.location
  resource_group_name = azurerm_resource_group.data_dev.name

  identity {
    type = "SystemAssigned"
  }

  tags = {
    environment = var.environment
    project     = "srid-azure-data-platform"
    managed_by  = "terraform"
  }
}
resource "azurerm_databricks_workspace" "data_platform" {
  name                = var.databricks_workspace_name
  resource_group_name = azurerm_resource_group.data_dev.name
  location            = azurerm_resource_group.data_dev.location
  sku                 = "premium"

  tags = {
    environment = var.environment
    project     = "srid-azure-data-platform"
    managed_by  = "terraform"
  }
}
resource "azurerm_log_analytics_workspace" "platform" {
  name                = var.log_analytics_workspace_name
  location            = azurerm_resource_group.data_dev.location
  resource_group_name = azurerm_resource_group.data_dev.name
  sku                 = "PerGB2018"
  retention_in_days   = 30

  tags = {
    environment = var.environment
    project     = "srid-azure-data-platform"
    managed_by  = "terraform"
  }
}
resource "azurerm_monitor_diagnostic_setting" "data_factory" {
  name                       = "diag-adf-srid-data-dev"
  target_resource_id         = azurerm_data_factory.data_factory.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.platform.id

  enabled_log {
    category_group = "allLogs"
  }

  enabled_metric {
    category = "AllMetrics"
  }
}
resource "azurerm_monitor_diagnostic_setting" "storage_blob" {
  name                       = "diag-st-srid-data-dev"
  target_resource_id         = "${azurerm_storage_account.data_lake.id}/blobServices/default"
  log_analytics_workspace_id = azurerm_log_analytics_workspace.platform.id

  enabled_log {
    category = "StorageRead"
  }

  enabled_log {
    category = "StorageWrite"
  }

  enabled_log {
    category = "StorageDelete"
  }

  enabled_metric {
    category = "Transaction"
  }
}
resource "azurerm_monitor_diagnostic_setting" "key_vault" {
  name                       = "diag-kv-srid-data-dev"
  target_resource_id         = azurerm_key_vault.data_platform.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.platform.id

  enabled_log {
    category_group = "allLogs"
  }

  enabled_metric {
    category = "AllMetrics"
  }
}
resource "azurerm_monitor_diagnostic_setting" "databricks" {
  name                       = "diag-dbw-srid-data-dev"
  target_resource_id         = azurerm_databricks_workspace.data_platform.id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.platform.id

  enabled_log {
    category_group = "allLogs"
  }
}
resource "azurerm_role_assignment" "adf_storage_blob_contributor" {
  scope                = azurerm_storage_account.data_lake.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_data_factory.data_factory.identity[0].principal_id
}
resource "azurerm_role_assignment" "adf_key_vault_secrets_user" {
  scope                = azurerm_key_vault.data_platform.id
  role_definition_name = "Key Vault Secrets User"
  principal_id         = azurerm_data_factory.data_factory.identity[0].principal_id
}
resource "azurerm_databricks_access_connector" "data_platform" {
  name                = var.databricks_access_connector_name
  resource_group_name = azurerm_resource_group.data_dev.name
  location            = azurerm_resource_group.data_dev.location

  identity {
    type = "SystemAssigned"
  }

  tags = {
    environment = var.environment
    project     = "srid-azure-data-platform"
    managed_by  = "terraform"
  }
}

resource "azurerm_role_assignment" "databricks_storage_blob_contributor" {
  scope                = azurerm_storage_account.data_lake.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = azurerm_databricks_access_connector.data_platform.identity[0].principal_id
}