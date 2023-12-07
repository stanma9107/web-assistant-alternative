import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3'
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment'
import * as iam from 'aws-cdk-lib/aws-iam'

export class DeploymentStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create S3 bucket
    const bucket = new s3.Bucket(this, 'web-assistant-alternative-ntust', {
      websiteIndexDocument: 'index.html',
      websiteErrorDocument: 'index.html',
      bucketName: 'web-assistant-alternative-ntust',
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      blockPublicAccess: {
        blockPublicAcls: false,
        blockPublicPolicy: false,
        ignorePublicAcls: false,
        restrictPublicBuckets: false
      },
      publicReadAccess: true,
      objectOwnership: s3.ObjectOwnership.OBJECT_WRITER,
    });

    // Sync the contents of the website folder with the S3 bucket
    new s3deploy.BucketDeployment(this, 'DeployWebsite', {
      sources: [s3deploy.Source.asset('../frontend/dist')],
      destinationBucket: bucket,
    });

    // Output the url of the website
    new cdk.CfnOutput(this, 'WebsiteURL', {
      value: bucket.bucketWebsiteUrl,
    });
  }
}
