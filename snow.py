#!/usr/bin/python3
import requests
import json
import sys
from credentials import snow_user, snow_pwd
url = 'https://domain.service-now.com/api/now/table/incident'
issue = sys.argv[1]
user = snow_user
pwd = snow_pwd

# Set proper headers and values ID you can get from the snow api explorer. 
headers = {"Content-Type":"application/json","Accept":"application/json"}
values = {"category":"71","short_description":issue,"u_business_service":"a79da54cdb1xxxxxxxx","caller_id":"17xxb6xxxxx22e890c571791xxxxx9a7","impact":"1","severity":"1","assignment_group":"2bxxxxxxd1xx350xxxxxxxxx","urgency":"1","contact_type":"Self-service","description":"incident created from jenkins","location":"60xxxxxxxxxxxxx"
str= json.dumps(values)
# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers ,data=str)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data

data = response.json()
print(data)
