import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  fig, ax = plt.subplots(figsize=(13, 8))
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

  # Create first line of best fit
  lm = LinearRegression()
  X = df[['Year']]
  Y = df[['CSIRO Adjusted Sea Level']]
  lm.fit(X, Y)

  fit_data = pd.DataFrame(columns=['Year', 'Sea Level'])

  for year in range(df["Year"].min(), 2050):
    fit_data.loc[year, "Year"] = year
    fit_data.loc[year, "Sea Level"] = (lm.intercept_ + lm.coef_ * year)

  fit_data.set_index('Year')

  fig, ax = plt.subplots(figsize=(13, 8))
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
  plt.plot(fit_data["Year"], fit_data["Sea Level"], 'r')

  # Create second line of best fit
  df1 = df.loc[df['Year'] >= 2000]

  lm = LinearRegression()
  X1 = df1[['Year']]
  Y1 = df1[['CSIRO Adjusted Sea Level']]
  lm.fit(X1, Y1)

  fit_data_1 = pd.DataFrame(columns=['Year', 'Sea Level'])

  for year in range(df1["Year"].min(), 2050):
    fit_data_1.loc[year, "Year"] = year
    fit_data_1.loc[year, "Sea Level"] = (lm.intercept_ + lm.coef_ * year)

  fit_data_1.set_index('Year')

  fig, ax = plt.subplots(figsize=(13, 8))
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
  plt.plot(fit_data["Year"], fit_data["Sea Level"], 'r')
  plt.plot(fit_data_1["Year"], fit_data_1["Sea Level"], 'b')

  # Add labels and title
  fig, ax = plt.subplots(figsize=(13, 8))
  plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
  plt.plot(fit_data["Year"], fit_data["Sea Level"], 'r')
  plt.plot(fit_data_1["Year"], fit_data_1["Sea Level"], 'b')
  ax.set_title('Rise in Sea Level')
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
