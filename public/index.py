import sys
sys.path.append('/Users/Jacy/Documents/Dropbox/BaconSearch')

import json
from flask import Flask
from flask import request
from flask import render_template
from flask import abort
from src.BaconSearch import BaconSearch

app = Flask(__name__)

bacon = BaconSearch('/Users/Jacy/Documents/Dropbox/BaconSearch/data/films')

@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    query = request.get_json()
    bacon.search(query['query'], 'Kevin Bacon')
    path = bacon.getJSONPath()
    if path == None:
      abort(404)
    else:
      return json.dumps(path)

if __name__ == "__main__":
  app.run()
