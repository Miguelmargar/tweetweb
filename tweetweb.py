from flask import *
import os
from tweets import search_tweets

app = Flask(__name__)

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/results")
def get_results():
    search  = request.args.get('search')
    number  = int(request.args.get('number'))
    tweets  = search_tweets(search,number)
    return render_template("results.html", tweets = tweets )


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)