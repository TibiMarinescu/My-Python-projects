import requests
import json
import jsonpath

def test_add_student_data():
  API_URL = "http://thetestingworldapi.com/api/studentDetails"
  f = open("C://Users//TestingWorld//Desktop//TaskAPI//RequestJSON.json",'r')
  json_request = json.loads(f.read())
  response = requests.post(API_URL,json_request)
  print(response.text)

#To run the test case: pytest main.py -s

def test_get_student_data():
  API_URL = "http://thetestingworldapi.com/api/studentDetails/3034"
  response = requests.get(API_URL)

#To run the test case: pytest main.py -s

json_response = json.loads(response.text)
id = jsonpath.jsonpath(json_response,'id')

assert id[0] == 3034

def test_update_student_data():
  API_URL = "http://thetestingworldapi.com/api/studentDetails/3034"
  f = open("C://Users//tibi",'r')
  json_file = json.loads(f.read())
  response = requests.put(API_URL,f)
  print(response.text)

def test_delete_student():
  API_URL = "http://thetestingworldapi.com/api/studentDetails/3034"
  response = requests.delete(API_URL)
  print(response.text)

def test_get_student_data():
  API_URL = "http://thetestingworldapi.com/api/studentDetails/3034"
  response = requests.get(API_URL)
  json_file = json.loads(response.text)
  id = jsonpath.jsonpath(json_file,'id')
