import requests
import json
import jsonpath

def test_add_student_multiple_data():
  API_URL = "http://testingworldapi.com/api/studentdetails"
  f = open("C:\\Users\\tibi\\Documents\\Tasks Management\\JSON2.json")
  
  #Load in JSON format
  json_requests = json.loads(f.read())
  response = requests.post(API_URL, json_requests)
  print(response.status_code)
