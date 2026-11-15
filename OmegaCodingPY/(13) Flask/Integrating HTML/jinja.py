from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>WELCOME TO FLASK</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello{name}!"
    return render_template('form.html')

'''Variable rule'''
# @app.route("/success/<int:score>")
# def success(score):
#     return "The marks you got is "+str(score)


### JINJA 2 TEMPLATE
'''
{{ }} expression to print output in html 
{%...%} conditions, for loop
{#...#} comments
'''
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',results=res)

@app.route("/successres/<int:score>")
def successres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    
    exp={'score':score,'res':res}

    return render_template('result1.html',results=exp)

if __name__=='__main__':
    app.run(debug=True)