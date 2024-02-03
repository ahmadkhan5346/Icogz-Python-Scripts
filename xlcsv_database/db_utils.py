import psycopg2
import logging
import psycopg2.extras
import traceback



class DBConnection:
    connection = None
    database_name = None
    user_name = None
    password = None
    host = None
    port = None
    db_type = None

    def __init__(self, database_name,  user_name, password, host, port, db_type, schema_name) -> None:
        self.database_name = database_name
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port
        self.db_type = db_type
        self.schema_name = schema_name

    def __enter__(self):
        self.__create_db_connection()

    def __exit__(self, *args):
        self.close()

    def close_connection(self):
        if not self.connection.closed:
            self.connection.close()
            self.connection = None

    def close(self):
        self.close_connection()
                
    def __create_db_connection(self):
        if not self.connection or self.connection.closed:
            try:
                if self.db_type == "postgresql":
                    self.connection = psycopg2.connect(
                        database=self.database_name,
                        user=self.user_name,
                        password=self.password,
                        host=self.host,
                        port=self.port,
                        options=f"-c search_path={self.schema_name}"
                    )
                    self.connection.autocommit = True
                else:
                    print("Does not support except postgresql database")
            except Exception as e:
                print(f"Error establishing database connection: {e}")
            # Handle the exception as needed (e.g., logging, raising, etc.)
                
    def create_table(self, table_name, columns:list[dict] | list[str]):
        table_name = table_name.replace('-', '_')
        print('createTable=================>', table_name)
        # print(columns)
        self.__create_db_connection()

        column_string = ""
        if columns:
            value_type = "dict" if isinstance(columns[0], dict) else "str"
            for column in columns:
                column_type = "text" if value_type == "str" else column
                column_name = column if value_type == 'str' else column

                column_string += f"{column_name} {column_type}, "
            column_string = column_string[:-2]

            with self.connection.cursor() as cursor:
                cursor.execute("set search_path to '%s'" % self.schema_name)
                create_table_query = f"""
                CREATE TABLE {self.schema_name}.{table_name} (
                {column_string}
                )
                """
                print(create_table_query)
                cursor.execute(create_table_query)
                cursor.close()
                return True
        return False
    

    def execute_bulk_query(self, table_name, data, df, constraint=None):
        """_summary_

        Args:
            table_name (string): _description_
            data (list): list of dictionary to be inserted.
            constraint (string, optional): comma separated constraint string. Defaults to None.
        """
        self.__create_db_connection()
        print('============tablename===========', table_name)
        print('============dataaaa===========', data)
        print('============dfffff===========', df)

        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            
            try:
                columns = [column.replace(".", "_") for column in data[0].keys()]
                query = f'''
                INSERT INTO {self.schema_name}.{table_name} ({','.join(columns)})
                VALUES %s
                '''
                if constraint:
                    query += f'''ON CONFLICT ({constraint}) DO NOTHING'''
                    print(query)
                values = [[value for value in each_data.values()] for each_data in data]
                # print("test for query=======",query)
                # print("==test for values===",values)
                psycopg2.extras.execute_values(cursor, query, values)
                # psycopg2.extras.execute_values(cursor, query, values, template=None, page_size=100)
                self.connection.commit()
                print(f'Inserting {len(df)} rows into {table_name}')

            except Exception as e:
                logging.error(f"Query Execution {str(e)} :: Query: {query}")

                print(traceback.format_exc())
                print(str(e))
                ...
                
     
                
                
    def execute_bulk_query_update(self, table_name, data, df, constraint=None):

        self.__create_db_connection()

        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            
            try:
                columns = [column.replace(".", "_") for column in data[0].keys()]
                for i in data:
                    print('iiiiiiiiiiiiiii',i)
                    
                    query = f'''
                    UPDATE {self.schema_name}.{table_name}
                    SET sentiment = %s,
                    classification = %s,
                    WHERE id = '{i['id']}'
                    '''
                    if constraint:
                        query += f'''ON CONFLICT ({constraint}) DO NOTHING'''
                        print(query)
                    update_values = [[i['sentiment']],[i['classification']]]
                    print("update query=======",query)
                    print("==update values===",update_values)
                    # psycopg2.extras.execute_values(cursor, query, update_values)
                    psycopg2.extras.execute_values(cursor, query, update_values, template=None, page_size=100)
                # self.connection.commit()
                print(f'Inserting {len(df)} rows into {table_name}')

            except Exception as e:
                logging.error(f"Query Execution {str(e)} :: Query: {query}")

                print(traceback.format_exc())
                print(str(e))
                ...
            