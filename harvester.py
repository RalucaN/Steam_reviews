from distutils.command import build
import requests
import json
from datetime import date
from ratelimit import limits, sleep_and_retry
import urllib.parse

# Define the limits for concurrent and total requests
CONCURRENT_LIMIT = 10 # number of concurrent requests allowed
CONCURRENT_PERIOD = 1 # period in seconds for concurrent limit
TOTAL_LIMIT = 100 # number of total requests allowed
TOTAL_PERIOD = 60 # period in seconds for total limit

# output file extension
extension=".json"
# date token for file naming
today = date.today().strftime("%y-%m-%d")

apid="892970"

# REST config declaration here
protocol=""
host=""
path=""
params=""
verb=""

# Create a session object to reuse the same connection
session = requests.Session()

# Decorate your function with the limits and backoff strategy
@sleep_and_retry # this will make the function wait and retry if the limit is reached
@limits(calls=CONCURRENT_LIMIT, period=CONCURRENT_PERIOD) # this will apply the concurrent limit
@limits(calls=TOTAL_LIMIT, period=TOTAL_PERIOD) # this will apply the total limit
def send_request_with_rateLimit(apids):
    reviews=""
    cursor=""
    conf = retrieveConfiguration("steampowered", "/appreviews")
    while(True):
        url=conf["url"]
        response=sendRequest(url, conf["verb"].upper())
        try:
            cursor=urllib.parse.quote(response.json()["cursor"])
        except Exception as e:
            print(e)
            break
        if(len(cursor)>0):
            url = conf["url"]+"&cursor="+cursor
            print("cursor: " + cursor)
        else:
            break
        reviews+=str(response.content)
    # Use list comprehension to create and write files for each apid
    # [write_file(apid) for apid in apids]

    # write_file(reviews,apid)

def write_file(response, apid):
    if response.ok:
        print("OK BOSS")
        data = json.loads(response.content)
        filename=apid+today+extension
        file=open(filename, "a")
        json.dump(data, file, indent=4)
        file.close()
    else:
        print("Request failed: ", response.status_code)

def buildEndpoint(protocol, host, path, params, verb, apid):
    configuration={}
    endpoint=protocol+"://"+host+path+"/"+apid+"?"
    for param in params:
        endpoint+=param+"&"
    if(endpoint.endswith("&")):
        endpoint=endpoint[:-1]
    print(endpoint)
    configuration.update({'url': endpoint, 'verb': verb})
    return configuration

def sendRequest(url, verb):
    response=""
    if verb=="GET":
        response=session.get(url)
    elif verb=="POST":
        response=session.post(url)
    elif verb=="PUT":
        response=session.put(url)
    elif verb=="DELETE":
        response=session.delete(url)
    return response

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
    return buildEndpoint(protocol, host, path, params, verb, apid)

send_request_with_rateLimit(apid)
