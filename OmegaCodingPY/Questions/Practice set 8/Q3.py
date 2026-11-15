# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 

class Attribute:
    a = 10

object = Attribute()
object.a = 0

print(object.a)
print(Attribute.a)