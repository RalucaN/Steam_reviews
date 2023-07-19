from . import utils

def getUserData(userID, session, auth):
    protocol="https"
    host="store.steampowered.com"
    path="/dynamicstore/userdata/"
    queryParams=["id={userID}", "cc=IE", "v=1"]
    verb="GET"

    requestURL = utils.buildEndpointURL_Query(protocol, host, path, queryParams)
    response = utils.sendRequest(requestURL, verb, session, authentication=("Cookie", AUTH))
    if response != None:
        return response
    else:
        print(f"The request to {requestURL} failed")

# documentation link
# https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_.28v0002.29
def getPlayerSummary(key, steamIDs, session):
    protocol="http"
    host="api.steampowered.com"
    path="/ISteamUser/GetPlayerSummaries/v0002/"
    queryParams=[f"key={key}", f"steamids={steamIDs}"]
    verb="GET"
    requestURL = utils.buildEndpointURL_Query(protocol, host, path, queryParams)
    print(requestURL)
    response = utils.sendRequest(requestURL, verb, session)
    if response != None:
        return response
    else:
        print(f"The request to {requestURL} failed")
