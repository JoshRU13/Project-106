import csv
import numpy as np
def getdata(data):
    coffee=[]
    sleep=[]
    with open(data)as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":sleep}
def findCorelation(data1):
    corelation=np.corrcoef(data1["x"],data1["y"])
    print(corelation[0,1])
def setup():
    data="cups of coffee vs hours of sleep.csv"
    data1=getdata(data)
    findCorelation(data1)
setup()        