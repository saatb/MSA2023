from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests

app = Flask(__name__)
app.config["DEBUG"] = True
#set secret key
app.config["SECRET_KEY"] = 'your secret key'

#function to request student data
def getStudentData(url):
    #make a request
    response = requests.get(url)

    #convert format to json
    responseJSON = response.json()
    return responseJSON
    


#create route for site index, will display all student data
@app.route('/', methods=['GET'])
def index():
    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    studentData = getStudentData(url)
    return render_template('index.html', studentData=studentData)

#run the flask application
app.run(port=5007)