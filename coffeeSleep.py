import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
  hoursOfSleep = []
  coffeeVolume = []
  with open(data_path) as dp:
    csv_reader = csv.DictReader(dp)
    for row in csv_reader:
      hoursOfSleep.append(float(row["sleep in hours"]))
      coffeeVolume.append(float(row["Coffee in ml"]))

  return{"y": hoursOfSleep, "x": coffeeVolume}

def findCorrelation(data_source):
  correlation = np.corrcoef(data_source["x"], data_source["y"])
  print("The coefficient of correlation between the datasets is ", correlation[0,1])

def setup():
  data_path = "cups of coffee vs hours of sleep.csv"
  data_source = getDataSource(data_path)
  findCorrelation(data_source)

setup()