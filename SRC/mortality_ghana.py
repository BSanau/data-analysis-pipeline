# Cleaning Infant Mortality Ghana csv dataset
# Units: Deaths per thousand live births
# Source: https://ghana.opendataforafrica.org/

import pandas as pd

def mortality_ghana():
    # Reading csv file
    mortality = pd.read_csv("INPUT/Ghana_infant_mortality.csv")

    # Dropping columns
    mortality = mortality.drop(columns = ["indicator", "Unit", "Date"])

    # Setting Region column as index
    mortality = mortality.set_index("region").sort_index()

    # Rename column 
    mortality = mortality.rename(columns = {"Value": "Mortality"})

    return mortality

