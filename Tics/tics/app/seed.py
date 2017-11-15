'''from config import *
from datetime import datetime
import psycopg2

conn = psycopg2.connect("dbname=%s host=%s user=%s password=%s"%(database,host,user,password))
cur = conn.cursor()



sql="""
insert into habitacion (id, tipo) values
('0','pieza')
returning
id, tipo;
"""

cur.execute(sql)
conn.commit()
negocio = cur.fetchone()
print ("Insertamos en habitacion:" )
print(habitacion)


fecha=datetime.now()
sql ="""
insert into encendido (id_habitacion, fecha) values ('0', ('%s'))
returning
id_habitacion, fecha;
"""%(fecha)

cur.execute(sql)
conn.commit()
ventas = cur.fetchone()
print ("Insertamos en  encendido : ")
print (encendido)


fecha=datetime.now()
sql ="""
insert into apagado (id_habitacion, fecha) values ('0', ('%s'))
returning
id_habitacion, fecha;
"""%(fecha)

cur.execute(sql)
conn.commit()
ventas = cur.fetchone()
print ("Insertamos en  apagado : ")
print (apagado)



fecha=datetime.now()
sql ="""
insert into alerta (id_habitacion, fecha) values ('0', ('%s'))
returning
id_habitacion, fecha;
"""%(fecha)

cur.execute(sql)
conn.commit()
ventas = cur.fetchone()
print ("Insertamos en  alerta : ")
print (alerta)



conn.close()'''
