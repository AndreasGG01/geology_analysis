import pandas as pd
from sqlalchemy import create_engine

#Config file
from config import setup_logger


logger = setup_logger('geology.log')
logger.info("Script started...")


# 1. Create the connection 'engine'
# Format: postgresql://[user]@localhost/[database_name]
engine = create_engine('postgresql://localhost/geo_practice')

# 2. Define your SQL query
query = "SELECT * FROM samples_v2"

# 3. Load the data into a Pandas DataFrame
try:
    df = pd.read_sql(query, engine)
    print("Success! Data loaded from SQL.")
    logger.info(f"Database connection successful. Loaded {len(df)} rows.")
    
    # 4. Show the first 5 rows and the column names
    print(df.head())
    print(f"\nColumns found: {df.columns.tolist()}")

except Exception as e:
    logger.error(f"Error connecting to database: {e}")
    print(f"Error connecting to database: {e}")
