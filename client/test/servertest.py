#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

output = [
    {
        'success': "true",
        'currency': 23.44,
        'difference': .98 
       
    },
    {
        'success':"false",
        'error':"error"
        
    }
]

@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'output': output})
if __name__ == '__main__':
    app.run(debug=True)
	
