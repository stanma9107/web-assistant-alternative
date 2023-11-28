from openai import OpenAI
import json
client = OpenAI()

def lambda_handler(event, context):
    message = event["message"]
    meta = event["meta"]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type":"json_object"},
        temperature=0.7,
        messages=[{"role":"system", "content":"You are a helpful assistant that extracts data and returns it in JSON format. Need to format as \"response\": answer "},
                  {"role":"user","content":message}],
        max_tokens=100
    )
    json_obj = json.loads(response.choices[0].message.content)
    return json_obj