import numpy as np
import matplotlib.pyplot as plt
import datetime

def readMappingFile():
    infile = open('city_temp/citylistWorld.htm', 'r')
    data = infile.readlines()[261:]
    mapping = {}


    for line in data:
        if "mso-list" in line:
            mapping[line[line.find('<b>')+3:-20]] = data[data.index(line)+2][data[data.index(line)+2].find('>')+1:data[data.index(line)+2].find('</a>')]
    infile.close()
    return mapping

def loadData(dictionary, cityName):
    fileName = dictionary[cityName]
    infile = open('city_temp/' + fileName)
    dates = []
    temps = []
    for line in infile:
        dates.append(datetime.date(int(line.split()[2]), int(line.split()[0]), int(line.split()[1])))
        temps.append(float(line.split()[3]))
    finaldata = {'dates': np.array(dates), 'temps': np.array(temps)}
    infile.close()
    return finaldata

def plotData(*cities):
    cityList = []
    for city in cities:
        cityList.append(city)
        plt.plot_date(loadData(readMappingFile(), city)['dates'], loadData(readMappingFile(), city)['temps'], '.')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend(cityList)
    plt.show()

print plotData('Tirana', 'London', 'Shenyang')

