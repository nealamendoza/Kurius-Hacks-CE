
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/api' , methods = ['GET' , 'POST'])
def home():
    return{
    'test': "yuh this is a test"
    }

if __name__ == "__main__":
    app.run(debug=True)
