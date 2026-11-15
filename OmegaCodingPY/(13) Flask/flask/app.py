from flask import Flask
'''
Creates an instance of flask which is WSGI which will interact with the web server
'''
#WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to FLASK. This is amazing Framework..."

@app.route("/index")
def index():
    return "Welcome to Index Page"

if __name__=='__main__':
    app.run(debug=True)