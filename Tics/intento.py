
from datetime import datetime
import time
import serial
import psycopg2

conn = psycopg2.connect("dbname=tics1 user=tics1 password=1234 host = localhost")
cur = conn.cursor()

ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(3)
e = 0
a = 0
w = 0
while True:
    try:
        date = datetime.now()

        line1 = ser.readline()

        line1 = line1.decode("utf-8")
        if line1[1] == "1":
            sql = """
            insert into alerta (id, fecha) values ((%s), ('%s'));
            """%(w, date)
            cur.execute(sql)
            conn.commit()
            w = w +1
        else:

            if line1[0] == "1":
                sql = """
                insert into encendido (id, fecha) values ((%s), ('%s'));
                """%(e, date)
                cur.execute(sql)
                conn.commit()
                e = e +1

            if line1[0] == "0":
                sql = """
                insert into apagado (id, fecha) values ((%s), ('%s'));
                """%(a, date)
                cur.execute(sql)
                conn.commit()
                a = a + 1


        print("l1",line1,date)



    except serial.SerialException:
        pass
