/**
 * Azure Storage Account component resource.
 */

import * as pulumi from "@pulumi/pulumi";
import * as storage from "@pulumi/azure-native/storage";

export interface StorageAccountArgs {
    resourceGroupName: pulumi.Input<string>;
    blobSource: pulumi.asset.Asset;
}

/**
 * A component resource for Azure Storage Account with a blob container and blob.
 */
export class StorageAccount extends pulumi.ComponentResource {
    public readonly account: storage.StorageAccount;
    public readonly container: storage.BlobContainer;
    public readonly blob: storage.Blob;
    public readonly primaryKey: pulumi.Output<string>;

    constructor(
        name: string,
        args: StorageAccountArgs,
        opts?: pulumi.ComponentResourceOptions
    ) {
        super("custom:storage:StorageAccount", name, args, opts);

        // Create an Azure Storage Account
        this.account = new storage.StorageAccount(
            `${name}account`,
            {
                resourceGroupName: args.resourceGroupName,
                sku: {
                    name: storage.SkuName.STANDARD_LRS,
                },
                kind: storage.Kind.StorageV2,
            },
            { parent: this }
        );

        // Create a blob container
        this.container = new storage.BlobContainer(
            `${name}-container`,
            {
                accountName: this.account.name,
                resourceGroupName: args.resourceGroupName,
            },
            { parent: this }
        );

        // Create a blob in the container
        this.blob = new storage.Blob(
            `${name}-blob`,
            {
                accountName: this.account.name,
                containerName: this.container.name,
                resourceGroupName: args.resourceGroupName,
                source: args.blobSource,
            },
            { parent: this }
        );

        // Export the primary key
        this.primaryKey = pulumi.output(args.resourceGroupName).apply(
            (rgName: string) =>
                pulumi.output(this.account.name).apply((accountName: string) =>
                    storage.listStorageAccountKeys(
                        {
                            resourceGroupName: rgName,
                            accountName: accountName,
                        },
                        { parent: this }
                    ).then((keys) => keys.keys[0].value)
                )
        ).apply((v: string) => v);

        this.registerOutputs({});
    }
}
