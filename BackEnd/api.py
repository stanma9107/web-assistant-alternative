<<<<<<< HEAD
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("openAI_key"),
)


def get_response(message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content
=======
import 
>>>>>>> 8a65219 (add: create BackEnd package)
