import pandas as pd
import sys
from argparse import ArgumentParser

from SRC.hospitals_ghana import ghanahospitals
from SRC.hospitals_spain import spainhospitals
from SRC.pop_area_ghana import population_area_ghana
from SRC.pop_area_spain import population_area_spain
from SRC.mortality_ghana import mortality_ghana
from SRC.mortality_spain import mortality_spain

from SRC.f_rejection import rejection
from SRC.f_plot import plotfunction


####    HOSPITALS DF    ####
hospitals = pd.concat([ghanahospitals(), spainhospitals()])


#### PROGRAM DESCRIPTION ####

# Adding a description and variables needed
parser = ArgumentParser(description="Program to compare hospital facilities between Ghana and Spain")

parser.add_argument("--owner",help="Ownership: Government or Private", default="Government")
parser.add_argument("--country",help="Country: Ghana or Spain", default="Ghana")

# Reading args from environment
args = parser.parse_args()


#### PROGRAM IMPLEMENTATION ####

# Rejecting invalid values
rejected = rejection(args.owner, args.country)

# Filtering hospitals df with owner and country values
if rejected == None:
    filtered_df=hospitals[(hospitals["Ownership"]== args.owner) & (hospitals["Country"]==args.country)]
    if args.country == "Ghana":
        study_df=pd.concat([filtered_df, population_area_ghana(), mortality_ghana()], axis =1)        
    if args.country == "Spain":
        study_df=pd.concat([filtered_df, population_area_spain(), mortality_spain()], axis =1)
    print(study_df)

# Function to plot
plotfunction (study_df)        

# Guardar la función, crear un PDF