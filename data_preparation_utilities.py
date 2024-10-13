import pandas as pd
import zipfile

def read_csv_from_zip():
    # Path to the ZIP file
    zip_file_path = 'stock-market-prediction-and-sentimental-analysis.zip'

    # Open the ZIP file
    with zipfile.ZipFile(zip_file_path, 'r') as z:
        # List all files in the ZIP archive
        file_list = z.namelist()
        
        # Assuming there's only one CSV file in the ZIP archive
        csv_file_name1 = 'Combined_News_DJIA(train).csv'
        csv_file_name2 = 'DJIA_table(train).csv'
        csv_file_name3 = 'RedditNews(train).csv'
        csv_file_name4 = 'Test_Combined_News.csv'
        csv_file_name5 = 'Test_DJIA_Table.cvs'
        csv_file_name6 = 'Test_Redit_news.csv'
        csv_file_name7 = 'sample_submission.csv'
        
        # Read the CSV file into a pandas DataFrame
        with z.open(csv_file_name1) as f:
            df1 = pd.read_csv(f)
        with z.open(csv_file_name2) as f:
            df2 = pd.read_csv(f)
        with z.open(csv_file_name3) as f:
            df3 = pd.read_csv(f)
        with z.open(csv_file_name4) as f:
            df4 = pd.read_csv(f)
    return df1, df2, df3, df4