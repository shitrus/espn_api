import requests, json
nextgame = {}
prefix_teamurl = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/"
prefix_GIU = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event="
for each in ["2","5","6","8","9","12","21","23","24","25","26","30","36","38","41","52","55","57","58","59","61","62","66","68","77","84","87","96","97","98","99","103","113","120","127","130","135","142","145","150","151","152","153","154","158","164","166","167","183","189","193","194","195","197","201","202","204","213","218","221","228","235","238","239","242","245","248","249","251","252","254","256","258","259","264","265","275","276","277","278","290","295","309","324","326","328","333","344","349","356","2005","2006","2026","2032","2050","2084","2116","2117","2132","2199","2226","2229","2247","2294","2305","2306","2309","2335","2348","2390","2393","2426","2429","2433","2439","2440","2459","2483","2509","2534","2567","2572","2579","2628","2633","2636","2638","2641","2649","2653","2655","2711","2751"]:
    teamReq = requests.get(prefix_teamurl + each)
    teamId = "teamId_" + each
    gameId = teamReq.json()["team"]["nextEvent"][0]["id"]
    gameIdName = {}
    gameIdNameVal = "gameId_" + gameId
    gameIdName[teamId] = {}
    gameIdUrl = prefix_GIU + gameId
    gameIdReq = requests.get(gameIdUrl)
    if gameIdReq.json()["pickcenter"] == []:
        gameIdName[teamId]["oddsExist"] = False
    else:
        gameIdName[teamId]["oddsExist"] = True
        gameIdName[teamId]["homeTeamId"] = gameIdReq.json()["predictor"]["homeTeam"]["id"]
        gameIdName[teamId]["awayTeamId"] = gameIdReq.json()["predictor"]["awayTeam"]["id"]
        awayFavorite = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["favorite"]
        homeFavorite = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["favorite"]
        gameIdName[teamId]["overUnder"] = gameIdReq.json()["pickcenter"][0]["overUnder"]
        gameIdName[teamId]["spread"] = gameIdReq.json()["pickcenter"][0]["spread"]
        gameIdName[teamId]["details"] = gameIdReq.json()["pickcenter"][0]["details"]
        gameIdName[teamId]["provider"] = gameIdReq.json()["pickcenter"][0]["provider"]["name"]
        if (awayFavorite):
            gameIdName[teamId]["favorite"] = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["teamId"]
            gameIdName[teamId]["underdog"] = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["teamId"]
        elif (homeFavorite):
            gameIdName[teamId]["favorite"] = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["teamId"]
            gameIdName[teamId]["underdog"] = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["teamId"]
        else:
            gameIdName[teamId]["favorite"] = "pickem"
            gameIdName[teamId]["underdog"] = "pickem"
    nextgame[gameIdNameVal] = gameIdName
with open('nextgame.json', 'w') as fp:
    json.dump(nextgame, fp)
