import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("Navigating to page...")
        await page.goto('https://stemgateway.nasa.gov/public/s/explore-opportunities/internships')
        await page.wait_for_load_state('networkidle')
        
        print("Scrolling to load all opportunities...")
        
        # Script to scroll the data table container
        scroll_script = """
        () => {
            const scrollableContainer = document.querySelector('.slds-scrollable_y');
            if (scrollableContainer) {
                const previousHeight = scrollableContainer.scrollTop;
                scrollableContainer.scrollTop = scrollableContainer.scrollHeight;
                return {
                    previousHeight,
                    currentHeight: scrollableContainer.scrollTop,
                    totalHeight: scrollableContainer.scrollHeight
                };
            }
            return null;
        }
        """
        
        # Keep track of previous item count to detect when no new items are loaded
        previous_count = 0
        same_count_iterations = 0
        
        while True:
            # Scroll
            scroll_result = await page.evaluate(scroll_script)
            if not scroll_result:
                print("Couldn't find scrollable container")
                break
                
            # Wait for potential new content to load
            await page.wait_for_timeout(2000)
            
            # Count current items
            items = await page.query_selector_all('a.outputLookupLink')
            current_count = len(items)
            print(f"Currently found {current_count} opportunities...")
            
            # Check if we're still loading new items
            if current_count == previous_count:
                same_count_iterations += 1
                if same_count_iterations >= 3:
                    print("No new items loaded after multiple scrolls, finishing...")
                    break
            else:
                same_count_iterations = 0
                previous_count = current_count
        
        # Extract titles
        titles = set()
        elements = await page.query_selector_all('a.outputLookupLink')
        for element in elements:
            title = await element.get_attribute('title')
            if title:
                titles.add(title)
        
        # Convert to sorted list
        titles_list = sorted(list(titles))
        
        print(f"\nFound {len(titles_list)} total opportunities:")
        for i, title in enumerate(titles_list, 1):
            print(f"{i}. {title}")
        
        await browser.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Main error: {str(e)}")
