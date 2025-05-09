# ----- required imports -----

import json
import asyncio
import scrape_greatruns as greatruns
import scrape_outdooractive as outdooractive
import scrape_plotaroute as plotaroute
import scrape_rungo as rungo
import scrape_wikiloc as wikiloc

# ----- helper functions -----

def save_routes_to_json(routes, filepath="routes.json"):
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(routes, f, ensure_ascii=False, indent=4)
        print(f"Routes successfully saved to {filepath}")
    except Exception as e:
        print(f"Error saving routes to JSON: {e}")

async def main(url_map, filepath):
    try:
        results = await asyncio.gather(
            greatruns.scrape_routes(url_map["greatruns"]["url"], url_map["greatruns"]["threshold"]),
            # outdooractive.scrape_routes(url_map["outdooractive"]["url"], url_map["outdooractive"]["threshold"]),
            plotaroute.scrape_routes(url_map["plotaroute"]["url"], url_map["plotaroute"]["threshold"]),
            # rungo.scrape_routes(url_map["rungo"]["url"], url_map["rungo"]["threshold"]),
            wikiloc.scrape_routes(url_map["wikiloc"]["url"], url_map["wikiloc"]["threshold"]),
        )
        combined_results = [route for route_list in results for route in route_list] 
        save_routes_to_json(combined_results, filepath)
        return True
    except:
        return False

# ----- execution code -----

if __name__ == "__main__":
    # FUA edit the below url_map
    url_map = {
        "plotaroute": {
            "url": "https://www.plotaroute.com/search?keyword=singapore",
            "threshold": 100,
        },
        # "rungo": {
        #     "url": "https://routes.rungoapp.com/routes?search=singapore",
        #     "threshold": 100,
        # },
        "greatruns": {
            "url": "https://greatruns.com/location/singapore/",
            "threshold": 100,
        },
        # "outdooractive": {
        #     "url": "https://www.outdooractive.com/en/routes/#area=1019113&filter=r-fullyTranslatedLangus-en,r-openState-,sb-sortedBy-0&wt=Singapore%20(Country)%0A1019113&zc=11.,103.81943,1.35119",
        #     "threshold": 100,
        # },
        "wikiloc": {
            "url": "https://www.wikiloc.com/trails/running/singapore",
            "threshold": 100,
        },
    }
    filepath = "../data/routes.json"
    asyncio.run(main(url_map, filepath))