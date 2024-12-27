from src.etl.extract import read_csv_data

# Test the loader with date parsing
df = read_csv_data('sample_data.csv', date_columns=['order_date'])

# Display the first few rows and data info
print("\nFirst few rows:")
print(df.head())
print("\nDataframe info:")
print(df.info())