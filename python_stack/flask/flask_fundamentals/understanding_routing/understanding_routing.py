from flask import Flask  
app = Flask(__name__)   

@app.route("/")          
def hello_world():
    return 'Hello World!' 

@app.route("/Champion")
def champion():
  return "Champion!"

@app.route("/say/<name>") 
def hi(name):
    print(name)
    return "Hi " + name +"!"

@app.route("/repeat/<int:num>/<word>") 
def repeat(num, word):
    return (word+" ")*num

@app.errorhandler(404)    # I looked it up online
def page_not_found(error):
    return "Sorry! No response. Try again.", 404

if __name__=="__main__":   
    app.run(debug=True)   

