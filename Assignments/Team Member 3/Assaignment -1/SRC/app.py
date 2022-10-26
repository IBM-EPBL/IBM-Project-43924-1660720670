from tkinter.tix import Form
from flask import Flask ,render_template,url_for,redirect,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/success/<name>/<phone>/<email>')
def success(name=None,phone=None,email=None):
    return " <h1>Registered Successfully</h1><h2>Your Details Are:-</h2>  {} <br>{} <br> {} ".format(name , phone ,email)
    #  '{} {} {}'.format(firstname, lastname, cellphone)
@app.route("/login",methods =['POST','GET'])
def login():
    if request.method == 'POST':

        user = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        return redirect(url_for("success", name = user ,phone = phone ,email = email ))
        # name = user ,phone = phone ,email = email
    else:
        user = request.args.get("input_name")
        return redirect(url_for("success",name=user))


if __name__ == '__main__':
    app.run(debug=True)
