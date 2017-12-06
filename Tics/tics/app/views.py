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
	select * from (select * from alerta) as FOO order by id desc;

	"""
	print sql
	cur.execute(sql)
	alertas = cur.fetchall()
	#print alertas
	sql = """
	select foo.fecha from (select * from encendido) as foo order by foo.fecha desc;
	"""
	cur.execute(sql)
	encendido = cur.fetchall()
	sql = """
	select foo.fecha from (select * from apagado) as foo order by foo.fecha desc;
	"""
	cur.execute(sql)
	apagado = cur.fetchall()
	print encendido
	return render_template("index.html",alertas=alertas, encendido = encendido)



    
