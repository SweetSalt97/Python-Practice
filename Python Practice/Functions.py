def greet_user():
    print("Hi There!\n")
    print("Welcome aboard")

print("Start")
greet_user()
print("Finish")

def greet(name):
    print("Hi",name)
a = input("Whats your name? ")
greet(a)

def insult(name):
    print("Fuck you",name,"You son of a bich")
insult(a)
#Parameter = name
#Attributes = actual input provied

#Setting Keyword Argument
calc_cost(total = 50, shipping =5, discount=0.1)
print("Finish")
