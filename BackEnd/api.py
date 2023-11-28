from openai import OpenAI
import json
import time 
client = OpenAI()

json_obj = ""
def get_response(message):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type":"json_object"},
        temperature=0.7,
        messages=[{"role":"system", "content":"You are a helpful assistant that extracts data and returns it in JSON format. Need to format as  \"response\": answer "},
                  {"role":"user","content":message}],
        max_tokens=100
    )
    return response.choices[0].message.content

def lambda_handler(event, context):
    return get_response(event['message'])