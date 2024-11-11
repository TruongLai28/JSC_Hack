import asyncio
import csv
import re
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
        
        opportunities = []  # List to store tuples of (title, description)
        page_number = 1
        
        def clean_text(text: str) -> str:
            # Remove extra whitespace and newlines
            text = ' '.join(text.split())
            # Replace multiple spaces with single space
            text = re.sub(r'\s+', ' ', text)
            # Remove any remaining special characters if needed
            text = text.replace('"', "'")  # Replace double quotes with single quotes to avoid CSV issues
            return text.strip()

        while True:
            # Get titles and descriptions from current page
            titles = await page.locator('c-ostem_-opportunity-results-card h2').all_text_contents()
            descriptions = await page.locator('p.descriptionclass').all_text_contents()
            
            # Combine titles and descriptions, cleaning the text
            for title, desc in zip(titles, descriptions):
                opportunities.append((clean_text(title), clean_text(desc)))
            
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
        with open('ostem.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Title', 'Description'])
            for i, (title, desc) in enumerate(opportunities, 1):
                writer.writerow([i, title, desc])

        print(f"\nTotal opportunities found: {len(opportunities)}")
        print("Data saved to ostem.csv")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_nasa_opportunities())


