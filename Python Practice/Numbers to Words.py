phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)
#The plus-equals operator += provides a convenient way 
#to add a value to an existing variable 
#and assign the new value back to the same variable