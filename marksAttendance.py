import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
  marksPercentage = []
  daysPresent = []
  with open(data_path) as dp:
    csv_reader = csv.DictReader(dp)
    for row in csv_reader:
      daysPresent.append(float(row["Days Present"]))
      marksPercentage.append(float(row["Marks In Percentage"]))

  return{"y": marksPercentage, "x": daysPresent}

def findCorrelation(data_source):
  correlation = np.corrcoef(data_source["x"], data_source["y"])
  print("The coefficient of correlation between the datasets is ", correlation[0,1])

def setup():
  data_path = "Student Marks vs Days Present.csv"
  data_source = getDataSource(data_path)
  findCorrelation(data_source)

setup()