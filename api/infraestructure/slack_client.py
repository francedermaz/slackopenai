from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config.config import slack_token

slack_client = WebClient(token=slack_token)

def authenticate_slack():
    try:
        response = slack_client.auth_test()
        return response['ok']
    except SlackApiError as e:
        print(f"Failed to authenticate with Slack: {e.response['error']}")
        return False