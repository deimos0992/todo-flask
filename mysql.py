from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)

app.config['SECRET_KEY'] = 'some secret string here'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:''@localhost:3306/todo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
CORS(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)


@app.route('/api/tasks', methods=['GET'])
def get_all():
    user = Task.query.all()
    return jsonify(user)

@app.route('/prova', methods=['GET'])
def get():
    return jsonify("strunz")

if __name__ == '__main__':
    app.run(debug=True)