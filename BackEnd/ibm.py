from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
import json

API_KEY = os.environ.get("IBM_API_KEY")
API_URL = os.environ.get("IBM_API_URL")
ENVIRONMENT_ID = os.environ.get("IBM_ENVIRONMENT_ID")

def lambda_handler(event, context):
  if event["httpMethod"] == "OPTIONS":
      return {
          "isBase64Encoded": True,
          "statusCode": 200,
          "headers": { 
              "Content-type": "Application/json",
              "Access-Control-Allow-Origin": "*",
              "Access-Control-Allow-Headers": "*",
              "Access-Control-Allow-Methods": "*"
          },
          "body": json.dumps({"message": "OPTIONS Success"})
      }
  body = json.loads(event['body'])

  session_id = body["session_id"] if "session_id" in body else None

  # IBM Watson Assistant
  authenticator = IAMAuthenticator(API_KEY)
  assistant = AssistantV2(
    version='2021-06-14',
    authenticator=authenticator
  )
  assistant.set_service_url(API_URL)

  # # Create Session
  if session_id is None:
    session = assistant.create_session(
        assistant_id=ENVIRONMENT_ID,
    ).get_result()
    session_id = session["session_id"]

  message = assistant.message(
    assistant_id=ENVIRONMENT_ID,
    session_id=session_id,
    input={
      'message_type': 'text',
      'text': body["message"]
    }
  ).get_result()

  output = message["output"]
  generic = output["generic"]

  return {
    "isBase64Encoded": True,
    "statusCode": 200,
    "headers": { 
        "Content-type": "Application/json",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*",
        "Access-Control-Allow-Methods": "*"
    },
    "body": json.dumps({"session_id": session_id, "generic": generic})
  }