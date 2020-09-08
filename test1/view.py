from django.shortcuts import render
import pandas as pd
import math

dict = {'PM2.5': None,
        'PM10': None,
        'SO2': None,
        'NO2': None,
        'CO':None,
        'O3':None}
def home_view(request,*args, **kwargs):

    df = pd.read_csv('Data.csv')
    pm25 = df['PM2.5'].tolist()
    pm10 = df['PM10'].tolist()
    so2 = df['SO2'].tolist()
    no2 = df['NO2'].tolist()
    co = df['CO'].tolist()
    o3 = df['O3'].tolist()
    populateDict(pm25,"pm25")
    populateDict(pm10,"pm10")
    populateDict(so2,"so2")
    populateDict(no2,"no2")
    populateDict(co,"co")
    populateDict(o3,"o3")
    # print(dict)
    return render(request, "home.html", {'data' : dict})

def std(list):
    sum =0
    result = 0
    if(len(list) >0): 
        for i in list:
            sum += i
        mean = sum/len(list)
        sum = 0
        for i in list:
            sum += (i - mean)**2
        result = math.sqrt(sum/len(list))
    else:
        pass
    return round(result,2)

def filler(list):
    above20 = []
    belowEqual20 = []
    for i in list:
        if ( i > 20):
            above20.append(i)
        elif (i <= 20):
            belowEqual20.append(i)
        else:
            pass
    return above20,belowEqual20

def populateDict(list,varName):
    above20 =[]
    belowEqual20 = []
    above20 , belowEqual20 = filler(list)
    if (varName == "pm25"):
        dict['PM2.5'] = [std(above20),std(belowEqual20)]
    elif(varName == "pm10"):
        dict['PM10'] = [std(above20),std(belowEqual20)]
    elif(varName == "so2"):
        dict['SO2'] = [std(above20),std(belowEqual20)]
    elif(varName == "no2"):
        dict['NO2'] = [std(above20),std(belowEqual20)]
    elif(varName == "co"):
        dict['CO'] = [std(above20),std(belowEqual20)]
    elif(varName == "o3"):
        dict['O3'] = [std(above20),std(belowEqual20)]
    