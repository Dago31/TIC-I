from app import app
from datetime import datetime
from flask import render_template,request,redirect
from config import *
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%("tics1","localhost","tics1","1234"))
cur = conn.cursor()

@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():

	sql = """
	select * from alerta ;
	"""
	print sql
	cur.execute(sql)
	alertas = cur.fetchall()
	print alertas
	return render_template("index.html",alertas=alertas)



    
