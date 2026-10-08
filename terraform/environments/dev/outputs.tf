output "resource_group_name" {
  value = azurerm_resource_group.data_dev.name
}

output "storage_account_name" {
  value = azurerm_storage_account.data_lake.name
}

output "key_vault_name" {
  value = azurerm_key_vault.data_platform.name
}
output "data_factory_name" {
  value = azurerm_data_factory.data_factory.name
}

output "databricks_workspace_name" {
  value = azurerm_databricks_workspace.data_platform.name
}
output "log_analytics_workspace_name" {
  value = azurerm_log_analytics_workspace.platform.name
}
output "databricks_access_connector_name" {
  value = azurerm_databricks_access_connector.data_platform.name
}