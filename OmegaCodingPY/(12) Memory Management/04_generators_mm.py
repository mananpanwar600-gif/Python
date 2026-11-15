## GENERATOORS FOR MEMORY EFFICIENCY

def generate_numbers(n):
    for i in range(n):
        yield i


## using the generator

for num in generate_numbers(10000):
    print(num)
    if num>10:
        break