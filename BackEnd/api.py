from openai import OpenAI
import json
client = OpenAI()

def lambda_handler(event, context): 
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={"type":"json_object"},
    temperature=0.7,
    messages=[{"role":"system", "content": "You are a helpful assistant designed to output JSON.\
                    And your json format should only be { \" response \" = your answer }"},
                {"role":"user","content":event['message']}],
    max_tokens=100
    )
    json_obj = json.loads(response.choices[0].message.content)
    return json_obj
