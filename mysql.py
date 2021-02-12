from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pymysql

app = Flask(__name__)
connection = pymysql.connect(host="localhost",user="root",passwd="manager",database="todo" )
cursor = connection.cursor()

app.config['SECRET_KEY'] = 'some secret string here'
#app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:manager@localhost/todo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
CORS(app)
ma = Marshmallow(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    def __init__(self,title):
        self.title=title

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','title')


product_schema = ProductSchema()
product_schema = ProductSchema(many=True)



@app.route('/api/tasks', methods=['GET'])
def get_all():
    all_tasks = Task.query.all()
    result = product_schema.dump(all_tasks)
    return jsonify(result)


@app.route('/api/task', methods=['POST'])
def insert_task():
    title = request.json['title']

    new_task = Task(title)
    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task)


if __name__ == '__main__':
    app.run(debug=True)