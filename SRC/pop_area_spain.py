# Webscrapping: Getting population and area of each region in Spain

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to structure the area data coming from the web
def structureAreaLines(tag):
    td = tag.find_all("td")
    return {
        "Region": td[1].find_all("a")[-1].text,
        "Area (km2)": int("".join(td[2].text.strip().split("\xa0")))  
        }


# Function to structure the data coming from the web
def structurePopulationLines(tag):
    td = tag.find_all("td")
    return {
        "Region": td[1].find_all("a")[-1].text,
        "Population (M)": int("".join("".join(td[2].text.strip().split("\xa0")).split(" ")))/1000000 
        }


def population_area_spain():
    # Webscrapping Wikipedia
    url = "https://es.wikipedia.org/wiki/Comunidad_aut%C3%B3noma"
    res = requests.get(url) #download content
    soup = BeautifulSoup(res.text, "html.parser") #parsing data

    tabletag = soup.find_all("table") # looking for all tables

    ####    AREA    ####

    table = tabletag[3] # area located in table 3
    rows = table.find_all("tr") # looking for rows in table

    # Applying function to table rows
    area_spain = list(map(structureAreaLines, rows[1:18]))

    # Transforming into dataframe
    area_spain_df = pd.DataFrame(area_spain)

    # Getting a dataframe with the regions as indexes
    area_spain_df = area_spain_df.set_index("Region").sort_index()

    translator = {
        "Andalucía": "Andalucia",
        "Aragón": "Aragon",
        "Cataluña": "Catalunya",
        "Comunidad de Madrid": "C_Madrid",
        "Comunidad Valenciana": "C_Valenciana",
        "Canarias": "Canarias",
        "Cantabria": "Cantabria",
        "Castilla-La Mancha": "Castilla_Mancha",
        "Castilla y León": "Castilla_Leon",
        "Comunidad Foral de Navarra": "Navarra",
        "Extremadura": "Extremadura",
        "Galicia": "Galicia",
        "Islas Baleares": "Baleares",
        "La Rioja": "Rioja",
        "País Vasco": "Pais_Vasco",
        "Principado de Asturias": "Asturias",
        "Región de Murcia": "Murcia"
    }

    # Renaming the indexes
    area_spain_df = area_spain_df.rename(index = translator)
    #print(area_spain_df)


    ####    POPULATION    ####

    table = tabletag[4] # area located in table 4
    rows = table.find_all("tr") # looking for rows in table

    # Applying function to table rows
    population_spain=list(map(structurePopulationLines, rows[1:18]))

    # Transforming into dataframe
    population_spain_df = pd.DataFrame(population_spain)

    # Getting a dataframe with the regions as indexes
    population_spain_df = population_spain_df.set_index("Region").sort_index()

    # Renaming the indexes
    population_spain_df = population_spain_df.rename(index = translator)
    #print(population_spain_df)


    ####    JOIN AREA AND POPULATION DF    ####

    pop_area_spain = pd.concat([area_spain_df, population_spain_df], axis=1)
    
    return pop_area_spain