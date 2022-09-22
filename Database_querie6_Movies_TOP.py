import psycopg2
from DbConfig import config 
import pandas as pd

def connect():
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        params =  config()

        print("Connecting to postgreSQL database")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print(" Wich are the top 10 movies : ")
        cur.execute('SELECT Movie_ID, Title, Metascore FROM "Movies" ORDER BY Metascore DESC LIMIT 10;')

        print((cur.fetchall()))

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


