import openai
from config.config import openai_api_key

openai.api_key = openai_api_key

def get_summary(messages):
    prompt = "Summarize the content of the Slack channel: "
    for message in messages:
        if 'text' in message:
            prompt += message['text'] + " "

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )

    summary = response.choices[0].text.strip()
    return summary
