import requests
import json
respond = requests.get("https://jsonplaceholder.typicode.com/users")
data = respond.json()
file = open('store.json', 'a+')
json.dump(data, file,indent=4)
file.seek(0)
savedata = json.load(file)
print(savedata)



