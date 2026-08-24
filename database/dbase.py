from pymongo import MongoClient
client = MongoClient("mongodb+srv://amakaessu_db_user:W5vhv7o1nNJS93Pc@cluster0.x55rxwr.mongodb.net/?authorSource=admin ")
db = client["school"]
students = db["students"]
# insert a new student document into the "students" collection
result = students.insert_one({
    "name": "Alex",
    "age": 20,
    "course": "Python",
    "city": "Lagos"
})

# print("Inserted ID:", result.inserted_id)

# # print("Connected successfully!")

# from pymongo import MongoClient
# # Replace with your real connection string from Atlas connection_string = "mongodb+srv://amakaessu_db_user:"
# client = MongoClient("connection_strig")
# db = client["students"]
# students = db["students"] 
# print("connected to Atlas!")

results2 = students.insert_many([
{"name": "Bola", "age": 22, "course": "Python", "city": "Abuja"},
{"name": "Chioma", "age": 19, "course": "Data Science", "city": "Lagos"},
{"name": "David", "age": 21, "course": "Python", "city": "Port Harcourt"}
])

print("Multiple students inserted!", results2.inserted_ids)

