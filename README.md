# data-analysis-pipeline


## Objective

To analise the hospital facilities in Spain and Ghana and how they are related to the infant mortality.


## Data sources

Data got from: 

health-facilities-gh.csv → Kaggle: https://www.kaggle.com/citizen-ds-ghana/health-facilities-gh

Spain_hospitals.json → API from opendata.esri.es/

Spain_infant_mortality.json → API from Instituto Nacional de Estadística: www.ine.es

Ghana_infant_mortality.csv → Ghana Data portal: https://ghana.opendataforafrica.org/

Wikipedia → Webscraping Ghana and Spain pages


## Program description

This program has to be executed by console by entering two parameters:
$ python3 main.py --country COUNTRY --owner OWNER

COUNTRY: Enther Ghana or Spain
OWNER: Enter Government or Private

The program will create a PDF with the report of the analysis of the parameters studied, comparing the ratios Population/ No. hospitals and Area/ No. hospitals against infant mortality.
