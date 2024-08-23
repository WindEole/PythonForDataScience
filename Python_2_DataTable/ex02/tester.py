from load_csv import load
from aff_pop import display

dataFrame = load("population_total.csv")
print(dataFrame)

if dataFrame is not None:
    display(dataFrame, "France", "Belgium")
    # display(dataFrame, "Tuvalu", "Marshall Islands")
    # display(dataFrame, "Belgium", "Marshall Islands")
    # display(dataFrame, "Mauritania", "Malaysia")
