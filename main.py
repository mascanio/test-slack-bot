import os
import slack
from pprint import pprint

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

a = client.conversations_history(channel='CMKBSP2JW', limit='1')

pprint(a.data['messages'][0]['text'])
