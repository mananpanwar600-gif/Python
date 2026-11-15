##Using method OVERRIDING

class Animal:
    def speak(self):
        return "Sound of the animal"

class Dog(Animal):
    def speak(self):
        return "Woof!!" 
    
class Cat(Animal):
    def speak(self):
        return "MEOW!"
    

    
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())