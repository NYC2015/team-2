from flask import Flask, request, redirect
import requests
import json
import jinja2
import os
import pymysql

app = Flask(__name__)
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
db = pymysql.connect(host='localhost', passwd='seedling', user='root', db='Seedling')

@app.route("/")
def index():
	template = JINJA_ENVIRONMENT.get_template('index.html')
	return template.render()

@app.route("/profileView")
def home():
	template = JINJA_ENVIRONMENT.get_template('profileView.html')	
	return template.render()

@app.route("/profile")
def profile():
	template = JINJA_ENVIRONMENT.get_template('profile.html')
	return template.render()

@app.route("/get_home_data")
def get_home_data():
	cursor = db.cursor()
	sql = "SELECT * FROM Everything"
	cursor.execute(sql)
	rows = [i for i in cursor]
	output = {}
	for row in rows:
		if row[2] not in output:
			output[row[2]] = []
		output[row[2]].append(row)
	return json.dumps(output)
		 
@app.route("/videos")
def get_videos():
	cursor = db.cursor()
	sql = "SELECT * FROM Videos"
	cursor.execute(sql)
	rows = [i for i in cursor]
	output = {}
	for row in rows:
		if row[0] not in output:
			output[row[0]] = []
		output[row[0]].append(row)
	return json.dumps(output)
#@app.route("/fhirbaes", methods=['GET', 'POST'])
#def fhirFight():
#	print "==========="
#	print request
#	print request.values
#	return "yolo"

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
    	app.run(host='0.0.0.0', port=port, debug=True)
