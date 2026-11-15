##ARRAY
import array
arr = array.array('i',[1,2,3,4])
print(arr)

##RANDOM
import random
print(random.randint(1,10))
print(random.choice(["apple","banana","cherry"]))

##DATA SERIALIZATION
import json
data={'name':"MSP",'age': 19}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data = json.loads(json_str)
print(parsed_data)
print(type(parsed_data))

## CSV

# import csv

# with open("exapmle.csv",mode="w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["name","age"])
#     writer.writerow(["MSP",19])

# with open("exapmle.csv",mode="r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

## DATE AND TIME
from datetime import datetime,timedelta

now = datetime.now()
print(now)

yesterday = now-timedelta(days=1)
print(yesterday)

## TIME
import time
print("q")
time.sleep(2)
print("p")

##REGULAR EXPRESSION
import re
pattern = r'\d+'
text = "There are 123 apples 456"
match = re.search(pattern,text)
print(match.group())