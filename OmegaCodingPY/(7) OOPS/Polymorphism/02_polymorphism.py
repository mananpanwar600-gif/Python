class Animal:
    def speak(self):
        return "Sound of the animal"

class Dog(Animal):
    def speak(self):
        return "Woof!!" 
    
class Cat(Animal):
    def speak(self):
        return "MEOW!"
    

#Function that demonstrate Polymorphism

def animal_speak(animal):
    print(animal.speak())

    
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)

