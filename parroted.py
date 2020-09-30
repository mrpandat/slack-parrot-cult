import os
from slack import WebClient

host = 'https://cultofthepartyparrot.com'


f = open('inventory')
for line in f:
    emojiName = line.split('.gif')[0].split('/')[-1]
    emojiUrl = host + line
    print('name: ' + emojiName)
    print('url: ' + emojiUrl)
    client = WebClient(token=os.environ['SLACK_API_TOKEN'])
    response = client.api_call(
    api_method='admin.emoji.add',
    json={'name': emojiName,'url': emojiUrl}
    )
    print("Parrot: " + emojiName + " parrotfuly added !")
f.close()

