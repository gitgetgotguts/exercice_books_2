# Bayt Job Scraper

## Overview
`bayt_scraper.py` is a web scraping script that extracts job listings from Bayt.com, specifically targeting job postings in Tunisia. The script uses Playwright for browser automation and BeautifulSoup for HTML parsing to collect detailed information about job opportunities.

## Features
- **Dynamic Web Scraping**: Uses Playwright to handle JavaScript-rendered content
- **Comprehensive Data Extraction**: Collects job title, company name, posting date, experience requirements, and job description
- **Error Handling**: Implements defensive programming with fallback values for missing data
- **Multi-page Navigation**: Automatically visits individual job listing pages for detailed information

## Dependencies
The script requires the following Python packages:
```bash
pip install playwright beautifulsoup4
```

After installing Playwright, you'll also need to install the browser binaries:
```bash
playwright install
```

## How It Works

### 1. Initial Setup
- Launches a Chromium browser instance (visible mode, `headless=False`)
- Navigates to the Bayt.com Tunisia jobs page

### 2. Job Links Collection
- Locates all job listings using CSS selector `li[class*='has-pointer-d']`
- Extracts job links from each listing using the `data-js-aid='jobID'` attribute
- Constructs complete URLs by prepending the base domain

### 3. Data Extraction
For each job listing, the script extracts:
- **Job Title**: From `h1` element with id `job_title`
- **Company Name**: From the first `li` element within `ul.list.is-basic`
- **Post Date**: From `span` element with id `jb-posted-date`
- **Experience Level**: From `div` with attribute `data-automation-id="id_type_level_experience"`
- **Job Description**: From `div` with class `t-break` (preserves formatting with newlines)

### 4. Output
Currently, the script prints the extracted information to the console with a separator line between each job.

## Code Structure

```python
# Browser setup and navigation
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(Baseurl)
    
    # Extract job links
    jobs = page.locator("li[class*='has-pointer-d']")
    links = []
    for i in range(jobs.count()):
        # Extract href attributes
    
    # Process each job
    for link in links:
        # Navigate to job page
        # Parse HTML with BeautifulSoup
        # Extract job details
        # Print results
```

## Error Handling
The script implements robust error handling:
- Uses conditional expressions (`if ... else "N/A"`) to handle missing elements
- Prevents crashes when specific job details are unavailable
- Closes browser pages properly after processing

## Future Enhancements
The script includes comments suggesting future improvements:
- **Data Storage**: Export results to CSV or Excel format using pandas
- **Structured Data**: Store job information in a list of dictionaries for better data management

## Example Usage
```bash
python bayt_scraper.py
```

## Output Format
```
Title: Software Engineer
Company: Tech Company Ltd
Post Date: Posted 2 days ago
Experience: 2-5 years
Description: We are looking for a skilled software engineer...
--------------------------------------------------
```

## Notes
- The script runs in non-headless mode, so you'll see the browser window during execution
- Each job page is opened in a new browser tab and closed after processing
- The script respects the website's structure and uses appropriate selectors
- Error handling ensures the script continues even if some job details are missing

## Technical Details
- **Language**: Python 3.x
- **Browser Automation**: Playwright (Chromium)
- **HTML Parsing**: BeautifulSoup4
- **Target Website**: Bayt.com (Tunisia job listings)
- **Approach**: Hybrid (Playwright for navigation + BeautifulSoup for parsing)
