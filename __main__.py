"""
Main entry point for the storage-component provider.
"""

from pulumi.provider.experimental import component_provider_host

from storage_account import StorageAccount

if __name__ == "__main__":
    component_provider_host(name="storageaccount", components=[StorageAccount])
