import pandas as pd

class CovidDataSummary:
    """A class to summarize and clean COVID-19 data."""

    def __init__(self, file_path):
        """
        Initialize CovidDataSummary object.

        Parameters:
        file_path (str): The file path to the dataset.
        """
        self.file_path = file_path
    
    def display_head(self):
        """
        Displays the first five rows of the data.
        
        Returns:
        None
        """
        display(self.data.head())
        
    def clean_data(dataframe):
        """Clean the COVID-19 dataset.

        Parameters:
        dataframe (pandas.DataFrame): The COVID-19 dataset.

        Returns:
        pandas.DataFrame: The cleaned dataset.
        """
        # Convert date to datetime format
        dataframe['date'] = pd.to_datetime(dataframe['date'], format='%Y%m%d')

        # Drop columns with a high percentage of missing values
        columns_to_drop = ['positiveTestsPeopleAntigen', 'totalTestsPeopleAntigen', 'positiveTestsAntigen',
                           'negativeTestsPeopleAntibody', 'positiveTestsPeopleAntibody', 'onVentilatorCumulative',
                           'negativeTestsAntibody', 'totalTestsAntigen', 'totalTestsPeopleAntibody', 'pending']
        dataframe.drop(columns=columns_to_drop, inplace=True)

        # Fill missing values for critical columns with median values
        critical_columns = ['positive', 'negative', 'hospitalizedCurrently', 'death', 'recovered']
        for column in critical_columns:
            dataframe[column].fillna(dataframe[column].median(), inplace=True)

        return dataframe

    @staticmethod
    def load_data(file_path):
        """Load the COVID-19 dataset.

        Parameters:
        file_path (str): The file path to the dataset.

        Returns:
        pandas.DataFrame: The loaded dataset.
        """
        return pd.read_csv(file_path)
