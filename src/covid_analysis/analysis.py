import matplotlib.pyplot as plt
import pandas as pd

class CovidDataAnalyzer:
    """A class to analyze COVID-19 data."""

    def __init__(self, dataframe):
        """
        Initialize CovidDataAnalyzer object.

        Parameters:
        dataframe (pandas.DataFrame): The COVID-19 dataset.
        """
        self.dataframe = dataframe

    def plot_positive_cases_over_time(self):
        """Plot total positive COVID-19 cases over time."""
        self.dataframe.groupby('date')['positive'].sum().plot(color='blue')
        plt.title('Total Positive Cases Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Positive Cases')
        plt.show()

    def plot_deaths_over_time(self):
        """Plot total COVID-19 deaths over time."""
        self.dataframe.groupby('date')['death'].sum().plot(color='red')
        plt.title('Total Deaths Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Deaths')
        plt.show()

    def plot_cases_by_state(self):
        """Plot total positive COVID-19 cases by state."""
        total_cases_by_state = self.dataframe.groupby('state')['positive'].sum().sort_values(ascending=False)
        total_cases_by_state.plot(kind='bar', color='skyblue')
        plt.title('Total Positive Cases by State')
        plt.xlabel('State')
        plt.ylabel('Total Positive Cases')
        plt.xticks(rotation=90)
        plt.show()
