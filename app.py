
import requests
from flask import Flask, render_template, flash, request
app = Flask(__name__)
from database import *
@app.route('/' , methods = ['GET' , 'POST'])
def home():
    name = ""
    address = ""
    date = ""
    desc = ""
    contact = ""
    if (request.method == 'POST'):
        name = request.form['name']
        address = request.form['address']
        date = request.form['date']
        desc = request.form['desc']
        contact = request.form['contact']
        add_Event_To_Database(name , address , date , desc , contact)
    events = preview_database()
    return render_template('index.html',events = events)

if __name__ == "__main__":
    app.run(debug=True)
