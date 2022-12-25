from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
    time.sleep(3)
    return "hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080)