import os
import sys
from openai import OpenAI
from dotenv import load_dotenv


def main(): 
    load_dotenv() 

    # https://platform.openai.com/docs/api-reference/authentication
    client = OpenAI(
        organization=os.getenv("ORGANIZATION_ID"),
        api_key=os.getenv("SECRET_KEY"),
        project=os.getenv("PROJECT_ID")
    )

    interaction_type = ""

    while True:
        print("Chat?  Talk?  Draw? Exit?")
        interaction_type = input()

        if interaction_type.lower() == "chat":
            # https://platform.openai.com/docs/api-reference/chat/create
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
            # https://platform.openai.com/docs/api-reference/audio/createSpeech
            print("What would you like to hear?")
            talk_input = input()
            response = client.audio.speech.create(
                model="tts-1",
                voice="alloy",
                input=talk_input)
            response.write_to_file("example.mp3")
        elif interaction_type.lower() == "draw":
            print("What would you like to draw?")
            draw_input = input()

            image = client.images.generate(
                model="dall-e-3",
                prompt=draw_input,
                n=1,
                size="1024x1024"
            )
            print(image.data[0].url)
        elif interaction_type.lower() == "exit":
            sys.exit(0)
        else:
            print("Sorry I don't understand.")

if __name__=="__main__": 
    main() 