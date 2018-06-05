from flask import *
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/results")
def get_results():
    
    results = [
    {"id": 1003923768601927682, "text": "hello"},
    {"id": 1003953439855005697, "text": "hello again"}
    ]
    
    return render_template("results.html", tweets=results)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)