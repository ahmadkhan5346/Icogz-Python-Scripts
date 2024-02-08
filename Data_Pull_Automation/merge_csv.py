import os
import pandas as pd


def context_file_csv_maker(common_keyword_in_file):
    base_directory_to_read = '/home/onkar/Downloads/csv_bfsi_data'
    list_of_all_directories = [x[0] for x in os.walk(base_directory_to_read)][1:]
    final_df = pd.DataFrame()
    file_count = 0
    print(os.sep)
    data_not_available_for_particular_candidate_list = []
    print('Initial Size', final_df.size)
    print('Directory List ', len(list_of_all_directories))
    print('list_of_all_directories', list_of_all_directories)
    if common_keyword_in_file == '-All Mentions-':
        csv_headers = ["data_date","mentions"]
    elif common_keyword_in_file == '-Interactions-':
        csv_headers = ["data_date","engagement"]
    elif common_keyword_in_file == '-Sources-':
        csv_headers = ['platform','mentions','percentage']
    elif common_keyword_in_file == '-Sentiment-':
        csv_headers = ["data_date","positive","negative","neutral"]
    elif common_keyword_in_file == '-Reach-':
        csv_headers = ["data_date","views"]
    
    
    for directory in list_of_all_directories:
        # print(directory)
        files = os.listdir(directory)
        file_read = None
        for file in files:
            if common_keyword_in_file in file:
                file_count += 1
                file_read = True
                df = pd.read_csv(directory + os.sep + file)
                if df.empty:
                    print('Data empty for ', directory)

                df['candidate_name'] = directory.split(os.sep)[1]
                if final_df.empty:
                    final_df = df
                else:
                    final_df = final_df._append(df)

        if not file_read:
            data_not_available_for_particular_candidate_list.append(directory)

    final_df.rename(columns={'CONTEXT': 'context', 'USES': 'use_count', 'HASHTAG': 'hashtag'}, inplace=True)
    print('File read count', file_count)
    print('Data not available for')
    print(data_not_available_for_particular_candidate_list)
    print('Count', len(data_not_available_for_particular_candidate_list))
    final_df.to_csv(f'Final List of MLA {common_keyword_in_file} Data.csv', index=False)


context_file_csv_maker(common_keyword_in_file = 'Related Hashtags')