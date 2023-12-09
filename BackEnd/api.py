from openai import OpenAI
import json

client = OpenAI()

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
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type":"json_object"},
        temperature=0.7,
        messages=[{"role":"system", "content": "You are a helpful assistant designed to output JSON.\
                        And your json format should only be { \" response \" = your answer }"},
                {"role":"user","content":body['message']}],
        max_tokens=100
    )
    
    return {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": { "Content-type": "Application/json" },
        "body": response.choices[0].message.content
    }