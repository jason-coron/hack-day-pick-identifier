
import os
import openai
import prompts.pick_identifier_prompts as prompts
import content.content_examples as content

def send_message_to_openai(prompt: str):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    print(prompt)

    return openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=50)

def identify_event_properties(content_text: str):
    prompt = f"{prompts.GET_EVENT_PROPERTIES}\n'''{content_text}'''"
    return send_message_to_openai(prompt)

def identify_pick_properties(content_text: str):
    prompt = f"{prompts.GET_PICK_PROPERTIES}\n'''{content_text}'''"
    return send_message_to_openai(prompt)

if __name__ == '__main__':
    event_response = identify_event_properties(content.example_01)
    print(event_response.choices[0].text.strip())