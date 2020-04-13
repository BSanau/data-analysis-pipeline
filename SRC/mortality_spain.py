# Cleaning Infant Mortality Spain API
# Units: Deaths per thousand live births
# Source: www.ine.es

import json
import pandas as pd

def mortality_spain():
    # Reading jason file
    with open('INPUT/Spain_Infant_mortality.json', 'r') as file:
        datajson=file.read()
    rawdata = json.loads(datajson)

    # Function to save data into a list of dictionaries
    def datoscomunidad (comunidad):
        return {
            "Region": comunidad["MetaData"][0]["Nombre"], # Comunidad autónoma
            "Mortality": comunidad["Data"][0]["Valor"] #mortalidad
        }

    # Transforming function into df
    mortality = pd.DataFrame(list(map(datoscomunidad, rawdata[1:18])))
    mortality = mortality.set_index("Region")

    translator = {
        "Andalucía": "Andalucia",
        "Aragón": "Aragon",
        "Cataluña": "Catalunya",
        "Madrid, Comunidad de": "C_Madrid",
        "Comunitat Valenciana": "C_Valenciana",
        "Canarias": "Canarias",
        "Cantabria": "Cantabria",
        "Castilla - La Mancha": "Castilla_Mancha",
        "Castilla y León": "Castilla_Leon",
        "Navarra, Comunidad Foral de": "Navarra",
        "Extremadura": "Extremadura",
        "Galicia": "Galicia",
        "Balears, Illes": "Baleares",
        "Rioja, La": "Rioja",
        "País Vasco": "Pais_Vasco",
        "Asturias, Principado de": "Asturias",
        "Murcia, Región de": "Murcia"
    }

    # Renaming indexes
    mortality = mortality.rename(index=translator)
    mortality = mortality.sort_index()

    return mortality