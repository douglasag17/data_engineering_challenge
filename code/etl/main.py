""" 
Example of how the module could be used
"""

from etl import ETL


file_path = "./code/etl/data/data.json"
expected_schema = {
    "event_type": "int64",
    "event_time": "datetime64[ns]",
    "data": "object",
    "processing_date": "object",
}
expectations = {"expect_column_to_exist": "data"}
db_credentials = {
    "DATABASE_HOST": "database",
    "POSTGRES_USER": "root",
    "POSTGRES_PASSWORD": "root",
    "POSTGRES_DB": "root",
}

etl = ETL(file_path, expected_schema, expectations, db_credentials)
etl.run_etl()
