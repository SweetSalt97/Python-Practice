names = ["Gupta" , "Mayuri" , "Bihari" , "Mishra" , "Badass" , "BigBoss"]
print(names)
print(names[0])
print(names[-1])
print(names[-2])
names[0] = "Gutka"
print(names)
print(names[0:3]) #Excluding the end index

numbers = [1,2,3,4,5]
numbers.append(67)
print(numbers)
numbers.insert(0, -1)
print(numbers)
numbers.remove(3)
print(numbers)
print(1 in numbers)
print(len(numbers))
numbers.clear()
print(numbers)

numbers= [1,2,3,4,5]
for item in numbers:
    print(item)