import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('./epa-sea-level.csv')
  
    # Create scatter plot
  fig, ax = plt.subplots(figsize=(12,6))
  plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level']);
  
    # Create first line of best fit
  df_since_2000 = df[df['Year'] >= 2000]
  lin_out = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
  new_lin_out = linregress(df_since_2000['Year'],df_since_2000['CSIRO Adjusted Sea Level'])
  x_fit = range(np.min(df['Year']),2051)
  new_x_fit = range(np.min(df_since_2000['Year']),2051)

    # Create second line of best fit
  y_fit = x_fit * lin_out.slope + lin_out.intercept
  new_y_fit = new_x_fit * new_lin_out.slope + new_lin_out.intercept

    # Add labels and title
  ax.plot(x_fit,y_fit,'-g',label = 'Best Fit Line 1');
  ax.plot(new_x_fit,new_y_fit,'-r',label = 'Best Fit Line 2');
  plt.title('Rise in Sea Level');
  plt.xlabel('Year');
  plt.ylabel('Sea Level (inches)');
  plt.grid()
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()