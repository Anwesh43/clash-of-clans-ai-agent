from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 
from urllib.parse import quote 

load_dotenv()

class ClashService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["CLASH_BASE_URL"])
        self.headers = {
            "Authorization": f"Bearer {os.environ["CLASH_TOKEN"]}"
        }

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "error",
            "message": str(e)
        }
    
    def getLeagues(self):
        try:
            response = self.client.getCall("leagues", headers = self.headers)
            return response["items"]
        except Exception as e:
            return self._handleError(e)

    def getLeagueSeasons(self, leagueId : str):
        try:
            response = self.client.getCall(f"leagues/{leagueId}/seasons", headers = self.headers)
            return response["items"]
        except Exception as e:
            return self._handleError(e)

    def getLeagueSeasonDetails(self, leagueId : str, seasonId : str):
        try:
            response = self.client.getCall(f"leagues/{leagueId}/seasons/{seasonId}", headers = self.headers)
            results = []
            #print("RESPONSE_ITEMS", response["items"])
            for playerRanking in response["items"]:
                obj = {}
                if "name" in playerRanking and "tag" in playerRanking:
                    obj["playerName"] = playerRanking["name"]
                    obj["playerTag"] = playerRanking["tag"]
                if "clan" in playerRanking:
                    obj["clanTag"] = playerRanking["clan"]["tag"]
                    obj["clanName"] = playerRanking["clan"]["name"]
                results.append(obj)
                if len(results) == 12:
                    break 
            return results  
        except Exception as e:
            return self._handleError(e)

    def getLeagueTiers(self):
        try:
            response = self.client.getCall(f"leaguetiers", headers = self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)

    def getLeagueTierDetails(self, leagueTierId : str):
        try:
            response = self.client.getCall(f"leaguetiers/{leagueTierId}", headers=self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)

    def getLocations(self):
        try:
            response = self.client.getCall(f"locations", headers = self.headers)
            return response["items"]
        except Exception as e:
            return self._handleError(e)

    def getClanRankingsInLocation(self, locationId : str):
        try:
            response = self.client.getCall(f"locations/{locationId}/rankings/clans", headers=self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)

    def getPlayersRankingsInLocation(self, locationId : str):
        try:
            response = self.client.getCall(f"locations/{locationId}/rankings/players", headers = self.headers)
            return response
        except Exception as e:
            return self._handleError(e)

    def getPlayerDetails(self, playerTag : str):
        print("PLAYER_TAG", playerTag)
        try:
            print("ENCODED_DATA", quote(playerTag,safe=''))
            response = self.client.getCall(f"players/{quote(playerTag,safe='')}", headers = self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)

    def getClanDetails(self, clanTag : str):
        try:
            print("ENCODED_DATA", quote(clanTag, safe=''))
            response = self.client.getCall(f"clans/{quote(clanTag, safe='')}", headers = self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)
        