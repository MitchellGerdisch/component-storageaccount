# storage-component

A Pulumi component resource for Azure Storage Account with blob container and blob.

## Usage

```python
import pulumi
from storage_account import StorageAccount

storage_component = StorageAccount("storage", {
    'resource_group_name': resource_group.name,
    'blob_source': pulumi.FileAsset("./README.md"),
})

pulumi.export('primary_key', pulumi.Output.secret(storage_component.primary_key))
```

## Component Inputs

- `resource_group_name` - The Azure resource group name
- `blob_source` - The asset to upload as a blob (FileAsset, StringAsset, etc.)

## Component Outputs

- `account` - The created StorageAccount resource
- `container` - The created BlobContainer resource
- `blob` - The created Blob resource
- `primary_key` - The primary storage account key
