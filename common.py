import requests

def send_webhook_message(webhook_url, content):
    data = {
        "content": content,
        "username": "Orbite"
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        raise Exception(f"Failed to send webhook message: {response.status_code} - {response.text}")
