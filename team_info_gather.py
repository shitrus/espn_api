import requests, time, csv, json

def main(): 
    nextgame = {}
    formatteddata2 = ""
    teamurl = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/"
    timestr = time.strftime("%Y%m%d%H%M%S")
    teamlistcsv = "team_list_master." + timestr + ".csv"
    with open(teamlistcsv, 'w', newline ='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["teamId", "gameId", "slug", "location", "name", "nickname", "abbreviation", "displayName", "shortDisplayName", "color", "alternateColor"])
        i = 1
        while i < 9999:
            teamReq = requests.get(teamurl + str(i))
            print(str("Team number " + i + " -- " + teamReq.status_code))
            if teamReq.status_code != 400:
                teamId = teamReq.json()["team"]["id"]
                try:
                    nextEvent = teamReq.json()["team"]["nextEvent"][0]["id"]
                except IndexError:
                    i = i + 1
                    continue
                slug = '\"' + teamReq.json()["team"]["slug"] + '\"'
                location = '\"' + teamReq.json()["team"]["location"] + '\"'
                name = '\"' + teamReq.json()["team"]["name"] + '\"'
                nickname = '\"' + teamReq.json()["team"]["nickname"] + '\"'
                abbreviation = '\"' + teamReq.json()["team"]["abbreviation"] + '\"'
                displayName = '\"' + teamReq.json()["team"]["displayName"] + '\"'
                shortDisplayName = '\"' + teamReq.json()["team"]["shortDisplayName"] + '\"'
                try:
                    color = teamReq.json()["team"]["color"]
                except KeyError:
                    color = None
                try:
                    alternateColor = teamReq.json()["team"]["alternateColor"]
                except KeyError:
                    alternateColor = None
                writer.writerow([teamId, nextEvent, slug, location, name, nickname, abbreviation, displayName, shortDisplayName, color, alternateColor])
                i = i + 1
                time.sleep(1)
            else:
                i = i + 1

if __name__ == '__main__':
    main()
