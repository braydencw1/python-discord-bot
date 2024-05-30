import psycopg2, os
from dotenv import load_dotenv
load_dotenv()
def dbQuery(table):
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_DB"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS")
        )
        cursor = connection.cursor()
        # print("Connected to the database")

        try:
            cursor.execute(f"SELECT * FROM {table}")
            records = cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print(f"Error executing the query: {error}")
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()
                print("Database connection closed")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to the database: {error}")
    return records

