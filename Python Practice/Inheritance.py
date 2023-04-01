#Most languages that support classes support inheritance
#DRY = Don't repeat yourself
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

#Pass means nothing
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()
cat1. = Cat()
cat1.walk