import pytest
import pandas as pd
import os
from src.etl.extract import read_csv_data

def create_sample_csv():
    # Create a sample CSV file for testing
    data = {
        'id': [1, 2, 3],
        'name': ['John', 'Jane', 'Bob'],
        'date': ['2024-01-01', '2024-01-02', '2024-01-03']
    }
    df = pd.DataFrame(data)
    df.to_csv('test_data.csv', index=False)
    return 'test_data.csv'

def test_read_csv_data():
    # Create test file
    file_path = create_sample_csv()
    
    try:
        # Test basic reading
        df = read_csv_data(file_path)
        assert len(df) == 3
        assert list(df.columns) == ['id', 'name', 'date']
        
        # Test with date parsing
        df = read_csv_data(file_path, date_columns=['date'])
        assert pd.api.types.is_datetime64_any_dtype(df['date'])
        
        # Test with custom dtypes
        df = read_csv_data(file_path, dtypes={'id': int, 'name': str})
        assert df['id'].dtype == 'int64'
        assert df['name'].dtype == 'object'
        
    finally:
        # Cleanup test file
        if os.path.exists(file_path):
            os.remove(file_path)

def test_read_csv_data_errors():
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        read_csv_data('nonexistent.csv')