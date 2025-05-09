# https://www.wikiloc.com/trails/running/singapore

from playwright.async_api import async_playwright

async def scrape_routes(url, threshold=None):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        traversed_urls = set()
        all_routes = []
        route_id = 0
        while True:
            current_url = page.url
            if current_url in traversed_urls:
                print(f"Already visited {current_url}, skipping.")
                break
            traversed_urls.add(current_url)
            trails_div = await page.query_selector('div#trails ul.trail-list')
            if not trails_div:
                break
            trail_items = await trails_div.query_selector_all('li.trail-list__item')
            if not trail_items:
                break
            for item in trail_items:
                title_elem = await item.query_selector('h3.trail-card-with-description__title')
                route_name = await title_elem.inner_text() if title_elem else ''
                title_link = await title_elem.query_selector('a') if title_elem else None
                route_url = await title_link.get_attribute('href') if title_link else ''
                if route_url and not route_url.startswith('http'):
                    from urllib.parse import urljoin
                    route_url = urljoin(page.url, route_url)
                activity_elem = await item.query_selector('div.trail-card-with-description__subtitle')
                route_activity_type = await activity_elem.inner_text() if activity_elem else ''
                location_elem = await item.query_selector('div.trail-card-with-description__near')
                location = await location_elem.inner_text() if location_elem else ''
                distance = ''
                elevation = ''
                stats = await item.query_selector_all('dl.trail-card-with-description__detail__stats')
                for stat in stats:
                    dt_elems = await stat.query_selector_all('dt')
                    dd_elems = await stat.query_selector_all('dd')
                    for dt, dd in zip(dt_elems, dd_elems):
                        dt_text = await dt.inner_text()
                        dd_text = await dd.inner_text()
                        if dt_text.strip().lower() == 'distance':
                            distance = dd_text
                        elif dt_text.strip().lower() == 'elevation':
                            elevation = dd_text
                route_template = {
                    'ID': route_id,
                    'route_name': route_name,
                    'route_url': route_url,
                    'location': location,
                    'country': '',
                    'route_activity_type': route_activity_type,
                    'route_distance': distance,
                    'route_elevation_gain': elevation,
                    'route_terrain_type': '',
                    'route_number_views': ''
                }
                all_routes.append(route_template)
                print(f'{len(all_routes)} scraped routes from {current_url}')
                route_id += 1
                if threshold is not None and len(all_routes) >= threshold:
                    print(f"Threshold of {threshold} reached, stopping Wikiloc scrape.")
                    await browser.close()
                    return all_routes
            pagination_div = await page.query_selector('div.pagination')
            if pagination_div:
                page_links = await pagination_div.query_selector_all('a.pagination__item')
                if page_links:
                    last_link = page_links[-1]
                    title_attr = await last_link.get_attribute('title')
                    if title_attr and title_attr.strip().lower() == 'next':
                        await last_link.click()
                        await page.wait_for_load_state('networkidle')
                        continue  
            break  
        await browser.close()
        print(f'{len(all_routes)} routes scraped')
        return all_routes