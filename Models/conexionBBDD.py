
import psycopg2

from Models.workpostgresql import getatrib


class Conexion:
    host = ''
    database = ''
    user = ''
    def __init__(self):
        pass

        self

    @staticmethod
    def getatrib():
        info=[]
        with open('../confBBDD.ini', 'r') as f:
            for line in f:
                p = line.split("=")
                if(len(p)==2):
                    p[1]=p[1].rstrip('\n')
                    info.append(p[1])
        print(info)
        return info

    def addone(nomlib,autor,description):
        info = getatrib()
        conn = None
        try:
            # read connection parameters

            conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
            cur = conn.cursor()
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            # execute a statement
            insertar= "insert into LIBROS (NOMBRE_LIBRO,AUTOR_LIBRO, DESCRIPCION_LIBRO) VALUES (%s, %s, %s)"
            values=(nomlib,autor,description)

            cur.execute(insertar,values)
            conn.commit()
