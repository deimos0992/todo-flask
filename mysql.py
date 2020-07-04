from flask import Flask,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)

app.config['SECRET_KEY'] = 'some secret string here'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/todo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
CORS(app)
ma = Marshmallow(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)

    def __init__(self,id,title):
        self.id = id
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

@app.route('/prova', methods=['GET'])
def get():
    return jsonify("strunz")

if __name__ == '__main__':
    app.run(debug=True)