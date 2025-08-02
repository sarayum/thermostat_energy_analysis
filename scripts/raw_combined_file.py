import pandas as pd #used for handling and manipulating tabular data
import os # used to interact with os, like reading file names from directories

# input and output paths
# input_folder: Directory where raw files are stored
# output_file: path where the ombined file is stored


print("Current Working Directory:", os.getcwd())

input_folder = "./uncleaned_thermostat_data/"
output_file = "./data/raw/thermostat_combined.csv"

print("input folder:", input_folder)
# list all csv files
# This line creates a list of all files in the input folder that have the .csv extension

csv_files = [f for f in os.listdir(input_folder) if f.endswith(".csv") and not f.startswith("._")]

combined_raw = []

for file in csv_files:
    file_path = os.path.join(input_folder, file)
    print("file path:", file_path)
    
    # Read CSV, skip the first 4 rows to remove metadata
    df = pd.read_csv(file_path, skiprows=4, encoding='ISO-8859-1')
    
    
    combined_raw.append(df)

# Combine all raw data
raw_df = pd.concat(combined_raw, ignore_index=True)


# Save to combined raw file
raw_df.to_csv(output_file, index=False)


print(f" Combined raw data saved to: {output_file}")



