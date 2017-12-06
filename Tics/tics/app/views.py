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
	select foo.fecha from (select * from encendido) as foo order by foo.fecha ;
	"""
	cur.execute(sql)
	encendido = cur.fetchall()
	sql = """
	select foo.fecha from (select * from apagado) as foo order by foo.fecha ;
	"""
	cur.execute(sql)
	apagado = cur.fetchall()
	enc = []
	apa = []
	for i in encendido:
		if i[0].day == datetime.now().day  :
			enc.append(i[0])

	for i in apagado:
		if i[0].day == datetime.now().day :
			apa.append(i[0])

	aux = []
	h = 0
	for i in range(24):
		if i <= datetime.now().hour:
			if i == enc[h].hour:
				aux.append([str(i)+":00",str(1)])
				if h < len(enc):
					while enc[h].hour == i and h < len(enc):
						h+=1
						if h >= len(enc)-1:
							break
			else:
				aux.append([str(i)+":00",str(0)])
		else:
			aux.append([str(i)+":00",str()])

	aux1 = [[],[],[],[],[]]
	for j in range(5):
		enc = []
		for i in encendido:
			if i[0].day == datetime.now().day-(j+1) :
				enc.append(i[0])

		h = 0
		for i in range(24):
			if len(enc)==0:
				aux1[j].append([str(i)+":00",str(0)])
			elif i == enc[h].hour:
				aux[j].append([str(i)+":00",str(1)])
				if h < len(enc):
					while enc[h].hour == i and h < len(enc):
						h+=1
						if h >= len(enc)-1:
							break
			else:
				aux1[j].append([str(i)+":00",str(0)])


	return render_template("index.html",alertas=alertas, encendido1 = aux, encendido2 = aux1[0], encendido3 = aux1[1], encendido4 = aux1[2], encendido5 = aux1[3], encendido6 = aux1[4], d1 =str(datetime.now().day), d2 =str(datetime.now().day-1), d3 =str(datetime.now().day-2), d4 =str(datetime.now().day-3), d5 =str(datetime.now().day-4), d6 =str(datetime.now().day-5))
