from load_csv import load
from aff_life import display

dataFrame = load("life_expectancy_years.csv")
print(dataFrame)

if dataFrame is not None:
    display(dataFrame, "France")
