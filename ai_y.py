import os
import openai
# Clear the screen
os.system("clear")

# OpenAI
# Secret Key: sk-
# Load your API key from an environment variable or secret management service
openai.api_key = "ENTER YOUR KEY HERE!"


x = 0

while (x < 5):
	# Get user input:
	print("\nEnter ChatGPT Prompt: ")
	our_prompt = input()
	# Send Prompt to OpenAI API
	chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": our_prompt}])
	# Parse the response
	print(chat_completion["choices"][0]["message"]["content"])

	# Increment the counter
	x += 1