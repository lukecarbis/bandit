#!/usr/bin/python

import sys
import openai

config = open('config.txt', 'r')
openai.api_key = config.readline().rstrip()
model=config.readline().rstrip()
prompt = "Bandit is from the television show Bluey. Continue this conversation between Bandit and his daughter Bluey, using Australian English.\n\n\nBluey: Hey Dad?\nBandit: What's up, Bluey?\nBluey: {0}\nBandit:"

# print (prompt.format(sys.argv[1]))

# create a completion
completion = openai.Completion.create(prompt=prompt.format(sys.argv[1]), temperature=0.9, max_tokens=64, presence_penalty=1, frequency_penalty=2, model=model, stop="\n")

# print the completion
print(completion.choices[0].text)
