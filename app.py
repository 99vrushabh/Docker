

from flask import Flask


app = Flask(__name__)

@app.get("/")
def check():
    return "hello world..."

app.run(debug=True)
