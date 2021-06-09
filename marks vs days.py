import csv
import numpy as np
def getdata(data):
    coffee=[]
    sleep=[]
    with open(data)as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            coffee.append(float(row["Marks In Percentage"]))
            sleep.append(float(row["Days Present"]))
    return{"x":coffee,"y":sleep}
def findCorelation(data1):
    corelation=np.corrcoef(data1["x"],data1["y"])
    print(corelation[0,1])
def setup():
    data="Student Marks vs Days present.csv"
    data1=getdata(data)
    findCorelation(data1)
setup()   