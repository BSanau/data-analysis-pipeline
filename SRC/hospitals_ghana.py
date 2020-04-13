# Cleaning Health facilities Ghana csv dataset
# Source: www.kaggle.com

import pandas as pd

def ghanahospitals (path_csv):
    # Reading csv file
    facilities = pd.read_csv(path_csv)

    # Dropping columns
    facilities = facilities.drop(columns = ["District", "FacilityName","Town", "Latitude", "Longitude"])

    # Looking for hospitals
    hospital_rows = facilities["Type"].str.contains("ospital") 
    facilities = facilities[hospital_rows]

    # Cathegorising the "Ownership" into Private, Government or Others
    owner = {
        "Private": "Private",
        "Government": "Government", 
        "CHAG": "Others", 
        "Quasi-Government": "Others",
        "Islamic": "Others",
        "Muslim": "Others", 
        "Mission": "Others"      
    }

    facilities = facilities.replace({"Ownership": owner})

    # Dropping columns with "Ownership" = "Others"
    # Indexes for which column "Ownership" has value "Others"
    indexNumber = facilities[ facilities["Ownership"] == "Others" ].index
    # Delete these row indexes from dataFrame
    facilities.drop(indexNumber , inplace=True)



    ### PUBLIC HOSPITALS DATAFRAME ###
    # Creating dataframe
    publichosp_ghana = facilities[facilities["Ownership"] == "Government"]["Region"].value_counts()
    publichosp_ghana = pd.DataFrame(publichosp_ghana)
    # Formatting columns
    publichosp_ghana = publichosp_ghana.rename(columns={"Region": "Hospitals"})
    publichosp_ghana["Ownership"] = "Government"
    publichosp_ghana = publichosp_ghana.sort_index()



    ### PRIVATE HOSPITALS DATAFRAME ###
    # Creating dataframe
    privatehosp_ghana=facilities[facilities["Ownership"] == "Private"]["Region"].value_counts()
    privatehosp_ghana = pd.DataFrame(privatehosp_ghana)
    # Formatting columns
    privatehosp_ghana = privatehosp_ghana.rename(columns={"Region": "Hospitals"})
    privatehosp_ghana["Ownership"] = "Private"
    privatehosp_ghana = privatehosp_ghana.sort_index()
    privatehosp_ghana



    ### CONCATENATING DATAFRAMES ###
    hosp_ghana = pd.concat([publichosp_ghana, privatehosp_ghana])
    hosp_ghana["Country"] = "Ghana"

    return hosp_ghana