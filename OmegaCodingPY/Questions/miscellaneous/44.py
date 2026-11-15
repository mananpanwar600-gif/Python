'''
Calc total cost of item in shopping cart
'''

def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item["price"] * item["quantity"]
    
    return total_cost

cart = [
    {"name": "Python HandBook" , "price": 500 , "quantity": 1},
    {"name": "MacBook", "price": 180000, "quantity": 1},
    {"name": "Iphone", "price": 200000, "quantity": 1},
    {"name": "AirPods", "price": 13000, "quantity": 2}
]

print(calculate_total_cost(cart))