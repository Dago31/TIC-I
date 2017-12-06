
from datetime import datetime
import time
import serial
import psycopg2

conn = psycopg2.connect("dbname=tics1 user=tics1 password=1234 host = localhost")
cur = conn.cursor()

ser = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(3)
e = 0
while True:
    try:
        date = datetime.now()

        line1 = ser.readline()

        #line1 = line1.decode("utf-8")
        if line1[0]=="1":
            if e == 0:
                sql = """
                select fecha from encendido;
                """
                cur.execute(sql)
                enc = cur.fetchall()
                sql = """
                select fecha from apagado;
                """
                cur.execute(sql)
                apa = cur.fetchall()
                print(enc)
                print(apa)
                e = 1

            if line1[2] == "1":
                sql = """
                insert into alerta ( fecha) values ( ('%s'));
                """%( date)
                cur.execute(sql)
                conn.commit()
            

            else:
                if date.minute%2 == 0:
                    ser.write('5')
                else:
                    ser.write('2')
        else:
            e = 0
            if line1[1] == "1":
                sql = """
                insert into encendido (fecha) values (('%s'));
                """%(date)
                cur.execute(sql)
                conn.commit()
              

            if line1[1] == "0":
                sql = """
                insert into apagado (fecha) values (('%s'));
                """%(date)
                cur.execute(sql)
                conn.commit()
               


        print("l1",line1,date)



    except serial.SerialException:
        pass
