
import os
import openai
import prompts.prompts as prompts
import content.content_examples as content
import content.content_urls as urls
import util.clipboard_util as clipboard_util
import util.html_util as html_util
import util.scrape_util as scrape_util

def send_message_to_openai(prompt: str):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    return openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=500)

def get_bet_suggestions(content):
    # remove html tags
    # build prompt
    prompt = f"{prompts.GET_EVENTS_AND_PICKS_FROM_CONTENT}\nTEXT[{content}]"

    # send prompt to openai
    return send_message_to_openai(prompt)

if __name__ == '__main__':
    text = scrape_util.scrape_article(urls.rg_example_nba)

    response = get_bet_suggestions(text)

    print(response.choices[0].text.strip())
    clipboard_util.copy(response.choices[0].text.strip())