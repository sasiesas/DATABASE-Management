import psycopg2
from DbConfig import config 

def connect():
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        params =  config()

        print("Connecting to postgreSQL database")
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print(" Does the International box office of movies have an higher revenue than the Domestic box office on average?: ")
        cur.execute('select user_type, AVG(idv_score) from reviews GROUP BY user_type ')

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


