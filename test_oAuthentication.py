import json
import requests
import jsonpath

def test_oAuthAPI():
    token_URL = "https://thetestingworld/token"
    data = {'grant-type':'password','username':'admin','password':'password'}
    response = requests.post(token_URL,data)
    print(response.text)

    #print an element e.g. 'token_path'
    token_path = jsonpath.jsonpath(response.json,'access_token')
    auth = {'Authorization' : 'Bearer ' + token_path[0]}

    API_URL = "https://thetestingworldapi.com/api"
    response = requests.get(API_URL, headers = auth)
    print(response.text)

#TO EXECUTE: pytest test_oAuthentication.py -s
