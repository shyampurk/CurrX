#!flask/bin/python
from flask import Flask, render_template, jsonify
 
app = Flask(__name__)
 
@app.route('/templates')
@app.route('/')
def index():
  return render_template('index.html')
 
@app.route('/index_get_data')
def stuff():
  # Assume data comes from somewhere else
  data = {
    "data": [
      
     {
        "success":"true",
        "currency":90.08222,
        "difference":28.093333
       }#,
      # {"success":"true",
        #"error":"error"}
         ]
  }
  return jsonify(data)
 
 
if __name__ == '__main__':
  app.run()
