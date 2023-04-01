num1 = 100000000
num2 = 10000000000
total = num1 + num2
print(total)

#This is same as this

num1 = 100_000_000
num2 = 100_000_00_000
total = num1 + num2
print(total)

#For easier counting _ doesnt do shit

#For the output to have separaters
print(f"{total:_}")
print(f"{total:,}")