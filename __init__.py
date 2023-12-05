from flask import Flask, render_template
from flask import session
from flask import request
from flask import redirect
import os
import dbtools
#import pandas as pd
app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route("/", methods = ["POST", "GET"])      
def hello_world():
    """Return base page. Mostly so it doesn't crash"""
    return render_template('main.html')



@app.route("/main", methods = ["POST", "GET"])
def home():
    dbtools.add_or_create(request.form["player_name"],request.form["culture_process"],request.form["culture_others"],request.form["hitting_swing"])
    averages = dbtools.get_average_scores()
    player_names = dbtools.list_player_names()
    print(averages)
    return render_template('main.html', averages = averages, players = player_names)

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()               # launch Flask/////////////