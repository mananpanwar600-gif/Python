## Json is JavaScript Object Notation

##It is mainly used for storing and tranferring data between the browser and the server

##JSON is text, written with the JavaScript Object notation

##Python too supports JSON with a built-in package called json

# #In py json exsits as string

import json 

dict = {
    'course' : 'python',
    'fees'  : 2000
}
f = json.dumps(dict)
print(f)
print(type(f))   ##str