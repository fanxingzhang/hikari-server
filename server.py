from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import MALManager as MM

app = Flask(__name__)

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://UeusugiErii:SayonaraSensei123@hikaridb.c9umgfyeannc.us-east-2.rds.amazonaws.com/hikariDB'
db = SQLAlchemy(application)

@app.route('/')
def hellow_word():
	return jsonify({"message": "Hello World!"})

