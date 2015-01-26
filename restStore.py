from store import store
from flask import Flask,request
import datetime
import json
import datetime

class myServer(Flask):
   def __init__(self, *args, **kwargs):
      super(myServer, self).__init__(*args, **kwargs)

      self.store = store(datetime.timedelta(minutes=1))

app = myServer(__name__)

@app.route("/get")
def getData():
    data = app.store.getData( datetime.datetime.now() )
    return json.dumps(data)

@app.route("/store", methods=['POST'])
def store():
    data = json.loads(request.form['data']) 
    for x in data:
       app.store.store(x, datetime.datetime.now()) 
    return json.dumps({"success":"ok"})

@app.route("/flush")
def flush():
    app.store.flush()
    return json.dumps({"success":"ok"})

if __name__ == "__main__":
    app.run()
