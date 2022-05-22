
import psycopg2




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

def readall():
    info = getatrib()
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        libros = []

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT * FROM LIBROS')

        # display the PostgreSQL database server version
        db_version = cur.fetchall()
        for row in db_version:
            libro = []
            libro.append(row[0])
            libro.append(row[1])
            libro.append(row[2])
            libro.append(row[3])
            libros.append(libro)

        print(libros)
        print(db_version)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

    return libros

def addone(id_cyclist,rider_name,weight,nationality,general_classification,time_trial,climbing,sprint,one_day_races):
    info = getatrib()
    conn = None
    try:
        # read connection parameters

        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        insertar= "insert into cyclists (id_cyclist,rider_name,weight,nationality,general_classification) VALUES (%s, %s, %s)"
        values=(id_cyclist,rider_name,weight,nationality,general_classification,time_trial,climbing,sprint,one_day_races)

        cur.execute(insertar,values)
        conn.commit()

        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def updateone(id):
    info = getatrib()
    conn = None
    try:
        # read connection parameters

        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        idstring = str(id)

        insertar= "UPDATE Libros SET NOMBRE_LIBRO = 'Alfred Schmidt', AUTOR_LIBRO= 'Frankfurt', DESCRIPCION_LIBRO= 'Frankfurt' WHERE ID_LIBROS = %s"
        values=(idstring)

        cur.execute(insertar,values)
        conn.commit()

        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def removeone(id):
    info = getatrib()
    conn = None
    try:
        # read connection parameters

        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        idstring = str(id)

        insertar= "DELETE FROM libros WHERE ID_LIBROS = %s"
        values=(idstring)

        cur.execute(insertar,values)
        conn.commit()

        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')




getatrib()

readall()

addone("mauro-finetto","Mauro  Finetto", "1.77", "62" kg   ,Italy,1002Climber,1199GC,229Time trial,1787Sprint,2156One day races)

updateone(7)

removeone(7)
