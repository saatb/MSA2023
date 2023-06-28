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

#create a route for the majors search page
@app.route('/majors', methods=['GET', 'POST'])
def majors():
    #make a request to the student api url
    url = 'http://127.0.0.1:5000/api/students/all'

    #get student data
    studentData = getStudentData(url)
    listOfMajors = []
    #write code that gets the unique majors from the studentData list
    for student in studentData:
        if student['major'] not in listOfMajors:
            listOfMajors.append(student['major'])

    if request.method == 'POST':
        #get the form data
        major = request.form['major'].strip()
        #create list to store results
        resultList = []

        #validate form data
        if not major:
            flash("You must select a major.")
        else:
            #get students with selected major and place in a results list
            for student in studentData:
                if student['major'] == major:
                    resultList.append(student)
            return render_template('majors.html', listOfMajors=listOfMajors, resultList=resultList)

    return render_template('majors.html', listOfMajors=listOfMajors)

#run the flask application
app.run(port=5007)