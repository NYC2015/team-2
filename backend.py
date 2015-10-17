from flask import Flask, request, redirect, send_from_directory
import requests
import json
import jinja2
import os
import pymysql

app = Flask(__name__, static_url_path='')
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
db = pymysql.connect(host='localhost', passwd='seedling', user='root', db='Seedling')

@app.route('/videos/<path:path>')
def send_videos(path):
	print "sending videos"
	return send_from_directory('videos', path)

@app.route('/js/<path:path>')
def send_js(path):
    print "sending js"
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    print "sending css"
    return send_from_directory('css', path)

@app.route('/pics/<path:path>')
def send_jpg(path):
	print "sending jpg"
	return send_from_directory('pics', path)

@app.route("/")
def index():
	template = JINJA_ENVIRONMENT.get_template('index.html')
	return template.render()

@app.route("/profileView")
def profileView():
	template = JINJA_ENVIRONMENT.get_template('profileView.html')	
	return template.render()

@app.route("/project")
def project():
	template = JINJA_ENVIRONMENT.get_template('project.html')
	return template.render()

@app.route("/get_home_data", methods=['POST'])
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
		 
@app.route("/videos", methods=['POST'])
def get_videos():
	cursor = db.cursor()
	sql = "SELECT * FROM Videos"
	cursor.execute(sql)
	rows = [i for i in cursor]
	output = {}
	for row in rows:
		output[row[0]] = row
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
