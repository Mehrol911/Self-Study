#Tuples #02:13:25
numbers = (1, 2, 3) #it is tuple () not []
#numbers[0] = 10 does not support to item assignment
print(numbers[0])
print(numbers)

#unpacking
coordinates = (1, 2, 3) #x,y,z
x = coordinates[0] 
y = coordinates[1] 
z = coordinates[2]

x, y, z = coordinates #exact the above code 
print(x)

#Dictionaries
customer = { #key and value (also in java, value can be anything)
    "name": "John Smith",
    "age": 30,
   # "age": 40,  keys should be uniqe  
    "is_verified": True
}
print(customer["name"])  #Name - KeyError
customer["name"] = "Jack Smith"
print(customer["name"])

customer["Gender"] = "Male"
print(customer.get("birthdate", "Jan 1 1980"))  # We get None means absence # adding default value
print(customer["Gender"])

#exercise
phone = input("Phone: ")
digits_mapping  = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)