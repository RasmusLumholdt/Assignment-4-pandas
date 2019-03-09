import pandas as pd
import numpy as np



def read_csv(filename="api-pov.csv"):
    return pd.read_csv(filename)



def poverty_line_diagram():
    allData = read_csv()
    allCountries = allData['Country Name']
    
    countries = ['Argentina', 'North America', 'Kenya']
    country_indexes = []
    countries_data = []

    #Gets the index of the countries, and puts them in an array
    for i in range(len(countries)):
        if (len(allCountries[allCountries == countries[i]]) <= 0):
            print('Error can find: ' + countries[i])
        else:
            print('Found: ' + countries[i])
            index = (allCountries[allCountries == countries[i]].index[0])
            countries_data.append(allData.loc[index])
        
    #Get each line of the countries

    print(countries_data[0][4:55])
    countries_data[0][4:55].plot()
    


poverty_line_diagram()
