import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3'
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment'
import * as _lambda from 'aws-cdk-lib/aws-lambda'
import * as apigw from 'aws-cdk-lib/aws-apigateway'

export class DeploymentStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create Lambda Container Function
    const lambdaFunction = new _lambda.DockerImageFunction(this, 'open-ai-function', {
      functionName: "open-ai-function",
      code: _lambda.DockerImageCode.fromImageAsset('../BackEnd'),
      environment: {
        "OPENAI_API_KEY": process.env.OPENAI_API_KEY || "",
      },
      timeout: cdk.Duration.seconds(30),
    })

    // Create API Gateway
    const api = new apigw.RestApi(this, 'open-ai-api', {
      restApiName: 'open-ai-api',
      description: 'This is a sample API Gateway'
    })
    
    // Create API Gateway Lambda Integration
    const chatRoute =  api.root.addResource('chat')
    chatRoute.addMethod('POST', new apigw.LambdaIntegration(lambdaFunction), {
      methodResponses: [
        {
          statusCode: '200',
        },
      ]
    })

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

    // Output the url of the api
    new cdk.CfnOutput(this, 'APIURL', {
      value: api.url,
    });
  }
}
