import pandas as pd
import numpy as np
#import matplotlib as mpl



def read_csv(filename="api-pov.csv"):
    df = pd.read_csv(filename)
    newDf = df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
    print(newDf.shape)
    return newDf
def read_csv_2(filename="api-pov.csv"):
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

    df = pd.DataFrame(
        [countries_data[0][4:55], countries_data[1][4:55], countries_data[2][4:55]])
    print(df)

    df.plot()

    #countries_data[0][4:55]
    #countries_data[0][4:55].Series.plot()
    

def test(df):
    df1 = df[df['Country Name'].isin(
        ['Argentina', "Cote d'Ivoire", 'United States'])]

    print(df1)

    
def top_10_poverty_diagram():
    df = read_csv_2()
    idArr = []
    for i in range(10):
        index = df[["2016"]].idxmax()
        idArr.append(index.tolist()[0])
        df = df.drop(index)
    df = read_csv_2()
    df = df.ix[idArr]

    
    df.plot.bar(x="Country Name")
    

#poverty_line_diagram()
#read_csv()
test(read_csv())
