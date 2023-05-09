import requests
import json

def send_slack_message(payload, webhook):

    return requests.post(webhook, json.dumps(payload))

webhook = "https://hooks.slack.com/services/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"
payload = {"text": "Hello This is Ahmed"}
send_slack_message(payload, webhook)