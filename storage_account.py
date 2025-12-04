"""
Azure Storage Account component resource.
"""

import pulumi
from pulumi_azure_native import storage
from pulumi import ComponentResource, ResourceOptions, Input, Output
from typing import TypedDict

class StorageAccountArgs(TypedDict):
    """Arguments for the StorageAccount component."""
    resource_group_name: Input[str]
    """The name of the Azure resource group where resources will be created."""
    blob_source: pulumi.Asset
    """The source asset for the blob (e.g., FileAsset, StringAsset, or RemoteAsset)."""

class StorageAccountComponent(pulumi.ComponentResource):
    """A component resource for Azure Storage Account with a blob container and blob."""

    def __init__(
        self,
        name: str,
        args: StorageAccountArgs,
        opts: pulumi.ResourceOptions = None,
    ):
        super().__init__("custom:storage:StorageAccountComponent", name, None, opts)

        # Create an Azure Storage Account
        self.account = storage.StorageAccount(
            f"{name}account",
            resource_group_name=args['resource_group_name'],
            sku={
                "name": storage.SkuName.STANDARD_LRS,
            },
            kind=storage.Kind.STORAGE_V2,
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Create a blob container
        self.container = storage.BlobContainer(
            f"{name}-container",
            account_name=self.account.name,
            resource_group_name=args['resource_group_name'],
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Create a blob in the container
        self.blob = storage.Blob(
            f"{name}-blob",
            account_name=self.account.name,
            container_name=self.container.name,
            resource_group_name=args['resource_group_name'],
            source=args['blob_source'],
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Export the primary key
        self.primary_key = (
            pulumi.Output.all(args['resource_group_name'], self.account.name)
            .apply(
                lambda args: storage.list_storage_account_keys(
                    resource_group_name=args[0], account_name=args[1]
                )
            )
            .apply(lambda accountKeys: accountKeys.keys[0].value)
        )

        self.register_outputs({})













# from pulumi import ComponentResource, ResourceOptions, Input, Output
# from typing import TypedDict
# from pulumi_azure_native import storage
# import pulumi

# class StorageAccountArgs(TypedDict):
#     """Arguments for the StorageAccount component."""
#     resource_group_name: Input[str]
#     """The name of the Azure resource group where resources will be created."""
#     blob_source: pulumi.Asset
#     """The source asset for the blob (e.g., FileAsset, StringAsset, or RemoteAsset)."""


# class StorageAccount(ComponentResource):
#     """
#     A component resource for Azure Storage Account with a blob container and blob.
#     """
    
#     account: storage.StorageAccount
#     """The created Azure Storage Account resource."""
    
#     container: storage.BlobContainer
#     """The created blob container resource."""
    
#     blob: storage.Blob
#     """The created blob resource."""
    
#     primary_key: Output[str]
#     """The primary access key for the storage account."""

#     def __init__(self,
#                  name: str,
#                  args: StorageAccountArgs,
#                  opts: ResourceOptions = None):

#         super().__init__('custom:storage:StorageAccount', name, {}, opts)

#         resource_group_name = args['resource_group_name']
#         blob_source = args['blob_source']

#         # Create an Azure Storage Account
#         self.account = storage.StorageAccount(
#             f'{name}account',
#             resource_group_name=resource_group_name,
#             sku=storage.SkuArgs(
#                 name=storage.SkuName.STANDARD_LRS,
#             ),
#             kind=storage.Kind.STORAGE_V2,
#             opts=ResourceOptions(parent=self)
#         )

#         # Create a blob container
#         self.container = storage.BlobContainer(
#             f'{name}-container',
#             account_name=self.account.name,
#             resource_group_name=resource_group_name,
#             opts=ResourceOptions(parent=self)
#         )

#         # Create a blob in the container
#         self.blob = storage.Blob(
#             f'{name}-blob',
#             account_name=self.account.name,
#             container_name=self.container.name,
#             resource_group_name=resource_group_name,
#             source=blob_source,
#             opts=ResourceOptions(parent=self)
#         )

#         # Export the primary key
#         def get_primary_key(args):
#             rg_name = args[0]
#             account_name = args[1]
#             keys = storage.list_storage_account_keys(
#                 resource_group_name=rg_name,
#                 account_name=account_name
#             )
#             return keys.keys[0].value

#         self.primary_key = (
#             pulumi.Output.all(resource_group_name, self.account.name)
#             .apply(
#                 lambda args: storage.list_storage_account_keys(
#                     resource_group_name=args[0], account_name=args[1]
#                 )
#             )
#             .apply(lambda accountKeys: accountKeys.keys[0].value)
#         )
#         self.register_outputs({
#             'account': self.account,
#             'container': self.container,
#             'blob': self.blob,
#             'primary_key': self.primary_key
#         })
