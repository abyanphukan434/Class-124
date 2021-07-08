from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy Grocerries',
        'description': u'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/')

def hello_world():
    return 'Hello World!'

@app.route('/add-data', methods = ['POST'])

def add_task():
    if not request.json: 
        return jsonify({
            "status": 'error',
            "message": "Please provide us the data"
        }, 400)

    task = {
        'id': tasks[-1]['id'] + 1, 
        'title': request.json['title'], 
        'description': request.json.get('description', ""), 
        'done': False
    }

    tasks.append(task)

    return jsonify({
        'status': 'success',
        'message': 'Task added successfully.'
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        'data': tasks
    })

if (__name__ == '__main__'):
    app.run(debug = True)