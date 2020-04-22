from application import app, YelpSearchAlgorithm
from flask import render_template, request
#pull data from api


@app.route("/", methods=["GET", "POST"])
def dashboard(login = True):
	return render_template("dashboard.html")

@app.route("/swipe", methods=["GET", "POST"])
def swipe():
	term = request.form.get('term')
	limit = int(request.form.get('limit'))
	radius = int(request.form.get('radius'))
	sort_by = request.form.get('sort_by')
	location = request.form.get('location')
	data = YelpSearchAlgorithm.pullDataFromYelpAPI(term, limit, radius, sort_by, location)
	return render_template("swipe.html", data=data)