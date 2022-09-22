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

        print(" What production budget do the best rated movies have? ")
        cur.execute('SELECT "Movies".Title, "Movies".Metascore, Sale.production_budget FROM "Movies" INNER JOIN Sale ON sale.movie_id = "Movies".Movie_ID WHERE Sale.production_budget IS NOT NULL ORDER BY Metascore DESC LIMIT 10;')
        

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


