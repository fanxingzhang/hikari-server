from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hellow_word():
	return jsonify({"message": "Hello World!"})

