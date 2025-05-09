# https://www.outdooractive.com/en/routes/#area=1019113&filter=r-fullyTranslatedLangus-en,r-openState-,sb-sortedBy-0&wt=Singapore%20(Country)%0A1019113&zc=11.,103.81943,1.35119

from asyncio import sleep
from playwright.async_api import async_playwright

async def scrape_routes(url, threshold=None):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        dialog = await page.query_selector('div#oax-dialog-main')
        if dialog:
            footer = await dialog.query_selector(
                'div.oax_modal_footer_wrap.oax_full.oax_pad_left_16.oax_pad_right_16.oax_marg_top_22.oax_marg_bottom_11'
            )
            if footer:
                buttons = await footer.query_selector_all('button')
                for btn in buttons:
                    text = (await btn.inner_text()).strip()
                    if text == "Accept all":
                        print("Clicked accept all button")
                        await btn.click()
                        await sleep(1)
                        break
        all_routes = []
        count = 0
        oax_dp_list = await page.query_selector('div.oax_dp_list')
        if oax_dp_list:
            prev_height = -1
            max_scrolls = 30  
            for _ in range(max_scrolls):
                curr_height = await oax_dp_list.evaluate('(el) => el.scrollHeight')
                await oax_dp_list.evaluate('(el) => { el.scrollTop = el.scrollHeight; }')
                await sleep(5)
                new_height = await oax_dp_list.evaluate('(el) => el.scrollHeight')
                if new_height == prev_height:
                    break
                prev_height = new_height
            route_elements = await oax_dp_list.query_selector_all('div.oax-mapList-snippet.oax-id')
            for elem in route_elements:
                class_attr = await elem.get_attribute('class')
                if 'oax-id-' in class_attr:
                    route_url_elem = await elem.query_selector('div.oax-domaw-restrict a')
                    route_url = await route_url_elem.get_attribute('href') if route_url_elem else ''
                    route_name_location_elem = await elem.query_selector('span.oax_ellipsis')
                    route_name_location = await route_name_location_elem.inner_text() if route_name_location_elem else ''
                    route_distance = ''
                    route_elevation_gain = ''
                    data_blocks = await elem.query_selector_all('div.oax_fl.oax_tour_data_block div.oax_tour_data.oax_fl')
                    for block in data_blocks:
                        text = await block.inner_text()
                        if 'distance' in text.lower():
                            route_distance = text
                        elif 'ascent' in text.lower():
                            route_elevation_gain = text
                    terrain_elem = await elem.query_selector('div.oax_snippet_labels')
                    route_terrain_type = await terrain_elem.inner_text() if terrain_elem else ''
                    route_template = {
                        'ID': count,
                        'route_name': route_name_location,
                        'route_url': route_url,
                        'location': '',
                        'country': 'Singapore',
                        'route_activity_type': '',
                        'route_distance': route_distance,
                        'route_elevation_gain': route_elevation_gain,
                        'route_terrain_type': route_terrain_type,
                        'route_number_views': ''
                    }
                    print(route_template)
                    all_routes.append(route_template)
                    count += 1
                    if threshold is not None and len(all_routes) >= threshold:
                        await browser.close()
                        return all_routes
        await browser.close()
        return all_routes