import pandas as pd
from typing import Optional, Dict, Any, List, Tuple
from datetime import datetime

class DataValidationError(Exception):
    """Custom exception for data validation errors"""
    pass

def validate_data(df: pd.DataFrame, rules: Dict[str, Dict]) -> Tuple[bool, List[str]]:
    """
    Validate dataframe against a set of rules
    
    Args:
        df: DataFrame to validate
        rules: Dictionary of validation rules
        
    Returns:
        Tuple of (is_valid, list of error messages)
    """
    errors = []
    
    for column, rule in rules.items():
        if column not in df.columns:
            errors.append(f"Required column '{column}' is missing")
            continue
            
        # Check data type
        if 'dtype' in rule:
            if not df[column].dtype == rule['dtype']:
                errors.append(f"Column '{column}' should be of type {rule['dtype']}")
                
        # Check for nulls if required
        if rule.get('required', False) and df[column].isnull().any():
            errors.append(f"Column '{column}' contains null values")
            
        # Check numeric range
        if 'min' in rule and df[column].min() < rule['min']:
            errors.append(f"Column '{column}' contains values below minimum {rule['min']}")
        if 'max' in rule and df[column].max() > rule['max']:
            errors.append(f"Column '{column}' contains values above maximum {rule['max']}")
            
    return len(errors) == 0, errors

def read_csv_data(
    file_path: str,
    date_columns: Optional[List[str]] = None,
    dtypes: Optional[Dict[str, Any]] = None,
    validation_rules: Optional[Dict[str, Dict]] = None
) -> pd.DataFrame:
    """
    Read data from CSV file with validation and basic statistics
    
    Args:
        file_path: Path to the CSV file
        date_columns: List of column names to parse as dates
        dtypes: Dictionary of column data types
        validation_rules: Dictionary of validation rules
    
    Returns:
        pandas.DataFrame: Loaded and validated data
    """
    try:
        # Read CSV
        df = pd.read_csv(
            file_path,
            parse_dates=date_columns if date_columns else False,
            dtype=dtypes if dtypes else None
        )
        
        # Basic validation
        if df.empty:
            raise DataValidationError("The CSV file is empty")
            
        # Remove any completely empty rows or columns
        df = df.dropna(how='all').dropna(axis=1, how='all')
        
        # Apply validation rules if provided
        if validation_rules:
            is_valid, errors = validate_data(df, validation_rules)
            if not is_valid:
                raise DataValidationError("\n".join(errors))
        
        # Print basic statistics
        print(f"\nData Summary:")
        print(f"Total rows: {len(df)}")
        print(f"Total columns: {len(df.columns)}")
        print(f"Memory usage: {df.memory_usage().sum() / 1024:.2f} KB")
        
        if date_columns:
            for date_col in date_columns:
                if date_col in df.columns:
                    print(f"\nDate range for {date_col}:")
                    print(f"From: {df[date_col].min()}")
                    print(f"To: {df[date_col].max()}")
        
        return df
        
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found at: {file_path}")
    except pd.errors.EmptyDataError:
        raise DataValidationError("The CSV file is empty")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")