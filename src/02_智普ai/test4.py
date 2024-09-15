import os
from zhipuai import ZhipuAI
from dotenv import load_dotenv
from zhipuai import ZhipuAI

load_dotenv(verbose=True)
api_key = os.environ.get('glmapikey')

client = ZhipuAI(api_key=api_key) 
l2m_prompt = """
Q: think, machine
A: The last letter of "think" is "k". The last letter of "machine" is "e". Concatenating "k" and "e" gives "ke". So "think, machine" output "ke".

Q: think, machine, learning
A: "think, machine" outputs "ke". The last letter of "learning" is "g". Concatenating "ke" and "g" gives "keg". So "think, machine, learning" is "keg".

Q: transformer, language
A: The last letter of "transformer" is "r". The last letter of "language" is "e". Concatenating "r" and "e" gives "re". So "transformer, language" is "re".

Q: transformer, language, vision
A: "transformer, language" outputs "re". The last letter of "vision" is "n". Concatenating "re" and "n" gives "ren". So "transformer, language, vision" is "ren".

Q: foo,bar,baz,blip,learn,prompting,world,shaking,event,dancefloor,prisma,giraffe
A:
"""

### create a function

def get_completion(prompt, model = "glm-3-turbo"):
    client = ZhipuAI(api_key=api_key)

    messages = [{"role":"user", "content":prompt}]

    response = client.chat.completions.create(
        model= model,
        messages=messages,
        temperature=0.95
    )
    return response.choices[0].message.content
r = get_completion(l2m_prompt)
print(r)