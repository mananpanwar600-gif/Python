class Animal:
    location = "Australia"
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speaking now!")

class Dog(Animal):  #This is how inheritance done in python
    def speak(self):
        super().speak() #We are using the speak function of parent class
        print("Woof!!")

b = Dog("Bruno")
b.speak()
print(b.location)