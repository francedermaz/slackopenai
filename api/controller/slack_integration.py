from slack_sdk.errors import SlackApiError
from infraestructure.slack_client import slack_client

def fetch_channel_messages(channel_id):
    try:
        response = slack_client.conversations_history(channel=channel_id)
        messages = response['messages']
        return messages
    except SlackApiError as e:
        print(f"Failed to fetch channel messages: {e.response['error']}")
        return []