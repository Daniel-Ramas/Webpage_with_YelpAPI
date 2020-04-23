from flask import Flask, request, url_for
from flask_pymongo import PyMongo
from application import routes

app = Flask(__name__)
app.config['MONGO_URI'] = 'localhost:27017/admin.flaskfiletest'
mongo = Pymongo(app)