host = 'https://cultofthepartyparrot.com'


f = open('inventory')
for line in f:
    emojiName = line.split('.gif')[0].split('/')[-1]
    emojiUrl = host + line
    print('name: ' + emojiName)
    print('url: ' + emojiUrl)
f.close()
