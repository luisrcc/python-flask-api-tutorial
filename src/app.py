from flask import Flask, jsonify, request
app = Flask(__name__)
import json

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])

def hello_world():
    # supongamos que tienes cierta información (some_data) en una variable json
    some_data = { "name": "Bobby", "lastname": "Rixer" }

    # puedes convertir esa variable en un string json así
    json_text = jsonify(todos)

    # y luego puedes retorarla (return) en el response body así:
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)   
    decoded_object = json.loads(request_body)  
    
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    
    
    todos.pop(position)
    return jsonify(todos)



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)