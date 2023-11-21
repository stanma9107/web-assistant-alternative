from openai import OpenAI
import ujson

client = OpenAI()


def get_response(message):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages= [
            {
             "role": "system", 
             "content": "You are a helpful assistant designed to output JSON.\
                        And your json format should only be { \" response \" = your answer }"
             },  
            {
                "role": "user",
                "content": message
            }
        ]
    )

    json_response = ujson.loads(chat_completion.choices[0].message.content)

    return json_response