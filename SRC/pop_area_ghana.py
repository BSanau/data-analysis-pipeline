# Webscraping: Getting population and area of each region in Ghana

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to structure the data coming from the web
def structureLine(tag):
    td = tag.find_all("td")
    line = [e.text for e in td if e.text]
    return {
            "Region": line[0],
            #"Capital": line[1],
            "Area (km2)": int("".join(line[2].split("."))),
            "Population (M)": int("".join(line[3].split(".")))/1000000      
        }

def population_area_ghana (url):
    # Webscrapping Wikipedia
    #url = "https://es.wikipedia.org/wiki/Ghana"
    res = requests.get(url) #download content
    soup = BeautifulSoup(res.text, "html.parser") #parsing data

    tabletag = soup.find_all("table") # looking for all tables
    table = tabletag[3] # interested in table 3
    rows = table.find_all("tr") # looking for rows in table

    # Applying function to table rows
    demographic = list(map(structureLine, rows[2:12]))

    # Transforming into dataframe
    demographic_df = pd.DataFrame(demographic)

    # Setting Region column as index
    demographic_df = demographic_df.set_index("Region")

    # Dictionary ES-EN with the translation of the names of the regions
    translator = {
        "Ashanti": "Ashanti",
        "Brong-Ahafo": "Brong Ahafo",
        "Ghana Central": "Central",
        "Ghana Oriental": "Eastern",
        "Gran Acra": "Greater Accra",
        "Ghana Septentrional": "Northern",
        "Alta Ghana Oriental": "Upper East",
        "Alta Ghana Occidental": "Upper West",
        "Volta": "Volta",
        "Ghana Occidental": "Western"
    }

    # Renaming/translating indexes
    demographic_df = demographic_df.rename(index=translator)
    demographic_df = demographic_df.sort_index()

    return demographic_df