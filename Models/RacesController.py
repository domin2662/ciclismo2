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


def addrace(id_race, duration, type_of_competition):
    info = getatrib()
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        insertar= "INSERT INTO public.races(id_race, duration, type_of_competition) VALUES (%s, %s, %s)"
        values=(id_race, duration, type_of_competition)
        cur.execute(insertar,values)
        conn.commit()
        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def add_one_race_result( id_race, id_cyclist, season, age, team_name, uci, finishing_time,rank):
    info = getatrib()
    conn = None
    try:
        # read connection parameters
        conn = psycopg2.connect(host=info[0], database=info[1], user=info[2], password=info[3])
        cur = conn.cursor()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        # execute a statement
        insertar= "INSERT INTO public.race_results( id_race, id_cyclist, season, age, team_name, uci, finishing_time,rank) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"
        values=(id_race, id_cyclist, season, age, team_name, uci, finishing_time,rank)
        cur.execute(insertar,values)
        conn.commit()
        # display the PostgreSQL database server version

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


