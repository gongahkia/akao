# notes
    # everything should be run through this single script and logging should be handled through here as well

# remaining scrapers to implement 
    # https://routes.rungoapp.com/
    # https://greatruns.com/location/singapore/
    # https://sg.mapometer.com/running
    # https://www.alltrails.com/singapore/trail-running
    # https://www.wikiloc.com/trails/running/singapore
    # https://www.outdooractive.com/en/running-routes/singapore/running-in-singapore/137993227/
    # https://www.komoot.com/guide/73939/running-trails-in-singapore
    # https://www.joggingroutes.org/p/routes-by-countrycity.html
    # https://www.activesgcircle.gov.sg/read/running-routes-in-singapore-where-to-run-in-singapore

# ----- required imports -----

import json
import asyncio
import scrape_plotaroute as plotaroute

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
            plotaroute.scrape_routes(url_map["plotaroute"]["url"], url_map["plotaroute"]["threshold"]),
            # add more later...
            # FUA
        )
        combined_results = [route for route_list in results for route in route_list] 
        save_routes_to_json(combined_results, filepath)
        return True
    except:
        return False

# ----- execution code -----

if __name__ == "__main__":
    url_map = {
        "plotaroute": {
            "url": "https://www.plotaroute.com/search?keyword=singapore",
            "threshold": 100,
        },
        # ... FUA to add
    }
    filepath = "../data/routes.json"
    asyncio.run(main(url_map, filepath))