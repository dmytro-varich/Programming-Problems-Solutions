from datetime import date
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1><a href='/date'>Dátum a čas</a>"

@app.route("/date")
def today():
    today = date.today()
    return "<p>{}</p>".format(today.strftime("%d.%m.%Y"))

if __name__ == "__main__":
    app.run()