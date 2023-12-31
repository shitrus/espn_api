import requests, json, pandas, time, csv

def main(): 
    prefix_teamurl = "https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams/"
    prefix_GIU = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event="
    timestr = time.strftime("%Y%m%d%H%M%S")
    nextgamejson = "nextgame." + timestr + ".json"
    nextgamecsv = "nextgame." + timestr + ".csv"
    with open(nextgamecsv, 'w', newline ='') as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(["teamId", "gameId", "oddsExist", "homeTeamId", "awayTeamId", "awayFavorite", "homeFavorite", "provider", "favorite", "underdog", "spread", "details", "overUnder", "awayMoneyLine", "homeMoneyLine", "awayspreadOdds", "homespreadOdds", "teamId2", "gameId2", "slug", "location", "name", "nickname", "abbreviation", "displayName", "shortDisplayName", "color", "alternateColor"])

        for each in ["2","3","5","6","7","8","9","11","12","13","15","16","17","18","21","23","24","25","26","29","30","32","33","36","38","40","41","43","46","47","48","49","50","52","55","56","57","58","59","60","61","62","63","65","66","67","68","70","72","74","75","77","79","80","81","83","84","86","87","89","90","93","96","97","98","99","101","103","107","108","109","110","112","113","114","118","119","120","121","124","125","126","127","128","129","130","131","132","133","134","135","137","138","142","143","145","146","147","149","150","151","152","153","154","155","158","159","160","162","163","164","166","167","171","172","173","174","175","183","184","188","189","190","191","193","194","195","196","197","199","200","201","202","203","204","205","209","210","213","215","216","218","219","221","222","223","225","227","228","231","233","235","236","237","238","239","241","242","245","246","247","248","249","251","252","253","254","255","256","257","258","259","262","263","264","265","266","268","271","272","275","276","277","278","282","284","286","290","291","293","295","297","301","302","304","306","308","309","311","317","319","322","323","324","326","328","330","331","332","333","336","338","340","341","344","348","349","351","352","354","356","359","365","366","367","374","375","379","386","388","389","390","391","395","396","398","399","402","409","411","415","417","418","424","425","426","427","433","437","446","452","455","471","490","509","548","559","568","583","587","611","613","620","630","2000","2001","2003","2005","2006","2010","2011","2013","2015","2016","2017","2018","2019","2022","2023","2025","2026","2028","2029","2032","2033","2038","2042","2043","2044","2045","2046","2047","2050","2056","2060","2062","2065","2069","2071","2074","2075","2079","2083","2084","2085","2086","2094","2097","2101","2102","2105","2106","2107","2108","2110","2115","2116","2117","2118","2119","2120","2121","2122","2123","2127","2128","2132","2134","2141","2142","2146","2148","2151","2152","2155","2166","2168","2169","2170","2171","2175","2181","2184","2188","2191","2193","2194","2197","2198","2199","2201","2205","2206","2207","2210","2213","2214","2220","2221","2222","2224","2226","2229","2230","2231","2232","2233","2234","2237","2241","2242","2247","2248","2249","2256","2257","2258","2261","2262","2264","2271","2273","2274","2277","2280","2283","2286","2287","2291","2292","2294","2296","2302","2304","2305","2306","2309","2310","2315","2316","2318","2320","2323","2329","2331","2333","2335","2336","2339","2348","2354","2355","2359","2362","2364","2368","2369","2371","2373","2377","2382","2383","2385","2390","2392","2393","2394","2395","2396","2398","2399","2400","2401","2402","2403","2405","2413","2415","2419","2422","2424","2426","2428","2429","2433","2438","2439","2440","2441","2442","2444","2447","2448","2449","2450","2453","2458","2459","2460","2464","2466","2467","2477","2483","2486","2487","2502","2504","2506","2508","2509","2516","2519","2523","2524","2528","2529","2532","2534","2535","2542","2545","2546","2551","2553","2557","2559","2560","2564","2567","2568","2569","2570","2571","2572","2579","2582","2583","2584","2586","2587","2588","2598","2600","2614","2615","2617","2619","2623","2627","2628","2630","2633","2634","2635","2636","2638","2639","2640","2641","2643","2644","2646","2649","2651","2653","2654","2655","2657","2658","2667","2673","2674","2676","2678","2681","2682","2685","2686","2687","2688","2692","2695","2698","2699","2700","2701","2702","2703","2704","2707","2710","2711","2714","2717","2721","2723","2725","2729","2731","2733","2736","2738","2740","2741","2743","2744","2745","2746","2747","2748","2749","2751","2754","2755","2757","2758","2771","2776","2779","2781","2782","2790","2800","2802","2803","2804","2805","2808","2810","2812","2815","2816","2817","2818","2822","2823","2825","2827","2828","2830","2832","2834","2837","2838","2839","2842","2843","2844","2845","2848","2849","2851","2858","2871","2876","2882","2884","2886","2888","2891","2894","2896","2900","2909","2911","2913","2916","2919","2923","2927","2930","2938","2940","2951","2963","2964","2967","2968","2969","2970","2972","2974","2977","2980","2985","2986","3066","3071","3101","3110","3111","3112","3162","3178","6353","6845"]:
            teamReq = requests.get(prefix_teamurl + each)
            teamId = "teamId_" + each
            gameId = teamReq.json()["team"]["nextEvent"][0]["id"]
            gameIdName = {}
            frt = str(gameIdName.get(teamId, {}).get(teamId))
            if frt == "None":
                gameIdName[teamId] = {}
            else:
                continue
            print(each)
            gameIdUrl = prefix_GIU + gameId
            gameIdReq = requests.get(gameIdUrl)
            if gameIdReq.json()["pickcenter"] == [] or gameIdReq.json()["pickcenter"][0]["provider"]["name"] == "teamrankings":
                oddsExist = False
                provider = "NONE"

            else:
                oddsExist = True
                homeTeamId = gameIdReq.json()["predictor"]["homeTeam"]["id"]
                awayTeamId = gameIdReq.json()["predictor"]["awayTeam"]["id"]
                awayFavorite = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["favorite"]
                homeFavorite = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["favorite"]
                provider = gameIdReq.json()["pickcenter"][0]["provider"]["name"]
                if (awayFavorite):
                    favorite = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["teamId"]
                    underdog = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["teamId"]
                elif (homeFavorite):
                    favorite = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["teamId"]
                    underdog = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["teamId"]
                else:
                    favorite = "pickem"
                    underdog = "pickem"
                spread = gameIdReq.json()["pickcenter"][0]["spread"]
                details = gameIdReq.json()["pickcenter"][0]["details"]
                overUnder = gameIdReq.json()["pickcenter"][0]["overUnder"]
                try:
                    awayMoneyLine = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["moneyLine"]
                except KeyError:
                    awayMoneyLine = None
                try:
                    homeMoneyLine = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["moneyLine"]
                except KeyError:
                    homeMoneyLine = None
                try:
                    awayspreadOdds = gameIdReq.json()["pickcenter"][0]["awayTeamOdds"]["spreadOdds"]
                except KeyError:
                    awayspreadOdds = None
                try:
                    homespreadOdds = gameIdReq.json()["pickcenter"][0]["homeTeamOdds"]["spreadOdds"]
                except KeyError:
                    homespreadOdds = None
                
            
            teamId2 = teamReq.json()["team"]["id"]
            try:
                gameId2 = teamReq.json()["team"]["nextEvent"][0]["id"]
            except IndexError:
                continue
            slug = teamReq.json()["team"]["slug"]
            location = teamReq.json()["team"]["location"]
            name = teamReq.json()["team"]["name"]
            nickname = teamReq.json()["team"]["nickname"]
            abbreviation = teamReq.json()["team"]["abbreviation"]
            displayName = teamReq.json()["team"]["displayName"]
            shortDisplayName = teamReq.json()["team"]["shortDisplayName"]
            try:
                color = teamReq.json()["team"]["color"]
            except KeyError:
                color = None
            try:
                alternateColor = teamReq.json()["team"]["alternateColor"]
            except KeyError:
                alternateColor = None
            time.sleep(1)

            writer.writerow([teamId, gameId, oddsExist, homeTeamId, awayTeamId, awayFavorite, homeFavorite, provider, favorite, underdog, spread, details, overUnder, awayMoneyLine, homeMoneyLine, awayspreadOdds, homespreadOdds, teamId2, gameId2, slug, location, name, nickname, abbreviation, displayName, shortDisplayName, color, alternateColor])
            teamId = ""
            gameId = ""
            oddsExist = ""
            homeTeamId = ""
            awayTeamId = ""
            awayFavorite = ""
            homeFavorite = ""
            provider = ""
            favorite = ""
            underdog = ""
            spread = ""
            details = ""
            overUnder = ""
            awayMoneyLine = ""
            homeMoneyLine = ""
            awayspreadOdds = ""
            homespreadOdds = ""
            teamId2 = ""
            gameId2 = ""
            slug = ""
            location = ""
            name = ""
            nickname = ""
            abbreviation = ""
            displayName = ""
            shortDisplayName = ""
            color = ""
            alternateColor = ""

if __name__ == '__main__':
    main()
