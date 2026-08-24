 # shop = {"fruits": ["apple", "banana", "orange", "grape", "kiwi", "banana", "spag", "rice", "water", "books","clothes", "pen"]
#         } 
# print(shop["fruits"][7])
 # print(shop["fruits"][8])

 # variable are containers for storing data values

# name = "Victor"
# age = 25
# price = 5000

# print(name)
# print(age)
# print(price)

# # Data types tell Python what kind of value something is.

 # 1. STRING 
 # A string is text written inside quotation marks.

# name = "Victor"
# product = "Rice"

# print(name)
# print(product)


# 2. INTEGER (int)
 # An integer is a whole number without a decimal point.

# age = 25
# quantity = 10

# print(age)
# print(quantity)


 # 3. FLOAT (float)
# A float is a number that has a decimal point.

# price = 2500.50
# weight = 2.5
#  4. BOOLEAN (bool)
# represents True or False.

# is_open = True
# is_closed = False

# print(is_open)
# print(is_closed)


# # 5. LIST (list)
# # A list stores multiple values in one variable.


# products = ["rice", "beans", "bread", "milk"]

#  print(products)
 # 6. DICTIONARY (dict)
 # A dictionary stores data using key and value pairs.
 # student = {
#     "name": "Victor",
#     "age": 25,
 #     "course": "Software Engineering"
 # }

# print(student)


 # OPERATORS
# Operators are symbols used to perform operations on values.


 # 1. ARITHMETIC OPERATORS
 # Used for mathematical calculations.

# a = 10
# b = 3

# print(a + b)   # for Addition
# print(a - b)   #  for Subtraction
# print(a * b)   # for Multiplication
# print(a / b)   # for Division
# print(a // b)  # for Floor division
# print(a % b)   # for Modulus (with remainder)
# print(a ** b)  # for Exponent


 # 2. COMPARISON OPERATORS
 # Used to compare two values.
 # They return True or False.

# x = 10
# y = 5

# print(x == y)   # Equal to
# print(x != y)   # Not equal to
# print(x > y)    # Greater than
# print(x < y)    # Less than
# print(x >= y)   # Greater than or equal to
# print(x <= y)   # Less than or equal to


# 3. ASSIGNMENT OPERATORS
 # Used to assign or update values.

# number = 10

# number += 5     # Same as number = number + 5
# print(number)

# number -= 2     # Same as number = number - 2
# print(number)

# number *= 2     # Same as number = number * 2
# print(number)

# number /= 2     # Same as number = number / 2
# print(number)


# 4. LOGICAL OPERATORS
 # Used to combine conditions.

# age = 25

# print(age > 18 and age < 30)  # Both conditions must be True
# print(age > 30 or age == 25)  # At least one condition must be True
# print(not age == 25)          # Reverses True to False
# conditional state


day = 3

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid")

Names = ['mr isaac', 'redeemer']
if 'mr victor' in Names:
    print("mr victor is here")
else:
    print("mr victor is not here")

    # Casting means changing a value from one data type to another.
# For example, you can change a string "25" into an integer 25.
# 1. String to Integer
# age = "25"
# age = int(age)

# print(age)
# print(type(age))

# 2. Integer to Float
# number = 10
# number = float(number)

# print(number)
# print(type(number))

# 3. Integer to String
# age = 25
# age = str(age)

# print(age)
# print(type(age))

# 4. Float to Integer
# price = 25.8
# price = int(price)

# print(price)
# print(type(price))

# 5. String to Float
# price = "1500.50"
# price = float(price)

# print(price)
# print(type(price))



