import asyncio
import csv
from playwright.async_api import async_playwright

async def scrape_nasa_opportunities():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to the website
        await page.goto('https://stemgateway.nasa.gov/public/s/explore-opportunities')
        
        # Wait for the page to load and select 45 items
        await page.wait_for_selector('select.slds-select')
        await page.select_option('select.slds-select', '45')
        await page.wait_for_timeout(2000)
        
        all_titles = []
        page_number = 1
        
        while True:
            # Get titles from current page
            titles = await page.locator('c-ostem_-opportunity-results-card h2').all_text_contents()
            all_titles.extend([title.strip() for title in titles])
            
            # Check for next button that's not disabled
            next_button = page.locator('button.slds-button_neutral:has-text("Next")')
            is_disabled = await next_button.get_attribute('aria-disabled') == 'true'
            
            if is_disabled:
                break
                
            # Click next and wait for new results
            await next_button.click()
            await page.wait_for_timeout(2000)
            page_number += 1
            print(f"Scraped page {page_number}...")

        # Save to CSV
        with open('nasa_opportunities.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Title'])  # Write header
            for i, title in enumerate(all_titles, 1):
                writer.writerow([i, title])

        print(f"\nTotal opportunities found: {len(all_titles)}")
        print("Data saved to nasa_opportunities.csv")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_nasa_opportunities())


