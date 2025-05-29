import json
import re
import time
import traceback

from bs4 import BeautifulSoup
from urllib3 import request

# Base URL of site
BASE_URL = "https://www.thegradcafe.com"
# URL for Grad Cafe survey results, sorted by newest first
INDEX_PAGE_URL = "https://www.thegradcafe.com/survey/index.php?page={page_num}"
# Target number of entries to scrape
TARGET_ENTRIES = 10000
# Delay between requests
REQUEST_DELAY = 2


def scrape_data():
    """Pulls data from Grad Cafe until at least TARGET_ENTRIES are collected."""
    all_entries_data = []
    page_num = 1

    print(f"Starting scrape. Target: {TARGET_ENTRIES} entries.")

    while len(all_entries_data) < TARGET_ENTRIES:
        current_url = INDEX_PAGE_URL.format(page_num=page_num)
        print(f"Requesting page: {page_num} ({current_url})")
        try:
            response = request("GET", current_url)
            if response.status != 200:
                print(f"Error fetching page {page_num}: HTTP {response.status}")
                break

            soup = BeautifulSoup(response.data, "html.parser")

            results_table = soup.find("table")

            if not results_table:
                print(f"Could not find results table on page {page_num}. Stopping.")
                break

            entry_rows = results_table.find_all("tr")

            current_entry_group = {}

            for entry_row in entry_rows[1:]:
                if _is_new_entry_group(entry_row):
                    if current_entry_group:
                        all_entries_data.append(current_entry_group)
                    current_entry_group = {}

                current_entry_group.update(_collect_entry_data(entry_row))

                if len(all_entries_data) >= TARGET_ENTRIES:
                    break

            page_num += 1
            time.sleep(REQUEST_DELAY)

        except Exception as e:
            print(f"An error occurred on page {page_num}: {e} {traceback.format_exc()}")
            break

    print(f"Scraping finished. Total entries collected: {len(all_entries_data)}")
    return all_entries_data


def _is_new_entry_group(entry_row):
    """Check if the entry is a new entry group."""
    return _is_first_row(entry_row)


def _collect_entry_data(entry_row):
    """Collect data from a single entry group."""
    if _is_first_row(entry_row):
        return _collect_data_from_first_row(entry_row)
    elif _is_second_row(entry_row):
        return _collect_data_from_second_row(entry_row)
    elif _is_third_row(entry_row):
        return _collect_data_from_third_row(entry_row)
    return {}


def _is_first_row(entry_row):
    """
    Check if the entry is the first row of an entry
    group by checking for a See More link.
    """
    return (
        entry_row.find("a", string=re.compile(r"See More", re.IGNORECASE)) is not None
    )


def _is_second_row(entry_row):
    """
    Check if the entry is the second row of an entry group by
    checking for a div with the tw-bg-orange-400 class.
    """
    return entry_row.find("div", class_="tw-bg-orange-400") is not None


def _is_third_row(entry_row):
    """
    Check if the entry is the third row of an entry group by
    checking for a p with the tw-text-gray-500 class.
    """
    return entry_row.find("p", class_="tw-text-gray-500") is not None


def _collect_data_from_first_row(entry_row_1):
    """Collect data from the first row of an entry group."""
    cells = entry_row_1.find_all("td")

    return {
        "university_raw": cells[0].get_text(strip=True),
        "program_raw": cells[1].find_all("span")[0].get_text(strip=True),
        "degree_raw": cells[1].find_all("span")[1].get_text(strip=True),
        "added_on": cells[2].get_text(strip=True),
        "decision_info_raw": cells[3].get_text(strip=True),
        "url": BASE_URL + cells[4].find("a")["href"] if cells[4].find("a") else None,
    }


def _collect_data_from_second_row(entry_row_2):
    """Collect data from the second row of an entry group."""
    divs = entry_row_2.find_all("div")

    gre_raw = entry_row_2.find("div", string=re.compile(r"GRE ", re.IGNORECASE))
    gre_v_raw = entry_row_2.find("div", string=re.compile(r"GRE V ", re.IGNORECASE))
    gre_aw_raw = entry_row_2.find("div", string=re.compile(r"GRE AW ", re.IGNORECASE))
    gpa_raw = entry_row_2.find("div", string=re.compile(r"GPA ", re.IGNORECASE))

    return {
        "semester_and_year_of_program_start_raw": divs[2].get_text(strip=True),
        "student_type_raw": divs[3].get_text(strip=True),
        "gre_raw": gre_raw.get_text(strip=True) if gre_raw else None,
        "gre_v_raw": gre_v_raw.get_text(strip=True) if gre_v_raw else None,
        "gre_aw_raw": gre_aw_raw.get_text(strip=True) if gre_aw_raw else None,
        "gpa_raw": gpa_raw.get_text(strip=True) if gpa_raw else None,
    }


def _collect_data_from_third_row(entry_row_3):
    """Collect data from the third row of an entry group."""
    comments_tag = entry_row_3.find("p")

    return {
        "comments_raw": comments_tag.get_text(strip=True) if comments_tag else None,
    }


if __name__ == "__main__":
    print("Starting Grad Cafe Scraper...")
    raw_data = scrape_data()

    if raw_data:
        with open("raw_applicant_data.json", "w") as f:
            json.dump(raw_data, f, indent=4)
        print(
            f"Successfully saved {len(raw_data)} raw entries to raw_applicant_data.json"
        )
    else:
        print("No data was scraped.")
