from zhipuai import ZhipuAI
import os
from dotenv import load_dotenv
load_dotenv(verbose=True)
api_key = os.environ.get('glmapikey')
client = ZhipuAI(api_key=api_key) 
question = "It taks Amy 4 minutes to climb to the top of a slide. It takes here 1 minute to slide down. The water slide closes in 15 minutes. How many times can she slide before it closes?"

MATH_PROMPT = f'''
Q: There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?

# solution in Python:
"""There were nine computers in the server room. Five more computers were installed each day, from monday to thursday. How many computers are now in the server room?"""
computers_initial = 9
computers_per_day = 5
num_days = 4  # 4 days between monday and thursday
computers_added = computers_per_day * num_days
computers_total = computers_initial + computers_added
result = computers_total
return result


Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?

# solution in Python:
"""Shawn has five toys. For Christmas, he got two toys each from his mom and dad. How many toys does he have now?"""
toys_initial = 5
mom_toys = 2
dad_toys = 2
total_received = mom_toys + dad_toys
total_toys = toys_initial + total_received
result = total_toys


Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?

# solution in Python:
"""Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. How many lollipops did Jason give to Denny?"""
jason_lollipops_initial = 20
jason_lollipops_after = 12
denny_lollipops = jason_lollipops_initial - jason_lollipops_after
result = denny_lollipops

Q: {question}

# solution in Python:
'''
response = client.chat.completions.create(
    model="glm-4",  
    messages=[
              {"role": "user", "content": MATH_PROMPT}
    ],
    temperature=0.95,1
)

print(response.choices[0].message.content)
