from flask import Flask, request, redirect
import requests
import json
import jinja2
import os

app = Flask(__name__)
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

@app.route("/")
def index():
	template = JINJA_ENVIRONMENT.get_template('index.html')
	return template.render()

@app.route("/home")
def home():
	template = JINJA_ENVIRONMENT.get_template('home.html')	
	return template.render()

@app.route("/profile")
def profile():
	template = JINJA_ENVIRONMENT.get_template('profile.html')
	return template.render()

@app.route("/get_home_data")
def get_home_data():

	return 

#@app.route("/fhirbaes", methods=['GET', 'POST'])
#def fhirFight():
#	print "==========="
#	print request
#	print request.values
#	return "yolo"

if __name__ == "__main__":
	app.run(debug=True)
