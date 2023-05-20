
import os
import openai
import prompts.pick_identifier_prompts as prompts
import content.content_examples as content
import util.html_util as html_util
import util.clipboard_util as clipboard_util

def send_message_to_openai(prompt: str):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    return openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=500)

def get_bet_suggestions(content_text: str):
    # remove html tags
    sanitized_text = html_util.get_text_from_html(content_text)
    # build prompt
    prompt = f"{prompts.GET_EVENTS_AND_PICKS}\nTEXT[{sanitized_text}]"

    # send prompt to openai
    return send_message_to_openai(prompt)

if __name__ == '__main__':
    response = get_bet_suggestions(content.example_03)

    print(response.choices[0].text.strip())
    clipboard_util.copy(response.choices[0].text.strip())