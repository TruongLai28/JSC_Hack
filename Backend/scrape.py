import asyncio
import csv
import re
from playwright.async_api import async_playwright

async def scraper():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Navigate to the website
        await page.goto('https://stemgateway.nasa.gov/public/s/explore-opportunities')
        
        # Wait for the page to load and select 45 items
        await page.wait_for_selector('select.slds-select')
        await page.select_option('select.slds-select', '45')
        await page.wait_for_timeout(2000)
        
        opportunities = []  # List to store tuples of (title, description, url)
        page_number = 1
        
        def clean_text(text: str) -> str:
            text = ' '.join(text.split())
            text = re.sub(r'\s+', ' ', text)
            text = text.replace('"', "'")
            return text.strip()

        def clean_url_title(text: str) -> str:
            # Remove special characters and parentheses
            text = re.sub(r'[^\w\s-]', '', text)
            # Remove extra whitespace
            text = ' '.join(text.split())
            # Convert to lowercase and replace spaces with hyphens
            text = text.lower().replace(' ', '-')
            return text

        while True:
            # Get titles, descriptions, and types from current page
            titles = await page.locator('c-ostem_-opportunity-results-card h2').all_text_contents()
            descriptions = await page.locator('p.descriptionclass').all_text_contents()
            
            # Get opportunity types
            type_buttons = await page.locator('c-ostem_-opportunity-results-card button.slds-button_neutral').all()
            types = []
            for button in type_buttons:
                type_text = await button.text_content()
                if any(keyword in type_text for keyword in ['Student', 'Educator']):
                    types.append(type_text.strip())
            
            # Get all opportunity IDs from h2 elements
            h2_elements = await page.locator('c-ostem_-opportunity-results-card h2').all()
            urls = []
            for h2 in h2_elements:
                id = await h2.get_attribute('id')
                if id:
                    opportunity_id = id.split('-')[0]
                    title_text = await h2.text_content()
                    url_title = clean_url_title(title_text)
                    url = f"https://stemgateway.nasa.gov/s/course-offering/{opportunity_id}/{url_title}"
                    urls.append(url)
            
            # Combine titles, descriptions, URLs, and types
            for title, desc, url, type_ in zip(titles, descriptions, urls, types):
                opportunities.append((
                    clean_text(title),
                    clean_text(desc),
                    url,
                    type_
                ))
            
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
            writer.writerow(['ID', 'Title', 'Description', 'URL', 'Type'])
            for i, (title, desc, url, type_) in enumerate(opportunities, 1):
                writer.writerow([i, title, desc, url, type_])

        print(f"\nTotal opportunities found: {len(opportunities)}")
        print("Data saved to nasa_opportunities.csv")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scraper())