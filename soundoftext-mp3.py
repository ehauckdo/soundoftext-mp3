import requests
import json
import sys

API = "https://api.soundoftext.com/sounds"
input_file = open(sys.argv[1],'r')
language=sys.argv[2]
if language == "en":
    language="en-US"
elif language == "jp":
    language="ja-JP"
else:
    language="en-US"
for word in input_file.readlines():
    filename='{0}.mp3'.format(word.rstrip())
    data = {"engine":"Google","data":{"text":word,"voice":language}}
    headers = {'Content-type': 'application/json', 'Accept': '*/*'}
    r = requests.post(API, data=json.dumps(data), headers=headers, verify=False)
    id=json.loads(r.text)['id']
    url = "{0}/{1}".format(API, id)
    r = requests.get(url, headers=headers, verify=False)
    url_mp3=json.loads(r.text)['location']
    r=requests.get(url_mp3)
    open(filename, 'wb').write(r.content)

