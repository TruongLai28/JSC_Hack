import asyncio
import csv
from playwright.async_api import async_playwright

async def scraper():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto('https://nspires.nasaprs.com/external/solicitations/solicitations!init.do')
        await page.wait_for_selector('select[name="openSolicitations_length"]')
        await page.select_option('select[name="openSolicitations_length"]', '100')
        
        await page.wait_for_selector('#filterStatusList_Open')
        await page.click('#filterStatusList_Open')
        
        await page.wait_for_timeout(2000)
        
        # Updated evaluation to get URLs along with other fields
        solicitations = await page.evaluate('''
            () => {
                const rows = document.querySelectorAll('table#openSolicitations tbody tr');
                return Array.from(rows).map(row => {
                    const titleLink = row.querySelector('a[target="solSearch"]');
                    const statusSpan = row.querySelector('.solStatusIcon');
                    const solIdElement = row.querySelector('a[id^="solSummaryAnchor"]');
                    
                    return {
                        title: titleLink ? titleLink.textContent : '',
                        url: titleLink ? titleLink.href : '',
                        status: statusSpan ? statusSpan.getAttribute('title') : '',
                        solicitation_id: solIdElement ? solIdElement.textContent.trim() : ''
                    };
                });
            }
        ''')
        
        await browser.close()
        return solicitations

async def main():
    results = await scraper()
    
    # Save results to CSV with additional columns
    with open('solicitations.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Solicitation Title', 'Status', 'Solicitation ID', 'URL'])
        for index, item in enumerate(results, 1):
            writer.writerow([
                index,
                item['title'],
                item['status'],
                item['solicitation_id'],
                item['url']
            ])
    
    print(f"Total solicitations found: {len(results)}")
    print("Data saved to solicitations.csv")

if __name__ == "__main__":
    import asyncio
    import csv
    asyncio.run(main())

