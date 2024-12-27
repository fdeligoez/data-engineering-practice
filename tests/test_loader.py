import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from src.etl.extract import read_csv_data

# Define validation rules
validation_rules = {
    'order_id': {
        'dtype': 'int64',
        'required': True,
        'min': 1
    },
    'customer_id': {
        'dtype': 'int64',
        'required': True,
        'min': 100
    },
    'amount': {
        'dtype': 'float64',
        'required': True,
        'min': 0
    }
}

# Test the loader with validation
df = read_csv_data(
    'sample_data.csv',
    date_columns=['order_date'],
    validation_rules=validation_rules
)

# Show some basic analysis
print("\nCustomer Statistics:")
print(df.groupby('customer_id')['amount'].agg(['count', 'sum', 'mean']))