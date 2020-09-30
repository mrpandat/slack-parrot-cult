host = 'https://cultofthepartyparrot.com'


f = open('inventory')
for line in f:
    print(host + line)
f.close()
