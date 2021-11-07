from reader import Reader
from schema_validator import SchemaValidator
from data_validator import DataValidator
from loader import Loader
from logger import Logger


class ETL:
    """
    [summary]
    """

    def __init__(self):
        self.reader = Reader()
        self.schema_validator = SchemaValidator()
        self.data_validator = DataValidator()
        self.loader = Loader()
        self.logger = Logger()

    def run_etl(self):
        """
        [summary]
        """

        self.reader.extract()
        self.schema_validator.check_schema()
        self.schema_validator.check_data_types()
        self.data_validator.run_expectations()
        self.loader.load()
