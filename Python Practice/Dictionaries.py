#For saving attributes
customer = {
    "name": "Ashutosh Jha",
    "age": 18,
    "is_verified": True
} 
#Curly braces for dictionaries
print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate" , "Jun 29 2004"))

#Editing
customer["name"] = "Ashutosh The Great"
print(customer["name"])

#New Key Value Pairs
customer["from"] = "New Delhi"
print(customer.get("from"))
