from reader import Reader
from schema_validator import SchemaValidator
from data_validator import DataValidator
from loader import Loader
from logger import Logger


class ETL:
    """
    The main object is an ETL Class, which runs the entire data pipeline and
    uses other classes to leverage its implementations, such as reading any
    file, running schema and data validations over that file, loading that
    data into a proper database, and monitoring the whole flow of the pipeline.
    """

    def __init__(
        self,
        file_path: str,
        expected_schema: dict,
        expectations: dict,
        db_credentials: dict,
    ):
        """
        Args:
            file_path (str): relative path to the file to read
            expected_schema (dict): pandas data types expected
                {object, int64, float64, datetime64[ns], bool}
            expectations (dict): great expectations checks that will run
            db_credentials (dict): database cerdentials
        """

        self.reader = Reader(file_path)
        self.schema_validator = SchemaValidator(expected_schema)
        self.data_validator = DataValidator(expectations)
        self.loader = Loader(db_credentials)
        self.logger = Logger()

    def run_etl(self):
        """
        Main method that runs the entire data pipeline
        """

        # log initiating read of the file
        df = self.reader.extract()
        # log initiating check of the schema
        self.schema_validator.check_schema(df)
        # log initiating check of the data types
        self.schema_validator.check_data_types(df)
        # log initiating execution of data validations
        self.data_validator.run_expectations(df)
        # log initiating load of the data to the DB
        self.loader.load(df)
        # log the ETL executed succesfully

        print(df.head(5))
        print("finished!")
