from db_utils import DBConnection
from utils import WorkingWithFiles


# db_connection = DBConnection(
#     database_name= "enbd", user_name="icogz_rnd", password="^sSDDfmz]i3Ld", host="216.48.178.148",
#     port="5432", db_type="postgresql", schema_name="public"
# )

db_connection = DBConnection(
    database_name= "enbd", user_name="postgres", password="postgres", host="127.0.0.1",
    port="5432", db_type="postgresql", schema_name="practice"
)

work_with_files = WorkingWithFiles("xlcsvdata")

# work_with_files.process_and_upload_data_to_file(
#     db_connection=db_connection, file_name_table_name_map_dict={"table_name":"facebooktable"},
#     column_to_exclude=["link_to_post"]
# )


work_with_files.process_and_upload_data_to_file(db_connection=db_connection, file_name_table_name_map_dict={"table_name":"social_listening_latest_mentions"})


# work_with_files.process_and_upload_data_to_file(db_connection=db_connection)
