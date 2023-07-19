import json
import os
from datetime import date

# Define the limits for concurrent and total requests
CONCURRENT_LIMIT = 10 # number of concurrent requests allowed
CONCURRENT_PERIOD = 1 # period in seconds for concurrent limit
TOTAL_LIMIT = 100 # number of total requests allowed
TOTAL_PERIOD = 60 # period in seconds for total limit

# REST config declaration here
protocol=""
host=""
path=""
params=""
verb=""

# output file extension
extension=".json"
# date token for file naming
today = date.today().strftime("%y-%m-%d")
# get the directory name of the script file
script_dir = os.path.dirname(__file__)

def loadSteamKey():
    # get the relative path from the script to the data folder
    rel_path = "..\steamKey.txt"
    # join the script directory and the relative path
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, "r") as file:
        return file.read()

def writeToFile(response, path, name, type="a"):
    if response.ok:
        data = json.loads(response.content)
        filename=name+"-"+today+extension
        relPath=os.path.join(path, filename)
        abs_file_path = os.path.join(script_dir, relPath)
        file=open(abs_file_path, type)
        json.dump(data, file, indent=4)
        file.close()
        print(f"Report saved as {filename}")
    else:
        print("Request failed: ", response.status_code)

def buildEndpointURL_Query(protocol, host, path, queryParams):
    endpoint=protocol+"://"+host+"/"+path+"?"
    for param in queryParams:
        endpoint+=param+"&"
    if(endpoint.endswith("&")):
        endpoint=endpoint[:-1]
    return endpoint

def sendRequest(endpoint, verb, session, authentication=None):
    response=""
    if authentication is None:
        if verb=="GET":
            response=session.get(endpoint)
        elif verb=="POST":
            response=session.post(endpoint)
        elif verb=="PUT":
            response=session.put(endpoint)
        elif verb=="DELETE":
            response=session.delete(endpoint)
    else:
        if verb=="GET":
            response=session.get(url=endpoint, auth=authentication)
        elif verb=="POST":
            response=session.post(url=endpoint, auth=authentication)
        elif verb=="PUT":
            response=session.put(url=endpoint, auth=authentication)
        elif verb=="DELETE":
            response=session.delete(url=endpoint, auth=authentication)
    if response.ok:
        return response
    else:
        print("Request failed: ", response.status_code)
        return None

def getDataFromCSV():
    print("TODO")

def get_value(response, keys):
    if response.ok:
        # parse the json data into a python dictionary
        data = json.loads(response.content)
        # loop through the keys and access the nested dictionary
        for key in keys:
            data = data[key]
        # return the final value
        return data
    else:
        print("Request failed: ", response.status_code)
        return None


def retrieveConfiguration(api, path):
    configFilePath="./data/"+api+"/api.json"
    with open(configFilePath, 'r') as configFile:
        conf = json.load(configFile)

    protocol=conf["protocol"]
    host=conf["host"]

    for apiObject in conf['endpoints']:
        if apiObject['path'] == path:
            params=apiObject['selectedParams']
            verb=apiObject['verb']
    return buildEndpointURL_Query(protocol, host, path, params, verb)
