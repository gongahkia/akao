from playwright.async_api import async_playwright

async def click_initial_popup(page):
    try:
        popup = await page.query_selector('.css-8riygdif')
        if popup:
            await popup.click()
            print("Initial popup clicked.")
    except Exception as e:
        print(f"Initial popup not found or could not be clicked: {e}")

async def handle_google_vignette(page):
    try:
        current_url = page.url
        if "#google_vignette" in current_url:
            print("Google vignette detected, attempting to dismiss...")
            dismiss_btn = await page.wait_for_selector('div#dismiss-button', timeout=5000)
            if dismiss_btn:
                await dismiss_btn.click()
                print("Google vignette dismissed.")
                return True
    except Exception as e:
        print(f"Could not handle google vignette: {e}")
    return False

async def scrape_routes(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await click_initial_popup(page)
        all_routes = []
        while True:
            if await handle_google_vignette(page):
                await page.goto(url)
                await click_initial_popup(page)
                continue
            results_div = await page.query_selector('#ResultsDiv')
            if not results_div:
                break
            results_table = await results_div.query_selector('table#ResultsTab')
            if not results_table:
                break
            rows = await results_table.query_selector_all('tr')
            for row in rows:
                route_template = {
                    'ID': None,
                    'route_name': None,
                    'route_url': None,
                    'location': None,
                    'country': None,
                    'route_activity_type': None,
                    'route_distance': None,
                    'route_elevation_gain': None,
                    'route_terrain_type': None,
                    'route_number_views': None
                }
                tds = await row.query_selector_all('td')
                if len(tds) < 10:
                    continue
                route_template['ID'] = await tds[0].inner_text()
                route_template['route_name'] = await tds[1].inner_text()
                anchor = await tds[1].query_selector('a')
                route_template['route_url'] = await anchor.get_attribute('href') if anchor else None
                route_template['location'] = await tds[2].inner_text()
                route_template['country'] = await tds[3].inner_text()
                route_template['route_activity_type'] = await tds[5].inner_text()
                route_template['route_distance'] = await tds[6].inner_text()
                route_template['route_elevation_gain'] = await tds[7].inner_text()
                route_template['route_terrain_type'] = await tds[8].inner_text()
                route_template['route_number_views'] = await tds[9].inner_text()
                all_routes.append(route_template)
            await asyncio.sleep(5)
            if await handle_google_vignette(page):
                await page.goto(url)
                await click_initial_popup(page)
                continue
            pagination = await page.query_selector('ul.pagenos')
            if not pagination:
                break
            page_items = await pagination.query_selector_all('a')
            if not page_items:
                break
            last_item = page_items[-1]
            last_text = await last_item.inner_text()
            if last_text.strip().lower() == 'next':
                await last_item.click()
                await page.wait_for_load_state('networkidle')
                print("navigating to next page...")
            else:
                break
        await browser.close()
        print(f'{len(all_routes)} routes scraped')
        return all_routes