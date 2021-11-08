import psycopg2
import pandas as pd


class Loader:
    """
    This object is in charge of inserting the data into a staging area
    of the desired database. It manages the data schema changes by 
    creating new columns over the tables when needed. It's is important
    to note that this will only insert data that passed all the previous 
    checks and it will not update nor delete any data already stored in 
    the target database.
    """

    def load(self, df: pd.DataFrame):
        """
        [summary]
        """

        pass
