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
from SRC.f_plot import *
from SRC.f_createpdf import createpdf


def main():
    ####    HOSPITALS DF    ####

    path_csv = "INPUT/health-facilities-gh.csv" # Ghana Hospitals csv
    path_json = "INPUT/Spain_hospitals.json"
    hospitals = pd.concat([ghanahospitals(path_csv), spainhospitals(path_json)])


    #### PROGRAM DESCRIPTION ####

    # Adding a description and variables needed
    parser = ArgumentParser(description="Program to analyse hospital facilities in Ghana and Spain")

    parser.add_argument("--owner",help="Ownership: Government or Private", default="Government")
    parser.add_argument("--country",help="Country: Ghana, Spain or Both", default="Ghana")

    # Reading args from environment
    args = parser.parse_args()


    #### PROGRAM IMPLEMENTATION ####

    # Rejecting invalid values
    rejected = rejection(args.owner, args.country)

    # Filtering hospitals df with owner and country values
    if rejected == None:
        filtered_df=hospitals[(hospitals["Ownership"]== args.owner) & (hospitals["Country"]==args.country)]
        if args.country == "Ghana":
            url = "https://es.wikipedia.org/wiki/Ghana"
            path_csv = "INPUT/Ghana_infant_mortality.csv"
            study_df=pd.concat([filtered_df, population_area_ghana(url), mortality_ghana(path_csv)], axis =1)        
            # Function to plot
            plotfunction (study_df) 
        elif args.country == "Spain":
            url = "https://es.wikipedia.org/wiki/Comunidad_aut%C3%B3noma"
            path_json = "INPUT/Spain_Infant_mortality.json"
            study_df=pd.concat([filtered_df, population_area_spain(url), mortality_spain(path_json)], axis =1)
            # Function to plot
            plotfunction (study_df) 
        else:
            url1 = "https://es.wikipedia.org/wiki/Ghana"
            url2 = "https://es.wikipedia.org/wiki/Comunidad_aut%C3%B3noma"
            path_csv = "INPUT/Ghana_infant_mortality.csv"
            path_json = "INPUT/Spain_Infant_mortality.json"
            filtered_df=hospitals[(hospitals["Ownership"]== args.owner)]
            pop = pd.concat([population_area_ghana(url1), population_area_spain(url2)])
            mort = pd.concat([mortality_ghana(path_csv), mortality_spain(path_json)])
            study_df=pd.concat([filtered_df, pop, mort], axis =1)
            # Function to plot
            plotboth(study_df)
        #print(study_df)

        # Guardar la función, crear un PDF
        createpdf(args.country, args.owner)

if __name__ == "__main__": 
    main() 
