# Cleaning API: Hospitals in Spain
# Source: opendata.esri.es/

import json
import pandas as pd


def datahosp(raw):
    return {
        "Name": raw["properties"]["NOMBRE"],
        "Region": raw["properties"]["COMUNIDADES"], 
        "Ownership": raw["properties"]["DEPENDENCIA_PATRIMONIAL"],
        }


def spainhospitals():
    # Reading json file (previously download from API)
    with open('INPUT/Spain_hospitals.json', 'r') as file:
        datajson=file.read()

    rawdata = json.loads(datajson)

    # Saving data into a list of dictionaries
    hospitals = list(map(datahosp, rawdata["features"]))

    # Transformation to pandas DataFrame
    hospitals_df = pd.DataFrame(hospitals)

    # Cathegorising the "Ownership" into Private, Government or Others
    owner = {
        "PRIVADO NO BENÉFICO": "Private",
        "COMUNIDAD AUTÓNOMA": "Government",
        "SEGURIDAD SOCIAL": "Government", 
        "OTRO PRIVADO BENÉFICO": "Private",
        "PRIVADO-BENÉFICO (IGLESIA)": "Private",
        "ENTIDADES PÚBLICAS": "Government",
        "DIPUTACIÓN O CABILDO": "Government",
        "MATEP": "Others",
        "MUNICIPIO": "Government",
        "PRIVADO-BENÉFICO (CRUZ ROJA)": "Others",
        "MINISTERIO DE INTERIOR": "Others",
        "MINISTERIO DE DEFENSA": "Others",
        "OTRA DEPENDENCIA PATRIMONIAL": "Others"
    }
    hospitals_df = hospitals_df.replace({"Ownership": owner})

    # Dropping columns with "Ownership" = "Others"
    # Indexes for which column "Ownership" has value "Others"
    indexNumber = hospitals_df[ hospitals_df["Ownership"] == "Others" ].index
    
    # Delete these row indexes from dataFrame
    hospitals_df.drop(indexNumber , inplace=True)



    ### PUBLIC HOSPITALS DATAFRAME ###
    # Creating dataframe
    publichosp_spain=hospitals_df[hospitals_df["Ownership"] == "Government"]["Region"].value_counts()
    publichosp_spain = pd.DataFrame(publichosp_spain)
    # Dropping rows related to Ceuta and Melilla
    publichosp_spain = publichosp_spain.drop(["CEUTA", "MELILLA"])
    # Formatting columns
    publichosp_spain = publichosp_spain.rename(columns={"Region": "Hospitals"})
    publichosp_spain["Ownership"] = "Government"
    publichosp_spain = publichosp_spain.sort_index()
    


    ### PRIVATE HOSPITALS DATAFRAME ###
    # Creating dataframe
    privatehosp_spain=hospitals_df[hospitals_df["Ownership"] == "Private"]["Region"].value_counts()
    privatehosp_spain = pd.DataFrame(privatehosp_spain)
    # Formatting columns
    privatehosp_spain = privatehosp_spain.rename(columns={"Region": "Hospitals"})
    privatehosp_spain["Ownership"] = "Private"
    privatehosp_spain = privatehosp_spain.sort_index()
    


    ### CONCATENATING DATAFRAMES ###
    hosp_spain = pd.concat([publichosp_spain, privatehosp_spain])

    # Standarising names of regions
    translator = {
        "ANDALUCÍA": "Andalucia",
        "ARAGÓN": "Aragon",
        "CATALUÑA": "Catalunya",
        "MADRID": "C_Madrid",
        "COMUNIDAD VALENCIANA": "C_Valenciana",
        "CANARIAS": "Canarias",
        "CANTABRIA": "Cantabria",
        "CASTILLA-LA MANCHA": "Castilla_Mancha",
        "CASTILLA Y LEÓN": "Castilla_Leon",
        "C. FORAL DE NAVARRA": "Navarra",
        "EXTREMADURA": "Extremadura",
        "GALICIA": "Galicia",
        "ILLES BALEARS": "Baleares",
        "LA RIOJA": "Rioja",
        "PAÍS VASCO": "Pais_Vasco",
        "PPDO. DE ASTURIAS": "Asturias",
        "REGIÓN DE MURCIA": "Murcia"
    }

    hosp_spain = hosp_spain.rename(index=translator)

    hosp_spain["Country"] = "Spain"
    #hosp_spain = hosp_spain.reset_index()
    #hosp_spain = hosp_spain.rename(columns = {"index": "Region"})

    return hosp_spain