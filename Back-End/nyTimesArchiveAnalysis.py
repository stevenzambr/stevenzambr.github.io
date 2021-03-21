import json


# Read stored data
with open('dataFiles/nyTimesData_2021_1.json') as f:
  data_2021_1 = json.load(f)

# TODO: Data Analysis of NyTimes articles
print(data_2021_1["response"]["docs"][0]["headline"]["main"])