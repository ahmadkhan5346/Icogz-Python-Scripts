import psycopg2
from db_config import DB_CONFIG
import psycopg2.extras as extras

pg_connection = psycopg2.connect(
    host = DB_CONFIG['LOCAL']['DB_HOST'],
    database = DB_CONFIG['LOCAL']['DB_NAME'],
    user = DB_CONFIG['LOCAL']['DB_USERNAME'],
    password = DB_CONFIG['LOCAL']['DB_PASSWORD'],
    port = DB_CONFIG['LOCAL']['DB_PORT'],
)


def df_to_db(df, tables, columns, on_conflict_columns):
    tuples = [tuple(x) for x in df.to_numpy()]
    print(tuples)
    #  SQL query to execute
    if on_conflict_columns:
        query = "INSERT INTO %s(%s) VALUES %%S on conflict (%s) DO NOTHNG;"%(tables, columns, on_conflict_columns)
    else:
        query = "INSERT INTO %s(%s) VALUES %%s ;"%(tables, columns)

    try:
        pg_cursor = pg_connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) # type: ignore
        extras.execute_values(pg_cursor, query, tuples)
        # pg_connection.commit()
        print("Data inserted successfully")
        return True
    except Exception as e:
        print(f"Query Execution {str(e)}")
        return False