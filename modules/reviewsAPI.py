import time
import urllib.parse
from . import utils

# Possible query params
#   "json=1",
#   "filter=recent",
#   "language=english",
#   "day_range=10",
#   "cursor=AoIIPwYYanDTv%2BQB",
#   "review_type=positive",
#   "purchase_type=steam",
#   "num_per_page=50",
#   "filter_offtopic_activity=0"
def getGameReviews(session, cursor="", reqLimit=1000, speedLimit=0):
    protocol="https"
    host="store.steampowered.com"
    path="/appreviews"
    queryParams=["json=1", "num_per_page=100", "purchase_type=all"]
    verb="GET"
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