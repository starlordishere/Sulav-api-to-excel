import openpyxl
import urllib.request
import json
key= 'ab5bf4b0970860437fc442604639d812' # for openweathermap
import time
import statistics
import weather

from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
import requests, json, time


def read_excel(name):
  wb = load_workbook(name)
  sheet1 = wb['Sheet1']
  sheet2 = wb['Sheet2']
  sheet3 = wb['Sheet3']
  
  city1 = sheet1["A1"].value
  city2 = sheet2["A1"].value
  cities = [city1, city2]
  
  print(city1)
  print(city2)
  
 
  ext_data = []
  
  #making api call
  for city in cities:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city.lower()}&appid={key}' 
  
    #store API response in a json file as r
    response = requests.get(url).json()
    
    #dumping into a json File
    filename = 'data.json'
    with open(filename, 'w') as fobj:
      json.dump(response, fobj, indent = 4)
    
    #loading a json File
    filename = 'data.json'
    with open(filename) as fobj:
      all_data = json.load(fobj)
    
    min_temp = all_data['main']['temp_min']
    max_temp = all_data['main']['temp_max']
  
    t_celsius1 = round(min_temp - 273.15, 2)
    t_celsius2 = round(max_temp - 273.15, 2)
    
    ext_data.append(t_celsius1)
    ext_data.append(t_celsius2)
  print(ext_data)
  c1, c2 = [], []
  c1.append(ext_data[0])
  c1.append(ext_data[1])
  c2.append(ext_data[2])
  c2.append(ext_data[3])
  print(c1)
  print(c2)
  
  #appending extracted data to sheet 1
  rows = [
      ("Min Temp", "Max Temp"),
      (c1[0], c1[1])
  ]
  
  for row in rows:
    sheet1.append(row)
  
  #append the extracted data  to sheet2
  rows = [
      ("Min Temp", "Max Temp"),
      (c2[0], c2[1])
  ]
  
  for row in rows:
    sheet2.append(row)
  
  #appending extracted data to sheet 3
  rows = [
      ("Min Temp", "Max Temp"),
      (c1[0], c1[1]),
      (c2[0], c2[1])
  ]
  
  for row in rows:
    sheet3.append(row)
  
    
  #make chart 1
  chart1 = BarChart()
  chart1.type = "col"
  chart1.style = 10
  chart1.title = "Bar Chart of City Temperature"
  chart1.y_axis.title = 'Frequency'
  chart1.x_axis.title = 'Temperature (celsius)'
  
  #make chart 2
  chart2 = BarChart()
  chart2.type = "col"
  chart2.style = 10
  chart2.title = "Bar Chart of City Temperature"
  chart2.y_axis.title = 'Frequency'
  chart2.x_axis.title = 'Temperature (celsius)'
  
  #make chart 3
  chart3 = BarChart()
  chart3.type = "col"
  chart3.style = 10
  chart3.title = "Bar Chart Comparing Two (2) City Temperatures"
  chart3.y_axis.title = 'Frequency'
  chart3.x_axis.title = 'Temperature (celsius)'
  
  data = Reference(sheet1, min_col=1, min_row=2, max_row=4, max_col=2)
 
  chart1.add_data(data, titles_from_data=True)

  chart1.shape = 4
  sheet1.add_chart(chart1, "A5")
  
  data = Reference(sheet2, min_col=1, min_row=2, max_row=4, max_col=2)

  chart2.add_data(data, titles_from_data=True)
 
  chart2.shape = 4
  sheet2.add_chart(chart2, "A5")
  
  data = Reference(sheet3, min_col=1, min_row=1, max_row=3, max_col=2)
  
  chart3.add_data(data, titles_from_data=True)
 
  chart3.shape = 4
  sheet3.add_chart(chart3, "A5")
  
  
  wb.save("processed/plot.xlsx")

  #logging processed files to keeptrack
  data = "processed/plot.xlsx"
  with open(f'plot-{time.time()}.json', 'w') as f:
    json.dump(data, f)