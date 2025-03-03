import os
from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello():
    name = "Ferko"
    if "MY_NAME" in os.environ:
        name = os.environ["MY_NAME"]
    return "<h1 style='color:blue'>Hello There {}!</h1>".format(name)

@app.route("/date")
def date():
    today = date.today()
    return "<p>{}</p>".format(today.strftime("%d.%m.%Y"))

if __name__ == "__main__":
    app.run()