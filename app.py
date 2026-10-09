from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return"Hello World!"

@app.route("/Sobre")
def sobre():
  return "Salve"

if __name__ == "__main__":
  app.run(debug=True)