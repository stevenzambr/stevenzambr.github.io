import requests
import json

# Read locally stored private NyTimes Api Key
with open('../apiKeys.json') as f:
  nyTimesApiKey = json.load(f)["NyTimes"]

# Set year and month
year = '2021'
month = '2'

# Get all NyTimes articles for the specified month
data = requests.get("https://api.nytimes.com/svc/archive/v1/"+year+"/"+month+".json?api-key="+nyTimesApiKey).json()

# Save data in json file (saved locally to avoid multiple requests for same archived data)
with open('dataFiles/nyTimesData_'+year+'_'+month+'.json', 'w') as outfile:
    json.dump(data, outfile)