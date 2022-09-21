import psycopg2
import pandas as pd
from DbConfig import config 

def connect():
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        params =  config()

        print("Connecting to postgreSQL database")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print("How many movies are there in Movie database ? :")
        cur.execute('select * from "Movies"')

        print(len((cur.fetchall())))

        # movie_data = cur.fetchone()
        # print(movie_data)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database Connection is now closed.')

if __name__ == '__main__':
    connect()
