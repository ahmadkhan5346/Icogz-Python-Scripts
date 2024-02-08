import pandas as pd
import os

def merge_excel_with_filename(folder_path):
  """
  Merges all excel files in a folder and adds a "filename" column with the original file names.

  Args:
    folder_path: The path to the folder containing excel files.

  Returns:
    A pandas DataFrame with merged data and a "filename" column.
  """

  all_dataframes = []
  for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
      filepath = os.path.join(folder_path, filename)
      df = pd.read_excel(filepath)
    #   df["filename"] = filename
      df['video_id'] = filename.split("youtube_comments_")[1].split(".xlsx")[0]
      all_dataframes.append(df)

  # Concatenate all dataframes
  merged_df = pd.concat(all_dataframes, ignore_index=True)

  return merged_df

# Example usage
folder_path = "/home/onkar/Downloads/youtube_comment_data"
merged_df = merge_excel_with_filename(folder_path)

# Do something with the merged dataframe
print(merged_df)
merged_df.to_excel('YT Comment Data Data.xlsx', index=False)