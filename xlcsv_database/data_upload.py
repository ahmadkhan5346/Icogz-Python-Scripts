from db_utils import DBConnection
from utils import WorkingWithFiles


db_connection = DBConnection(
    database_name= "practice", user_name="postgres", password="pgadmin", host="localhost",
    port="5433", db_type="postgresql", schema_name="employees"
)

work_with_files = WorkingWithFiles("xlcsvdata")

work_with_files.process_and_upload_data_to_file(
    db_connection=db_connection, file_name_table_name_map_dict={"table_name":"facebooktable"},
    column_to_exclude=["link_to_post"]
)


# work_with_files.process_and_upload_data_to_file(db_connection=db_connection, file_name_table_name_map_dict={"file":"twitter"})
