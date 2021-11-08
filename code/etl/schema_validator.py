import pandas as pd


class SchemaValidator:
    """
    This object is in charge of validating the schema of the file received with
    the expected schema. Given the requirement that the schema may change over time,
    proper checks were implemented with a certain level of flexibility.

    First, the Python module will check if the schema matches with the expected one
    if it's successful it will check the data types expected for each attribute, if
    something goes wrong at this stage the execution will stop and will log.

    If the schema does not match, it will stop the execution and will not run until
    a proper expected schema is passed that matches with the data received (this
    assumes that the schema may change, but it will not change that often).
    """

    def __init__(self, expected_schema: dict):
        self.expected_schema = expected_schema

    def check_schema(self, df: pd.DataFrame):
        """
        Check if the schema matches with the expected one, if something goes wrong at
        this stage the execution will stop and will log

        Args:
            df (pd.DataFrame): data

        Raises:
            Exception: if something went wrong it'll raise an exception
        """
        if (
            df.dtypes.apply(lambda x: x.name).to_dict().keys()
            != self.expected_schema.keys()
        ):
            # log: schema doesn't match
            raise Exception("The data schema doesn't match with the expected schema")

        # log: schema match

    def check_data_types(self, df: pd.DataFrame):
        """
        Check if the data types matches with the expected ones, if something goes wrong
        at this stage the execution will stop and will log

        Args:
            df (pd.DataFrame): data

        Raises:
            Exception: if something went wrong it'll raise an exception
        """

        if df.dtypes.apply(lambda x: x.name).to_dict() != self.expected_schema:
            # log: data types doesn't match
            raise Exception("The data types doesn't match with the expected schema")

        # log: data types match
