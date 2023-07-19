import requests
import modules.usersAPI as users
import modules.reviewsAPI as reviews
import modules.utils as utils

apid="892970"
userID="76561198037964481"

steamKey= utils.loadSteamKey()

# Create a session object to reuse the same connection
session = requests.Session()
#reviews.getGameReviews(session, reqLimit=10000, speedLimit=1)

userData = users.getPlayerSummary(steamKey, userID, session)
personaname = utils.get_value(userData, ["response", "players", 0, "personaname"])
utils.writeToFile(response=userData, path="..\\data\\userSummary\\", name=userID, type="w+")