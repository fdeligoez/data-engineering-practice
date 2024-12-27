import pandas as pd
from typing import Optional, Dict, Any

def read_csv_data(
    file_path: str,
    date_columns: Optional[list] = None,
    dtypes: Optional[Dict[str, Any]] = None
) -> pd.DataFrame:
    """
    Read data from a CSV file with error handling and basic validations
    
    Args:
        file_path: Path to the CSV file
        date_columns: List of column names to parse as dates
        dtypes: Dictionary of column data types
    
    Returns:
        pandas.DataFrame: Loaded and validated data
        
    Raises:
        FileNotFoundError: If the CSV file doesn't exist
        pd.errors.EmptyDataError: If the CSV file is empty
    """
    try:
        # Read CSV with provided parameters
        df = pd.read_csv(
            file_path,
            parse_dates=date_columns if date_columns else False,
            dtype=dtypes if dtypes else None
        )
        
        # Basic validation
        if df.empty:
            raise pd.errors.EmptyDataError("The CSV file is empty")
            
        # Remove any completely empty rows or columns
        df = df.dropna(how='all').dropna(axis=1, how='all')
        
        return df
        
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at: {file_path}")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError("The CSV file is empty")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")