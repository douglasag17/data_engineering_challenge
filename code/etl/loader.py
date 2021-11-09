import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import json


class Loader:
    """
    This object is in charge of inserting the data into a staging area
    of the desired database. It manages the data schema changes by
    creating new columns over the tables when needed. It's is important
    to note that this will only insert data that passed all the previous
    checks and it will not update nor delete any data already stored in
    the target database.
    """

    def __init__(self, db_credentials: dict):
        self.db_credentials = db_credentials

    def load(self, df: pd.DataFrame):
        """
        Method to load the data coming from a pandas dataframe into
        a table in postgres

        Args:
            df (pd.DataFrame): data
        """

        user = self.db_credentials["POSTGRES_USER"]
        password = self.db_credentials["POSTGRES_PASSWORD"]
        db = self.db_credentials["POSTGRES_DB"]
        conn_string = f"postgresql://{user}:{password}@{self.db_credentials['DATABASE_HOST']}:5432/{db}"

        try:
            db = create_engine(conn_string)
            conn = db.connect()
            # log: connection with the db established
        except:
            # log: Couldn't espablished connection with DB
            raise Exception("Couldn't espablished connection with DB")

        df["data"] = df["data"].apply(json.dumps)
        df.to_sql("data", con=conn, if_exists="replace", index=False)
        # log:data has been uploaded succesfully
