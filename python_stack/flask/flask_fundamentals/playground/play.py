from flask import Flask , render_template 
app = Flask(__name__) 

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/play')          
def playOne():
    return render_template("index.html")  

@app.route('/play/<num>')          
def playTwo(num):
    return render_template("play2.html", number=int(num))  

@app.route('/play/<num>/<color>')          
def playThree(num,color):
    return render_template("play2.html", number=int(num),color=color,level=True)

if __name__=="__main__":     
    app.run(debug=True)    