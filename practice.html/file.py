# with('data.json', 'w+') as file:
#   file.write({"name": "victor", "age": 25})
#   file.seek(0)
#   data = file.read()
#   print(data)
#   file = open("data.json", "w+")
#   file.write({"name":"Ama","age":"20"})
#   file.seek(0)
#   data = file.read()
#   print (data)

# Variable called store
# file = open("store.json", "w+")
# file.write({"name":"Ama","age":"20","store name":"blessed treets", "store products": 26})
# file.seek(0)
# data = file.read()
# print (data)

# json.dumps(store)
# result=(json.dumps(store))
# print(result)

with('data.json', 'A+') as file:
  file.write({"name": "victor", "age": 25})
  file.seek(0)
  data = file.read()
  print(data)

json.dumps(store)
result=(json.dumps(store))
print(result)