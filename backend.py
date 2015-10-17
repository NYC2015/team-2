from flask import Flask, request, redirect
import requests
import json
import jinja2

@app.route("/", methods=['GET', 'POST'])
def index():
	pass

@app.route("/home", methods['GET', 'POST'])
def home():
	pass

@app.route("/profile", methods['GET', 'POST'])
def profile():
	pass


@app.route("/home", methods['GET', 'POST'])

@app.route("/home", methods['GET', 'POST'])

@app.route("/home", methods['GET', 'POST'])

@app.route("/fhirbaes", methods=['GET', 'POST'])
def fhirFight():
	print "==========="
	print request
	print request.values
	return "yolo"

if __name__ == "__main__":
	app.run(debug=True)
