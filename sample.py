import requests

x = requests.get('https://raw.githubusercontent.com/linuxacademy/content-elastic-log-samples/master/access.log').text

test = x.split('\n')

i = 0
for log in test:
    i+=1

print i