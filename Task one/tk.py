Person = {"name": "Amaka", "age": 13, "university": "Babcock University", "course":" Computer engineering"}
print(Person["name"])
print(Person["age"])
print(Person["university"])
print(Person["course"])

with open("Person.txt", "w") as file:
    for value in Person.values():
        file.write(str(value) + "\n")