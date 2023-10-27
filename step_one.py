import requests, json, pandas, time, csv, gspread

def main(): 
    prefix_GIU = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event="
    timestr = time.strftime("%Y%m%d%H%M%S")
    nextgamecsv = "game_results_" + timestr + ".csv"
    with open(nextgamecsv, 'w', newline ='') as outcsv:
        incsv = open("gameIDlist.csv", "r")
        writer = csv.writer(outcsv)
        writer.writerow(["gameId", "homeTeamId", "homeTeamName ", "awayTeamId", "awayTeamName", "homeTeamScore", "awayTeamScore"])

        reader =csv.DictReader(incsv)
        for each in reader:
            
            gameId = each["gameId"]
            homeTeamId = each["homeTeamId"]
            awayTeamId = each["awayTeamId"]

            gameIdUrl = prefix_GIU + gameId
            gameIdReq = requests.get(gameIdUrl)
            
            
            try:
                gameIdReq.json()["header"]["competitions"][0]["status"]["type"]["completed"] == "true"
                gameExist = 1
            except KeyError:
                gameExist = 0
            except IndexError:
                gameExist = 0
            time.sleep(1)
            if gameExist == 1:
                homeAway0 = gameIdReq.json()["header"]["competitions"][0]["competitors"][0]["homeAway"]
                score0 = gameIdReq.json()["header"]["competitions"][0]["competitors"][0]["score"]
                score1 = gameIdReq.json()["header"]["competitions"][0]["competitors"][1]["score"]
                team0 = gameIdReq.json()["header"]["competitions"][0]["competitors"][0]["team"]["displayName"]
                team1 = gameIdReq.json()["header"]["competitions"][0]["competitors"][1]["team"]["displayName"]
                if homeAway0 == "home":
                    homeTeamScore = score0
                    awayTeamScore = score1
                    homeTeamName = team0
                    awayTeamName = team1
                elif homeAway0 =="away":
                    awayTeamScore = score0
                    homeTeamScore = score1
                    homeTeamName = team1
                    awayTeamName = team0
                else:
                    awayTeamScore = ""
                    homeTeamScore = ""
                    homeTeamName = ""
                    awayTeamName = ""
                
                print(gameId,homeTeamId,homeTeamName,awayTeamId,awayTeamName,homeTeamScore,awayTeamScore,sep=" ")
                writer.writerow([gameId,homeTeamId,homeTeamName,awayTeamId,awayTeamName,homeTeamScore,awayTeamScore])
                gameId = ""
                homeTeamId = ""
                homeTeamName = ""
                awayTeamId = ""
                awayTeamName = ""
                homeTeamScore = ""
                awayTeamScore = ""
            else:
                continue        
        incsv.close()
    nextgamecsv.close()
if __name__ == '__main__':
    main()
