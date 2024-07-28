import os
import sys
from openai import OpenAI
from dotenv import load_dotenv


def main(): 
    load_dotenv() 
    client = OpenAI(
        organization=os.getenv("ORGANIZATION_ID"),
        api_key=os.getenv("SECRET_KEY"),
        project=os.getenv("PROJECT_ID")
    )

    interaction_type = ""

    while interaction_type != "exit()":
        print("Chat?  Talk?  Exit?")
        interaction_type = input()

        if interaction_type.lower() == "chat":
            print("What would you like to chat?")
            chat_input = input()

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": chat_input,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            print(chat_completion.choices[0].message.content)
        elif interaction_type.lower() == "talk":
            print("One moment for talk, please.")
        elif interaction_type.lower() == "exit":
            sys.exit(0)
        else:
            print("Sorry I don't understand.")
          
        print("Chat?  Talk?  Exit?")
        interaction_type = input()

if __name__=="__main__": 
    main() 