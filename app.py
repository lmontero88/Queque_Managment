from flask import Flask 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import Queue

app= Flask (__name__)

app.url_map.strict_slashes = False 
app.config['DEBUG'] = True 
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
aq = main()

@app.route('/')
def app():
    return 'helloooooo'


@app.route('/new', methods=['POST'])
def Create ():
    user = request.json.get('user', None)
    phone = request.json.get('phone', None)

     if not user:
        return jsonify({"msg": "name is required"}), 400
    if not phone:
        return jsonify({"msg": "phone is required"}), 400

    turno = Queue()
    turno.name = cliente
    turno.enqueue()

     msg = aq.enqueue(turno)

    return jsonify(msg), 200


@app.route('/new', methods=['GET'])
def dequeue():
    turno = aq.dequeue()
    return jsonify({"msg": "Processing next in line", "item": turno}), 200



@app.route('/all', methods=['GET'])
def queue():
    line = aq.get_queue()
    return jsonify(line), 200



if __name__ == "__main__":
    manager.run()