import requests
url = "https://jsonplaceholder.typicode.com/users"
respond =requests.get(url)
print(respond.status_code)
print(respond.text)
users = respond.json()
for user in users :

  print (user["name"])
  print (user["username"])
  print (user["email"])
  print (user["address"])
  print (user["phone"])
  print (user["website"])
try:
   print (user["email"])
except KeyError:
  print ("email not available")


  with open("eample4.py", "w") as file:
    for 