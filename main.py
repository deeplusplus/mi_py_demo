import os
import logging
from openai import OpenAI
from dotenv import load_dotenv


def main(): 
    load_dotenv() 
    client = OpenAI(
        organization=os.getenv("ORGANIZATION_ID"),
        api_key=os.getenv("SECRET_KEY"),
        project=os.getenv("PROJECT_ID")
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)

  
  
if __name__=="__main__": 
    main() 