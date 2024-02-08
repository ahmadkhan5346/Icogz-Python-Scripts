import pandas as pd
import os
import glob

def process_folder(folder_path, output_path):
    for filename in glob.glob(os.path.join(folder_path, "*.xlsx")):
        # Read excel file and convert to dataframe
        df = pd.read_excel(filename)

        # Extract filename without extension and use it for output csv name
        basename = os.path.splitext(os.path.basename(filename))[0]

        # Create output path for the csv file
        output_filename = os.path.join(output_path, f"{basename}.csv")

        # Save dataframe to csv
        df.to_csv(output_filename, index=False)

    # Recursively process subfolders
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        if os.path.isdir(subfolder_path):
            output_subfolder_path = os.path.join(output_path, subfolder)
            os.makedirs(output_subfolder_path, exist_ok=True)
            process_folder(subfolder_path, output_subfolder_path)

# Set your input and output folder paths
input_folder_path = "/home/onkar/Downloads/Brand_mention-20231212T113413Z-001/Brand_mention"
output_folder_path = "/home/onkar/Downloads/cav_bfsi_data"

# Start processing the input folder
process_folder(input_folder_path, output_folder_path)