import os
from flask import Flask
from datetime import date
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    name = "Ferko"
    if "MY_NAME" in os.environ:
        name = os.environ["MY_NAME"]
    return "<h1 style='color:blue'>Hello There {}!</h1>".format(name)

@app.route("/date")
def calendar():
    today = date.today()
    return "<p>{}</p>".format(today.strftime("%d.%m.%Y"))

@app.route("/connect")
def connect():
 connection = psycopg2.connect(database="postgres", user='postgres', 
                               password='mysecretpassword', host='database')
 return "<h1 style='color:blue'>Connected!</h1>"

if __name__ == "__main__":
    app.run()
