"""from config import *
import psycopg2
conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))

cur = conn.cursor()

 sql = """ #DROP SCHEMA public CASCADE;
# CREATE SCHEMA public;
# """

# cur.execute(sql)

#sql = """
"""CREATE TABLE habitacion( id serial PRIMARY KEY , tipo varchar, id_on integer, id_off integer , id_wr integer);

CREATE TABLE encendido(id serial PRIMARY KEY , fecha timestamp);

CREATE TABLE apagado(id serial PRIMARY KEY , fecha timestamp);

CREATE TABLE alerta(id serial PRIMARY KEY , fecha timestamp);
"""

#queda con 255 el varchar
"""cur.execute(sql)
conn.commit()
cur.close()
conn.close()"""
