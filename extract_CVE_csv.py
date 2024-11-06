from numpy import extract
import pandas as pd
import os

def extract_csv_data(file_path):
    """
    Extracts data from Common Vulnerabilites & Exposure CSV file
    and returns it as a pandas DataFrame.
    
    Parameters: file_path(str) is path to CSV file to be extracted
    
    Returns: exracted data as pandas dataframe.
    """
    try:
        # Loads cve.csv file into DataFrame
        df = pd.read_csv(file_path)
        print(f"Data successfully extrracted from {file_path}")
        return df
    except Exception as e:
        print(f"Error Extracting data from {file_path}: {e}")

if __name__ == "__main__":
    file_path = r"C:\Users\a205722\OneDrive - REC Silicon, Inc\REC Work Notes\Personal Work\Python Work\Python_ThreatETLProject\data\cve.csv"
    print(f"File path: {file_path}") # print confirms path
    data = extract_csv_data(file_path)
    if data is not None:
        print(data.head()) # Display first few rows for verificaton
    else:
        print("Data not loaded.")