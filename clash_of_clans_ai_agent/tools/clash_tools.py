from services.clash_service import ClashService 

clashService = ClashService()

def getLeagues():
    print(f"Calling getLeagues tool")
    return clashService.getLeagues()

def getLeagueSeasons(leagueId : str):
    print(f"Calling getLeagueSeasons tool")
    return clashService.getLeagueSeasons(leagueId=leagueId)

def getLeagueSeasonDetails(leagueId : str, seasonId : str):
    print(f"Calling getLeagueSeasonDetails tool {leagueId} and {seasonId}")
    return clashService.getLeagueSeasonDetails(leagueId=leagueId, seasonId=seasonId)

def getLeagueTiers():
    print(f"Calling getLeagueTiers")
    return clashService.getLeagueTiers()

def getLeagueTierDetails(leagueTierId : str):
    print(f"Calling getLeagueTierDetails tool {leagueTierId}")
    return clashService.getLeagueTierDetails(leagueTierId=leagueTierId)

def getLocations():
    print(f"Callign getLocations tool")
    return clashService.getLocations()

def getPlayerRankingsInLocation(locationId : str):
    print(f"Calling getPlayerRankingsInLocation tool {locationId}")
    return clashService.getPlayersRankingsInLocation(locationId=locationId)

def getClanRankingsInLocation(locationId : str):
    print(f"Calling getClashRankingsInLocation tool {locationId}")
    return clashService.getClanRankingsInLocation(locationId=locationId)

def getPlayerDetails(playerTag : str):
    print(f"Calling getPlayerDetails for {playerTag}")
    return clashService.getPlayerDetails(playerTag=playerTag)

def getClanDetails(clanTag : str):
    print(f"Calling getClanDetails tool {clanTag}")
    return clashService.getClanDetails(clanTag=clanTag)

def getAvailableTools():
    return list(set([
        getClanDetails,
        getPlayerDetails,
        getLeagueTierDetails, 
        getClanRankingsInLocation, 
        getPlayerRankingsInLocation,
        getLocations,
        getLeagueTiers,
        getLeagues,
        getLeagueSeasonDetails,
        getLeagueTierDetails,
        getLeagueSeasons, 
    ]))