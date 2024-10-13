from data_preparation_utilities import read_csv_from_zip

Combined_News_DJIA, DJIA_table, RedditNews, Test_dates = read_csv_from_zip()

print(RedditNews.shape)
print(DJIA_table.shape) 
print(Combined_News_DJIA.columns)