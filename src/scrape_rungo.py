# https://routes.rungoapp.com/routes?search=singapore&minDistance=3&maxDistance=10&units=imperial&lat=0&lng=0&geoBox=null

from playwright.async_api import async_playwright

async def scrape_routes(url, threshold=None):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        all_routes = []
        route_id = 0
        while True:
            current_url = page.url
            route_list_div = await page.query_selector('div#route-list')
            if not route_list_div:
                break
            items = await route_list_div.query_selector_all('div.large-12.small-12.columns.route-listing.list-item')
            if not items:
                break
            for item in items:
                item_id = await item.get_attribute('id')
                if not item_id or "route-listing-" not in item_id:
                    continue
                name_div = await item.query_selector('div.large-9.small-8.columns.route-name')
                route_name = await name_div.inner_text() if name_div else ''
                name_link = await name_div.query_selector('a') if name_div else None
                route_url = await name_link.get_attribute('href') if name_link else ''
                if route_url and not route_url.startswith('http'):
                    from urllib.parse import urljoin
                    route_url = urljoin(page.url, route_url)
                distance_div = await item.query_selector('div.large-3.small-4.columns.route-distance')
                route_distance = await distance_div.inner_text() if distance_div else ''
                terrain_div = await item.query_selector('div.large-12.small-12.columns.route-description')
                route_terrain_type = await terrain_div.inner_text() if terrain_div else ''
                route_template = {
                    'ID': str(route_id),
                    'route_name': route_name,
                    'route_url': route_url,
                    'location': '',
                    'country': 'Singapore',
                    'route_activity_type': '',
                    'route_distance': route_distance,
                    'route_elevation_gain': '',
                    'route_terrain_type': route_terrain_type,
                    'route_number_views': ''
                }
                all_routes.append(route_template)
                print(f'{len(all_routes)} scraped routes from {current_url}')
                route_id += 1
                if threshold is not None and len(all_routes) >= threshold:
                    print(f"Threshold of {threshold} reached, stopping RunGo scrape.")
                    await browser.close()
                    return all_routes
            pagination_ul = await page.query_selector('div.pagination ul')
            if pagination_ul:
                li_items = await pagination_ul.query_selector_all('li')
                selected_index = None
                for idx, li in enumerate(li_items):
                    class_attr = await li.get_attribute('class')
                    if class_attr and 'page-number' in class_attr and 'selected' in class_attr:
                        selected_index = idx
                        break
                if selected_index is not None and selected_index + 1 < len(li_items):
                    next_li = li_items[selected_index + 1]
                    next_a = await next_li.query_selector('a')
                    if next_a:
                        await next_a.click()
                        await page.wait_for_load_state('networkidle')
                        continue  
            break  
        print(f'{len(all_routes)} routes scraped')
        return all_routes