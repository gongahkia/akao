# https://www.plotaroute.com/search?keyword=singapore

from playwright.async_api import async_playwright

async def click_initial_popup(page):
    try:
        popup = await page.query_selector('div.qc-cmp2-summary-buttons button.css-8riygd')
        if popup:
            await popup.click()
            print("Initial popup clicked.")
    except Exception as e:
        print(f"Initial popup not found or could not be clicked: {e}")

async def handle_google_vignette(page):
    try:
        current_url = page.url
        if "#google_vignette" in current_url:
            print("Google vignette detected, removing fragment and reloading...")
            clean_url = current_url.replace("#google_vignette", "")
            await page.goto(clean_url)
            print("Reloaded page without #google_vignette.")
            return True
    except Exception as e:
        print(f"Could not handle google vignette: {e}")
    return False

async def scrape_routes(url, threshold=None):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await click_initial_popup(page)
        traversed_urls = set()
        all_routes = []
        while True:
            await handle_google_vignette(page)
            current_url = page.url
            if current_url in traversed_urls:
                print(f"Already visited {current_url}, skipping.")
                break
            traversed_urls.add(current_url)
            results_div = await page.query_selector('#ResultsDiv')
            if not results_div:
                break
            results_table = await results_div.query_selector('table#ResultsTab')
            if not results_table:
                break
            rows = await results_table.query_selector_all('tr')
            for row in rows:
                tds = await row.query_selector_all('td')
                if len(tds) < 10:
                    continue
                route_template = {
                    'ID': await tds[0].inner_text(),
                    'route_name': await tds[1].inner_text(),
                    'route_url': await (await tds[1].query_selector('a')).get_attribute('href') if await tds[1].query_selector('a') else None,
                    'location': await tds[2].inner_text(),
                    'country': await tds[3].inner_text(),
                    'route_activity_type': await tds[5].inner_text(),
                    'route_distance': await tds[6].inner_text(),
                    'route_elevation_gain': await tds[7].inner_text(),
                    'route_terrain_type': await tds[8].inner_text(),
                    'route_number_views': await tds[9].inner_text()
                }
                all_routes.append(route_template)
                print(f'{len(all_routes)} scraped routes from {current_url}')
                if threshold is not None and len(all_routes) >= threshold:
                    print(f"Threshold of {threshold} reached, stopping Plotaroute scrape.")
                    await browser.close()
                    return all_routes
            pagination = await page.query_selector('ul.pagenos')
            if not pagination:
                break
            page_items = await pagination.query_selector_all('a')
            next_url = None
            for item in page_items:
                text = await item.inner_text()
                if text.strip().lower() == 'next':
                    next_url = await item.get_attribute('href')
                    break
            if next_url:
                from urllib.parse import urljoin
                next_url = urljoin(page.url, next_url)
                if next_url in traversed_urls:
                    print(f"Already traversed {next_url}, stopping.")
                    break
                await page.goto(next_url)
            else:
                break
        await browser.close()
        print(f'{len(all_routes)} routes scraped')
        return all_routes
