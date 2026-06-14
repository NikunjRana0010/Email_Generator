import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=api_key)

Sytem_Prompt = """
You are an expert professional email copywriter. Your task is to draft highly effective, context-aware emails based on the provided parameters.

When provided with a Recipient Name, Purpose, and Tone, you must generate a complete email following these rules:
Subject Line: Write a concise, compelling subject line that clearly reflects the email's purpose.

Salutation: Open with an appropriate greeting using the provided Recipient Name, matched to the requested tone.

Body: Draft the main message clearly and concisely. You must strictly adhere to the requested tone (e.g., formal, friendly, apology, request).

Sign-off: Provide a suitable closing statement and sign-off.

Formatting: Output only the email itself. Do not include introductory or concluding conversational text.
"""

#User Input
recipient_name = input("Enter Recipient Name")
purpose_of_mail = input("Enter Purpose of Mail")
tone = input("Enter Tone of mail")

user_prompt = f"""
recipient name = {recipient_name}
purpose of mail = {purpose_of_mail}
tone = {tone}

Write mail from above details.
"""

prompt = (
    {"role": "system", "content": Sytem_Prompt},
    {"role": "user", "content": user_prompt}
)

response = openai.chat.completions.create(model= "gpt-5-nano", messages= prompt)

print(response.choices[0].message.content)

