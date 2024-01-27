import os
from db_utils import DBConnection
import pandas as pd
import re





class WorkingWithFiles:
    directory_name = None
    
    def __init__(self, directory_name) -> None:
        self.directory_name = directory_name

    def read_directory_and_return_list_of_files(self):
        return os.listdir(self.directory_name)
    
    def get_df_for_file(self, file_name):
        file_name_type_tuple = os.path.splitext(file_name)
        method_for_read = None
        if file_name_type_tuple[1] == ".csv":
            method_for_read = getattr(pd, "read_csv")
            
        elif file_name_type_tuple[1] in [".xlsx", ".xls"]:
            method_for_read = getattr(pd, "read_excel")

        if method_for_read:
            df = method_for_read(self.directory_name + os.sep + file_name   )
            return df
        else:
            return None
        

    @staticmethod
    def df_columns_formatting(df:pd.DataFrame()):
        # print(df.info())

        df.columns = df.columns.str.strip()
        # print(df.columns)
        df.columns = df.columns.str.lower()
        # print(df.columns)

        # replaces single or multiple spaces with single spaces
        df.rename(columns=lambda x: re.sub(r'\s+', ' ', x), inplace=True)
        # Remove colon
        df.rename(columns=lambda x: x.replace(":", ""), inplace=True)

        df.rename(columns=lambda s: s.replace("(", ""), inplace=True)
        df.rename(columns=lambda s: s.replace(")", ""), inplace=True)

        # replaces single or mulitple spaces with single underscore
        df.rename(columns=lambda x: re.sub(r'\s+', '_', x), inplace=True)

        # replace hyphen with underscores
        df.rename(columns=lambda s: re.sub(r'\-', "_", s), inplace=True)

        # replaces slash(with 0 or multiple space before or after) with underscores
        df.rename(columns=lambda x: re.sub(r'\s*/\s*', '_', x), inplace=True)

        df.rename(columns={'\ufeffinter_actions': 'inter_actions'}, inplace=True)
        
        return df
    

    @staticmethod
    def create_table_and_upload_data_using_df(db_connection:DBConnection, file_name:str, table_name:str, df):
        """
        This function creates a table and upload data from the given DataFrame

        """
        # print(f'Creating table {table_name} for file {file_name}')
        # db_connection.create_table(table_name, list(df.columns))

        all_data = df.to_dict(orient='records')
        # print(f'Inserting {len(df)} rows into {table_name}')

        db_connection.execute_bulk_query(table_name, all_data, df, constraint=None)



    def process_and_upload_data_to_file(
            self, db_connection:DBConnection, file_name_table_name_map_dict:dict | None=None,
            column_to_exclude:list[str] | None=None
    ):
        # record_count = 0
        for file in self.read_directory_and_return_list_of_files():
            table_name = file if not file_name_table_name_map_dict else file_name_table_name_map_dict.get("table_name")
            df = self.get_df_for_file(file)

            # Change Column Names to match the formatting supported by database.
            df = self.df_columns_formatting(df)

            if column_to_exclude:
                for column in column_to_exclude:
                    df.drop(column, axis=1, inplace=True)
            # print('df========64========>', df.info())

            self.create_table_and_upload_data_using_df(db_connection, file, table_name, df)

            # record_count += len(df)

        # print(f"Total {len(df)}. Record Inserted")