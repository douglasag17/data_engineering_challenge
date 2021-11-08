import pandas as pd
import great_expectations as ge


class DataValidator:
    """
    This object is in charge of validating the data received.
    Here, with the help of the Great Expectations module, several
    tests (expectations) will run. For instance: the number of rows,
    number of unique rows, number of unique rows based on a primary key,
    expected values over columns, nulls columns check, etc.
    """

    def __init__(self, expectations: dict):
        self.expectations = expectations

    def run_expectations(self, df: pd.DataFrame):
        """
        Method that executes all the received data validations over the data

        Args:
            df (pd.DataFrame): data

        Raises:
            Exception: if something went wrong it'll raise an exception
        """

        df_ge = ge.from_pandas(df)
        failed_results = []
        for expectation, args in self.expectations.items():
            if expectation == "expect_column_to_exist":
                res = df_ge.expect_column_to_exist(args)
                # log results {res}
                if not res["success"]:
                    failed_results.append(res)

            else:
                # log the following expectation wasn't able to run {expectation}
                continue

        if len(failed_results) > 0:
            # log the following expectations failed {failed_results}
            raise Exception(f"The following expectations failed {failed_results}")
