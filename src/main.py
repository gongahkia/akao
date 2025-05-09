# notes
    # use threads if necessary to centralise everything
    # everything should be run through this single script and logging should be handled through here as well
    # 

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

import scrape_plotaroute as plotaroute
import asyncio

url = "https://www.plotaroute.com/search?keyword=singapore"
routes = asyncio.run(plotaroute.scrape_routes(url))