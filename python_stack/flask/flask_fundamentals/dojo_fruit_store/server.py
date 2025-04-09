from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    form_strawberry=request.form["strawberry"]
    form_rasperry=request.form["raspberry"]
    form_apple=request.form["apple"]
    form_name=request.form["first_name"]
    form_lastname=request.form["last_name"]
    form_id=request.form["student_id"]
    return render_template("checkout.html", strawberry=form_strawberry, raspberry=form_rasperry,apple=form_apple, first_name=form_name, last_name=form_lastname, student_id=form_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    