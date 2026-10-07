output "resource_group_name" {
  value = azurerm_resource_group.data_dev.name
}

output "storage_account_name" {
  value = azurerm_storage_account.data_lake.name
}

output "key_vault_name" {
  value = azurerm_key_vault.data_platform.name
}