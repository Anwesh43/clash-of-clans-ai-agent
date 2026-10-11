from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

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
            return response 
        except Exception as e:
            return self._handleError(e)

    def getLeagueSeasons(self, leagueId : str):
        try:
            response = self.client.getCall(f"leagues/{leagueId}/seasons", headers = self.headers)
            return response
        except Exception as e:
            return self._handleError(e)

    def getLeagueSeasonDetails(self, leagueId : str, seasonId : str):
        try:
            response = self.client.getCall(f"leagues/{leagueId}/seasons/{seasonId}", headers = self.headers)
            results = []
            for playerRanking in response:
                obj = {}
                if "name" in playerRanking and "tag" in playerRanking:
                    obj["playerName"] = playerRanking["name"]
                    obj["playerTag"] = playerRanking["tag"]
                if "clan" in playerRanking:
                    obj["clanTag"] = playerRanking["clan"]["tag"]
                    obj["clanName"] = playerRanking["clan"]["name"]
                results.append(obj)
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
            return response 
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
        try:
            response = self.client.getCall(f"players/{playerTag}")
            return response 
        except Exception as e:
            return self._handleError(e)

    def getClanDetails(self, clanTag : str):
        try:
            response = self.client.getCall(f"clans/{clanTag}")
            return response 
        except Exception as e:
            return self._handleError(e)
        