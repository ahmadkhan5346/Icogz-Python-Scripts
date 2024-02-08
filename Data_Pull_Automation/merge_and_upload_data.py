import os
import pandas as pd
from utils import df_to_db,get_brand_mapping_data_sl
exception_files = []
relative_path = ''
completed_folder_name = 'completed/social_listening/all_mentions'
brand_Data = get_brand_mapping_data_sl()
data_not_available_for_particular_candidate_list = []
def context_file_csv_maker(common_keyword_in_file):
    # base_directory_to_read = '/home/onkar/Downloads/Dubai Brands Social Listening Data-Ishani-196brands'
    base_directory_to_read = '/home/onkar/Downloads/csv_bfsi_data' 
    # base_directory_to_read = '/home/onkar/Downloads/banks data'
    # common_keyword_in_file = '-Related Hashtags-'
    list_of_all_directories = [x[0] for x in os.walk(base_directory_to_read)][1:]
    final_df = pd.DataFrame()
    file_count = 0
    print(os.sep)
    # data_not_available_for_particular_candidate_list = []
    # all mentions
    if common_keyword_in_file == '-All Mentions-':
        csv_headers = ["data_date","mentions"]
        for directory in list_of_all_directories:
            # print(directory)
            files = os.listdir(directory)
            file_read = None
            for file_name in files:
                if common_keyword_in_file in file_name:
                    file_count += 1
                    file_read = True
                    df = pd.read_csv(directory + os.sep + file_name,parse_dates=['DATE'],dayfirst= True)
                    if df.empty:
                        print('Data empty for ', directory)
                    df.columns = csv_headers
                    file_brand_name = file_name.split("-All Mentions")[0]
                    file_key_name = 'social_listening_name'
                    exp_dict = next(filter(lambda d: d.get(file_key_name) == file_brand_name, brand_Data), None)
                    if exp_dict:
                        df['brand_name'] =  exp_dict.get('brand_name')
                        df['brand_id'] = exp_dict.get('brand')
                    else:
                        df['brand_name'] = file_brand_name
                        df['brand_id'] = ""
                    if final_df.empty:
                        final_df = df
                    else:
                        final_df = final_df._append(df)

            if not file_read:
                data_not_available_for_particular_candidate_list.append(directory)
        # print("final_df--------------------------\n", final_df)
        df_col_str = """data_date,mentions,brand_name,brand_id"""
        on_conflict_column = """data_date,brand_id"""
        output = df_to_db(final_df,'social_listening_all_mentions',df_col_str,on_conflict_column)
        if output is True:
            print("===================df is done==============")
        else:
            pass
        final_df.to_csv(f'Final Indian All Mentions New {common_keyword_in_file} Data.csv', index=False, sep='\t')
    # interactions
    elif common_keyword_in_file == '-Interactions-':
        csv_headers = ["data_date","engagement"]
        for directory in list_of_all_directories:
            # print(directory)
            files = os.listdir(directory)
            file_read = None
            for file_name in files:
                if common_keyword_in_file in file_name:
                    file_count += 1
                    file_read = True
                    df = pd.read_csv(directory + os.sep + file_name,parse_dates=['DATE'],dayfirst= True)
                    if df.empty:
                        print('Data empty for ', directory)
                    df.columns = csv_headers
                    file_brand_name = file_name.split("-Interactions")[0]
                    file_key_name = 'social_listening_name'
                    exp_dict = next(filter(lambda d: d.get(file_key_name) == file_brand_name, brand_Data), None)
                    if exp_dict:
                        df['brand_name'] =  exp_dict.get('brand_name')
                        df['brand_id'] = exp_dict.get('brand')
                    else:
                        df['brand_name'] = file_brand_name
                        df['brand_id'] = ""
                    if final_df.empty:
                        final_df = df
                    else:
                        final_df = final_df._append(df)

            if not file_read:
                data_not_available_for_particular_candidate_list.append(directory)
        # print("final_df--------------------------\n", final_df)
        df_col_str = """data_date,engagement,brand_name,brand_id"""
        on_conflict_column = """data_date,brand_id"""
        output = df_to_db(final_df,'social_listening_interactions',df_col_str,on_conflict_column)
        if output is True:
            print("===================df is done==============")
        else:
            pass
    
        final_df.to_csv(f'Final Indian All New {common_keyword_in_file} Data.csv', index=False, sep='\t')
    # mentions platform
    elif common_keyword_in_file == '-Sources-':
        csv_headers = ['platform','mentions','percentage']
        for directory in list_of_all_directories:
            # print(directory)
            files = os.listdir(directory)
            file_read = None
            for file_name in files:
                if common_keyword_in_file in file_name:
                    file_count += 1
                    file_read = True
                    df = pd.read_csv(directory + os.sep + file_name)
                    if df.empty:
                        print('Data empty for ', directory)
                    df.columns = csv_headers
                    file_brand_name = file_name.split("-Reach")[0]
                    file_key_name = 'social_listening_name'
                    exp_dict = next(filter(lambda d: d.get(file_key_name) == file_brand_name, brand_Data), None)
                    if exp_dict:
                        df['brand_name'] =  exp_dict.get('brand_name')
                        df['brand_id'] = exp_dict.get('brand')
                    else:
                        df['brand_name'] = file_brand_name
                        df['brand_id'] = ""
                    if final_df.empty:
                        final_df = df
                    else:
                        final_df = final_df._append(df)

            if not file_read:
                data_not_available_for_particular_candidate_list.append(directory)
        print("final_df--------------------------\n", final_df)
        df_col_str = """platform,mentions,percentage,brand_name,brand_id"""
        on_conflict_column = """platform,brand_id"""
        output = df_to_db(final_df,'social_listening_reach',df_col_str,on_conflict_column)
        if output is True:
            print("===================df is done==============")
        else:
            pass
    
        final_df.to_csv(f'Final Indian All New {common_keyword_in_file} Data.csv', index=False, sep='\t')
    # sentiment
    elif common_keyword_in_file == '-Sentiment-':
        csv_headers = ["data_date","positive","negative","neutral"]
        for directory in list_of_all_directories:
            # print(directory)
            files = os.listdir(directory)
            file_read = None
            for file_name in files:
                if common_keyword_in_file in file_name:
                    file_count += 1
                    file_read = True
                    df = pd.read_csv(directory + os.sep + file_name)
                    if df.empty:
                        print('Data empty for ', directory)
                    df.columns = csv_headers
                    file_brand_name = file_name.split("-Sentiment")[0]
                    file_key_name = 'social_listening_name'
                    exp_dict = next(filter(lambda d: d.get(file_key_name) == file_brand_name, brand_Data), None)
                    if exp_dict:
                        df['brand_name'] =  exp_dict.get('brand_name')
                        df['brand_id'] = exp_dict.get('brand')
                    else:
                        df['brand_name'] = file_brand_name
                        df['brand_id'] = ""
                    if final_df.empty:
                        final_df = df
                    else:
                        final_df = final_df._append(df)

            if not file_read:
                data_not_available_for_particular_candidate_list.append(directory)
        # print("final_df--------------------------\n", final_df)
        final_df.fillna(0,inplace = True)
        print("final_df--------------------------\n", final_df)
        df_col_str = """data_date,positive,negative,neutral,brand_name,brand_id"""
        on_conflict_column = """data_date,brand_id"""
        output = df_to_db(final_df,'social_listening_mentions_sentiments',df_col_str,on_conflict_column)
        if output is True:
            print("===================df is done==============")
        else:
            pass
        

        final_df.to_csv(f'Final Indian All New {common_keyword_in_file} Data.csv', index=False, sep='\t')

    # reach
    elif common_keyword_in_file == '-Reach-':
        csv_headers = ["data_date","views"]
        for directory in list_of_all_directories:
            # print(directory)
            files = os.listdir(directory)
            file_read = None
            for file_name in files:
                if common_keyword_in_file in file_name:
                    file_count += 1
                    file_read = True
                    df = pd.read_csv(directory + os.sep + file_name,parse_dates=['DATE'],dayfirst= True)
                    if df.empty:
                        print('Data empty for ', directory)
                    df.columns = csv_headers
                    file_brand_name = file_name.split("-Reach")[0]
                    file_key_name = 'social_listening_name'
                    exp_dict = next(filter(lambda d: d.get(file_key_name) == file_brand_name, brand_Data), None)
                    if exp_dict:
                        df['brand_name'] =  exp_dict.get('brand_name')
                        df['brand_id'] = exp_dict.get('brand')
                    else:
                        df['brand_name'] = file_brand_name
                        df['brand_id'] = ""
                    if final_df.empty:
                        final_df = df
                    else:
                        final_df = final_df._append(df)

            # if not file_read:
            #     data_not_available_for_particular_candidate_list.append(directory)
        # print("final_df--------------------------\n", final_df)
        final_df.fillna(0,inplace = True)
        print("final_df--------------------------\n", final_df)
        df_col_str = """data_date,views,brand_name,brand_id"""
        on_conflict_column = """data_date,brand_id"""
        output = df_to_db(final_df,'social_listening_reach',df_col_str,on_conflict_column)
        if output is True:
            print("===================df is done==============")
        else:
            pass
        

        final_df.to_csv(f'Final Indian All New {common_keyword_in_file} Data.csv', index=False, sep='\t')
    # social_listening_related_hashtag
    elif common_keyword_in_file == '-Related Hashtags-':
        csv_headers = ["hashtag","uses"]
        for directory in list_of_all_directories:
            # print(directory)
            files = os.listdir(directory)
            file_read = None
            for file_name in files:
                if common_keyword_in_file in file_name:
                    file_count += 1
                    file_read = True
                    df = pd.read_csv(directory + os.sep + file_name)
                    if df.empty:
                        print('Data empty for ', directory)
                    df.columns = csv_headers
                    file_brand_name = file_name.split("-Related Hashtags")[0]
                    file_key_name = 'social_listening_name'
                    exp_dict = next(filter(lambda d: d.get(file_key_name) == file_brand_name, brand_Data), None)
                    if exp_dict:
                        df['brand_name'] =  exp_dict.get('brand_name')
                        df['brand_id'] = exp_dict.get('brand')
                    else:
                        df['brand_name'] = file_brand_name
                        df['brand_id'] = ""
                    if final_df.empty:
                        final_df = df
                    else:
                        final_df = final_df._append(df)

            # if not file_read:
            #     data_not_available_for_particular_candidate_list.append(directory)
        # print("final_df--------------------------\n", final_df)
        final_df.fillna(0,inplace = True)
        print("final_df--------------------------\n", final_df)
        df_col_str = """hashtag,uses,brand_name,brand_id"""
        on_conflict_column = """hashtag,brand_id"""
        output = df_to_db(final_df,'social_listening_related_hashtag',df_col_str,on_conflict_column)
        if output is True:
            print("===================df is done==============")
        else:
            pass
        

        final_df.to_csv(f'Final Indian All New {common_keyword_in_file} Data.csv', index=False, sep='\t')
    
    print(data_not_available_for_particular_candidate_list)

common_keyword_list = ['-All Mentions-','-Interactions-','-Sources-','-Sentiment-','-Reach-']
for keyword in common_keyword_list:
    context_file_csv_maker(keyword)
# with open('exception_file.csv', 'w') as f:
#     # Create a CSV writer object that will write to the file 'f'
#     csv_writer = csv.writer(f)
    
#     # Write the field names (column headers) to the first row of the CSV file
#     csv_writer.writerow(fields)
    
#     # Write all of the rows of data to the CSV file
#     csv_writer.writerows(rows)

# create a dictionary with the three lists
exception_dict = {'File Name': data_not_available_for_particular_candidate_list}  
       
# create a Pandas DataFrame from the dictionary
df = pd.DataFrame(exception_dict) 
    
# write the DataFrame to a CSV file
df.to_csv('exception_file.csv') 