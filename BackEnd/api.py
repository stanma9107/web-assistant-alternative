import openai
import os
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config['OPENAI_API_KEY']

response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt="To solve x^2 = cos(0) + i*sin(0)"
)