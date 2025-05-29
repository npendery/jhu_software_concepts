## Name & ID
Nick Pendery
JHID: E1284D

## Module Info
Module 2
Grad Cafe Scraper

This project includes a web scraper for Grad Cafe applicant data.

### Approach
I followed the guidelines to use BeautifulSoup to parse the HTML returned from the requests.

In order to collect the appropriate data, I used a combination of tag, class, and string identifiers to select which values I needed. I believe that long functions are hard to debug and read, so I chose to create many descriptive protected functions that are called within the public functions. This helps explain the process in a more readable way.

The trickiest part of parsing the html was delineating which table rows are for which entries. Since entries arent a set amount of rows and do not have classes that are descriptive, I had to use certain methods of finding specific indications of what each row is in relation to an entry. Sometimes there were two rows, sometimes there were three, sometimes there were rows that weren't part of any entry, so parsing that out was important to ensure all entry data is collected together.

### Known Bugs
None

### robots.txt Compliance

The `robots.txt` file for `thegradcafe.com` was checked prior to scraping. A screenshot of the `robots.txt` content can be found in `thegradcafe_com_robots_txt.png`.

The relevant section for general crawlers is:
```
User-agent: *
Disallow: /cgi-bin/
Disallow: /index-ad-test.php
```
This permits scraping of the admissions results pages.

### Running the Scraper and Cleaner

1.  **Clone the repository.**
2.  **Navigate to the `module_2` directory:**
    ```bash
    cd module_2
    ```
3.  **Create a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the scraper:**
    ```bash
    python scrape.py
    ```
    This will fetch data from Grad Cafe and save it to `raw_applicant_data.json`. This might take a while as it collects up to 10,000 entries with delays between requests.
6.  **Run the data cleaner:**
    ```bash
    python clean.py
    ```
    This will process `raw_applicant_data.json`, clean and structure the data, and save it to `applicant_data.json`.

### Scraper Project Structure

-   `scrape.py`: Contains the `scrape_data()` function to pull data from Grad Cafe.
-   `clean.py`: Contains `clean_data()`, `save_data()`, and `load_data()` functions for processing and managing the scraped data.
-   `raw_applicant_data.json`: Stores the raw data directly from the scraper.
-   `applicant_data.json`: Stores the final cleaned and structured JSON data.
-   `thegradcafe_com_robots_txt.png`: Screenshot of `thegradcafe.com/robots.txt`.

