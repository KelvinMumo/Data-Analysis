import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file

    df = pd.read_csv('epa-sea-level.csv', float_precision="legacy")

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = df['Year']
    y1 = line.slope * x1 + line.intercept

    plt.plot(x1, y1)

    # Create second line of best fit

    x2 = np.arange(2000, 2050)
    y2 = line.slope * x2 + line.intercept

    plt.plot(x2, y2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()