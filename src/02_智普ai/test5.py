import os
from dotenv import load_dotenv

from openai import OpenAI
load_dotenv(verbose=True)
api_key = os.environ.get('Secret_Key')

question = """Hello,

I have discovered an issue in your system. Although it is 
easy to use, it is possible to gain access to all of your users' data. I have attached
a proof of concept. Please fix this issue as soon as possible.

Cheers,

Donny

Classify the above email as IMPORTANT or NOT IMPORTANT
"""
prompt = f"""{question}. Let's think step by step. 

Format: 
Return the result in a json string with two keys: answer and reason.
"""
def get_completion(prompt):
    client = OpenAI(
    api_key=api_key,
    base_url="https://api.gptsapi.net/v1/",
    )

    messages = [{"role":"user", "content":prompt}]

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "user", "content": prompt}
    ],
    temperature=0.99,
    )
    return response.choices[0].message.content

r = get_completion(prompt=prompt)
print(r)