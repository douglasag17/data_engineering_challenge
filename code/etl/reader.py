import pandas as pd


class Reader:
    """
    This object is in charge of extracting the data from any file received.
    The correct formatting of the file is checked here, for instance: if a JSON
    file is received the code will check and validate that the file is a valid JSON.
    Finally, if everything goes well, it will read it successfully and will be stored
    in a Pandas DataFrame, otherwise, the execution will fail and the pipeline will stop.
    Remember that everything will be logged using the Logger object.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract(self) -> pd.DataFrame:
        """
        Extract the data of the received file

        Returns:
            pd.DataFrame: pandas dataframe with the data loaded in it

        Raises:
            Exception: if something went wrong it'll raise an exception
        """

        try:
            df = pd.read_json(
                self.file_path,
                convert_dates=True,
                keep_default_dates=True,
                encoding="utf-8",
            )
            # log the file was read successfully

        except:
            # log couldn't read the file
            raise Exception("Couldn't read the file")

        return df
