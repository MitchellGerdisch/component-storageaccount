# storage-component

A Pulumi component resource for Azure Storage Account with blob container and blob.

## Usage

```typescript
import { StorageAccount } from "@custom/storage-component";
import * as pulumi from "@pulumi/pulumi";

const storageComponent = new StorageAccount("storage", {
    resourceGroupName: resourceGroup.name,
    blobSource: new pulumi.asset.FileAsset("./README.md"),
});

export const primaryKey = pulumi.secret(storageComponent.primaryKey);
```

## Component Inputs

- `resourceGroupName` - The Azure resource group name
- `blobSource` - The asset to upload as a blob (FileAsset, StringAsset, etc.)

## Component Outputs

- `account` - The created StorageAccount resource
- `container` - The created BlobContainer resource
- `blob` - The created Blob resource
- `primaryKey` - The primary storage account key
