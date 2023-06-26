#pip install flask
import flask
from flask import request, jsonify
import studentGeneratorV2

#create an app
app = flask.Flask(__name__)

#auto reload server when changes made
app.config["DEBUG"] = True

#load student dictionaries
studentDictionaries = studentGeneratorV2.getStudentDictionaries()

@app.route('/', methods=['GET'])
def index():
    return"<h1>My name is Avyam Bansal</h1>"


#create route to return all student data
@app.route('/api/students/all', methods=["GET"])
def api_all():
    return jsonify(studentDictionaries)

app.run()