# Function to generate a scatter plot

import matplotlib.pyplot as plt

def plotfunction (df):

    country = df["Country"][0]
    owner = df["Ownership"][0]
    title = f"{country}: {owner} hospitals"

    # Setting colours
    if country == "Ghana":
        colors = "#ff3333"
    elif country == "Spain":
        colors = "#333fff"

    # Creating two subplots
    figure, (ax1, ax2) = plt.subplots(2,1)


    # Plot 1: Function Population(M)/Hospitals versus Mortality
    pop_hosp=df["Population (M)"]/df["Hospitals"]
    x = df["Mortality"]/1000*10
    y = pop_hosp

    # Plot
    ax1.scatter(x, y, c=colors)
    #ax1.set_xlabel('Infant Mortality (%)')
    ax1.set_ylabel('Poputalion (M)/ Hospitals')


    # Plot 2: Function Area/Hospitals versus Mortality
    area_hosp=df["Area (km2)"]/df["Hospitals"]
    x = df["Mortality"]/1000*10
    y = area_hosp

    # Plot
    ax2.scatter(x, y, c=colors)
    ax2.set_xlabel('Infant Mortality (%)')
    ax2.set_ylabel('Area (km2)/ Hospitals')


    # Title
    figure.suptitle(title)

    # Saving figure
    plt.savefig("OUTPUT/graphic.png")
    plt.show()