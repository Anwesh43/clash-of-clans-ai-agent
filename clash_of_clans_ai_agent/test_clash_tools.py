from tools.clash_tools import getLeagueSeasonDetails, getLeagues, getPlayerRankingsInLocation, getClanRankingsInLocation, getClanDetails, getPlayerDetails, getLeagueTierDetails, getLeagueSeasons, getLeagueTiers, getLocations
from typing import Dict 
import json 

def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"writeFile to {fileName}")

if __name__ == "__main__":
    leagues = getLeagues()
    writeFile("leagues.json", leagues)
    writeFile("league_tiers.json", getLeagueTiers())
    if len(leagues) > 0 and "id" in leagues[0]:
        leagueId = leagues[-1]["id"]
        leagueSeasons = getLeagueSeasons(leagueId)
        writeFile("league_seasons.json", leagueSeasons)
        if len(leagueSeasons) > 0 and "id" in leagueSeasons[0]:
            leagueSeasonDetails = getLeagueSeasonDetails(leagueId=leagueId, seasonId=leagueSeasons[0]["id"])
            writeFile("league_season_details.json", leagueSeasonDetails)
            if len(leagueSeasonDetails) > 0:
                playerTag = leagueSeasonDetails[0]["playerTag"]
                clanTag = leagueSeasonDetails[0]["clanTag"]
                writeFile("player_details.json", getPlayerDetails(playerTag=playerTag))
                writeFile("clan_details.json", getClanDetails(clanTag=clanTag))
   
    locations = getLocations()
    writeFile("locations.json", locations)
    if len(locations) > 0 and "id" in locations[0]:
        print("Locations", locations[-1])
        writeFile("locations_player_ranking.json", getPlayerRankingsInLocation(locationId=locations[-1]["id"]))
        writeFile("locations_clan_ranking.json", getClanRankingsInLocation(locationId=locations[-1]["id"]))