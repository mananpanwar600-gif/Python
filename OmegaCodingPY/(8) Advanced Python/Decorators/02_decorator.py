def decorator(func):
    def wrapper():
        print("I am about to execute the function....")
        func()
        print("I have executed the funtion...")
    return wrapper
@decorator
def say_hello():
    print("Hello!")

say_hello()