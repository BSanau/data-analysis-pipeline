# Function to generate a scatter plot

import matplotlib.pyplot as plt

def plotfunction (df):
    pop_hosp=df["Population (M)"]/df["Hospitals"]
    x = df["Mortality"]/1000*10
    y = pop_hosp

    country = df["Country"][0]
    owner = df["Ownership"][0]
    title = f"{country}: {owner} hospitals"

    if country == "Ghana":
        colors = "#ff3333"
    elif country == "Spain":
        colors = "#333fff"

    # Plot
    plt.scatter(x, y, c=colors)
    plt.title(title)
    plt.xlabel('Infant Mortality (%)')
    plt.ylabel('Poputalion (M) /hospitals')
    plt.show()

    #return plt