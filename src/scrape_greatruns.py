# https://greatruns.com/location/singapore/

import asyncio
from playwright.async_api import async_playwright

async def scrape_routes(url, threshold=None):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        all_routes = []
        count = 0
        city_section = await page.query_selector('section#City-Sections')
        if city_section:
            articles = await city_section.query_selector_all('article')
            for article in articles:
                location_elem = await article.query_selector('h3.Entry-Small-Title')
                country_elem = await article.query_selector('h3.Entry-Small-City')
                route_name_elem = await article.query_selector('span.Entry-Meta-KeyCats')
                route_url_elem = await article.query_selector('div.Entry-More a')
                route_activity_type_elem = await article.query_selector('div.Entry-Small-Text')
                location = await location_elem.inner_text() if location_elem else ''
                country = await country_elem.inner_text() if country_elem else ''
                route_name = await route_name_elem.inner_text() if route_name_elem else ''
                route_url = await route_url_elem.get_attribute('href') if route_url_elem else ''
                route_activity_type = await route_activity_type_elem.inner_text() if route_activity_type_elem else ''
                route_template = {
                    'ID': count,
                    'route_name': route_name,
                    'route_url': route_url,
                    'location': location,
                    'country': country,
                    'route_activity_type': route_activity_type,
                    'route_distance': '',
                    'route_elevation_gain': '',
                    'route_terrain_type': '',
                    'route_number_views': ''
                }
                all_routes.append(route_template)
                print(f"{len(all_routes)} scraped routes from {url}")
                if threshold is not None and len(all_routes) >= threshold:
                    print(f"Threshold of {threshold} reached, stopping scrape.")
                    await browser.close()
                    return all_routes
                count += 1
        await browser.close()
        print(f"{len(all_routes)} routes scraped")
        return all_routes