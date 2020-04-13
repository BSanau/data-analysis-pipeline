#import random
import os 
import pandas as pd
import sys
from argparse import ArgumentParser
#import subprocess


# Reading csv file
facilities = pd.read_csv("../INPUT/health-facilities-gh.csv")

# Dropping columns
facilities = facilities.drop(columns = ["District", "FacilityName","Town", "Latitude", "Longitude"])


def filtering(region):#, type, owner):
    if region == "Ashanti":
        return region
        #rows = facilities["Region"]=="Great Accra"
        #return facilities["Region"][rows]
    #elif lang=="en":
    #    return f"Hello {ta} from {lugar}"
    else:
        return "No puedo saludar"

#print(sys.argv)

# Optional arguments
parser = ArgumentParser(description="This program filters data from health facilities in Ghana")

parser.add_argument("--region", help="Select a region in Ghana", default="Ashanti")
#parser.add_argument("--type", help="Type of facility", default="Hospital")
#parser.add_argument("--owner", help="Ownership", default="Government")

# Showing optional arguments by console
args = parser.parse_args()

# Parametrize this program with the "LUGAR" environment variable
region = os.getenv("region")

#lang = sys.argv[2]
#saluda(lang,lugar)
print(filtering())
"""
Escribir por consola args.py --help para que salgan los tipos de argumentos que le puedo meter.

"""