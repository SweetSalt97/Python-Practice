age =int(input("Age: "))
print(age)
#Provide string
#How to handle errors

try:
    age =int(input("Age: "))
    income = 2000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cant be zero")
except ValueError:
    print("Invalid Value")