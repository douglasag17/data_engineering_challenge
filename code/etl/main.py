""" 
Example of how the module could be used
"""

from etl import ETL


file_path = "../../data.json"
expected_schema = {
    "event_type": "int64",
    "event_time": "datetime64[ns]",
    "data": "object",
    "processing_date": "object",
}
expectations = {"expect_column_to_exist": "data"}

etl = ETL(file_path, expected_schema, expectations)
etl.run_etl()
