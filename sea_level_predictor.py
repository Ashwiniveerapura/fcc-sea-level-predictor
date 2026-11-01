import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # 1. Import data from epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data', s=10)

    # 3. First Line of Best Fit (All data from 1880 to 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(1880, 2051)
    line_all = res_all.slope * years_all + res_all.intercept
    plt.plot(years_all, line_all, color='red', label='Best Fit Line 1 (1880-2050)', linestyle='--')

    # 4. Second Line of Best Fit (Data from year 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    line_recent = res_recent.slope * years_recent + res_recent.intercept
    plt.plot(years_recent, line_recent, color='green', label='Best Fit Line 2 (2000-2050)')

    # 5. Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # 6. Save plot and return the current figure context
    plt.savefig('sea_level_plot.png')
    return plt.gca()
