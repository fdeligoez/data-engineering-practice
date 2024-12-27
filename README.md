# Data Engineering Practice Repository

This repository is designed for practicing data engineering concepts and version control.

## Project Structure

```
├── src/
│   └── etl/
│       ├── extract.py    # Data extraction functions
│       ├── transform.py  # Data transformation functions
│       └── load.py       # Data loading functions
├── tests/                # Unit tests
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/fdeligoez/data-engineering-practice.git
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Practice Scenarios

1. ETL Pipeline Development
   - Implement data extraction from various sources
   - Add data transformation logic
   - Implement data loading to different destinations

2. Version Control Practice
   - Create feature branches
   - Make changes and commit them
   - Create pull requests
   - Handle merge conflicts

3. Testing
   - Write unit tests for ETL functions
   - Run tests and fix failures

## Best Practices

- Always create a new branch for new features
- Write clear commit messages
- Update tests when adding new features
- Document your code
- Review your changes before committing