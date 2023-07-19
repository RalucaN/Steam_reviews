import time
import urllib.parse
from . import utils

# Args:
#   session = http session to be reused across requests
#   reqLimit = the maximum number of requests until stopping
#   speedLimit = how many seconds to wait after each request
# Returns a tuple consisting of the reviews data and the last cursor
def getGameReviews(session, cursor="", reqLimit=1000, speedLimit=0):
    reviews=""
    cursor=""
    conf = utils.retrieveConfiguration("steampowered", "/appreviews")
    reqCount=0
    while(reqCount<reqLimit):
        url=conf["url"]
        response=utils.sendRequest(url, conf["verb"].upper(), session)
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
        time.sleep(speedLimit)
    return reviews, cursor