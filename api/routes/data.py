from flask import Blueprint, jsonify
from infraestructure.slack_client import authenticate_slack
from controller.slack_integration import fetch_channel_messages
from controller.openai_integration import get_summary
from config.config import slack_channel_id

main = Blueprint('data_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_prompt_response():
    if authenticate_slack():
        messages = fetch_channel_messages(slack_channel_id)
        summary = get_summary(messages)
        return jsonify({'message': summary})
    return jsonify({'error': "Error auth slack"})
