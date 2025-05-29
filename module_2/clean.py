import json
import re
from bs4 import BeautifulSoup
from pprint import pprint

def clean_data(raw_data_list):
    """Converts raw scraped data into a structured format."""
    cleaned_entries = []
    unknown_value = None # Consistent format for unavailable data

    for raw_entry in raw_data_list:
        entry = {
            'program_name': raw_entry.get('program_raw', unknown_value),
            'degree_type': raw_entry.get('degree_raw', unknown_value),
            'university': raw_entry.get('university_raw', unknown_value),
            'comments': raw_entry.get('comments_raw', unknown_value),
            'date_added': raw_entry.get('added_on', unknown_value),
            'url': raw_entry.get('url', unknown_value),
            'applicant_status': raw_entry.get('decision_info_raw', unknown_value),
            'decision_date': raw_entry.get('decision_info_raw', unknown_value),
            'program_season_year': raw_entry.get('semester_and_year_of_program_start_raw', unknown_value),
            'student_nationality': raw_entry.get('student_type_raw', unknown_value), 
            'gre_total': raw_entry.get('gre_raw', unknown_value),
            'gre_verbal': raw_entry.get('gre_v_raw', unknown_value),
            'gre_aw': raw_entry.get('gre_aw_raw', unknown_value),
            'gpa': raw_entry.get('gpa_raw', unknown_value),
        }

        comments = entry.get('comments', unknown_value)
        if isinstance(comments, str):
           comments = _remove_html(comments)
           comments = _remove_special_characters(comments)
           entry['comments'] = comments

        gre_total = entry.get('gre_total', unknown_value)
        if isinstance(gre_total, str):
            gre_total = _remove_label(gre_total, r'GRE ')
            entry['gre_total'] = float(gre_total) if gre_total else unknown_value

        gre_verbal = entry.get('gre_verbal', unknown_value)
        if isinstance(gre_verbal, str):
            gre_verbal = _remove_label(gre_verbal, r'GRE V ')
            entry['gre_verbal'] = float(gre_verbal) if gre_verbal else unknown_value

        gre_aw = entry.get('gre_aw', unknown_value)
        if isinstance(gre_aw, str):
            gre_aw = _remove_label(gre_aw, r'GRE AW ')
            entry['gre_aw'] = float(gre_aw) if gre_aw else unknown_value

        gpa = entry.get('gpa', unknown_value)
        if isinstance(gpa, str):
            gpa = _remove_label(gpa, r'GPA ')
            entry['gpa'] = float(gpa) if gpa else unknown_value

        cleaned_entries.append(entry)
    
    return cleaned_entries

def save_data(data, filename="applicant_data.json"):
    """Saves cleaned data into a JSON file."""
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved {len(data)} cleaned entries to {filename}")
    except IOError as e:
        print(f"Error saving data to {filename}: {e}")

def load_data(filename="applicant_data.json"):
    """Loads cleaned data from a JSON file."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        print(f"Successfully loaded {len(data)} entries from {filename}")
        return data
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filename}.")
        return []
    except IOError as e:
        print(f"Error loading data from {filename}: {e}")
        return []


def _remove_html(text):
    """Removes HTML tags from a string."""
    return BeautifulSoup(text, "html.parser").get_text(strip=True)

def _remove_label(text, label):
    """Removes label from a string."""
    return re.sub(label, '', text)

def _remove_special_characters(text):
    """Removes special characters from a string."""
    return re.sub(r'[\n\r\t]', '', text)

if __name__ == "__main__":
    # Example usage: Load raw data, clean it, and save it.
    print("Starting Data Cleaner...")
    raw_data_to_clean = []
    try:
        with open("raw_applicant_data.json", "r") as f:
            raw_data_to_clean = json.load(f)
        print(f"Loaded {len(raw_data_to_clean)} raw entries for cleaning.")
    except FileNotFoundError:
        print("raw_applicant_data.json not found. Run scrape.py first.")
    except Exception as e:
        print(f"Error loading raw_applicant_data.json: {e}")

    if raw_data_to_clean:
        cleaned_applicant_data = clean_data(raw_data_to_clean)
        save_data(cleaned_applicant_data)
        
        loaded_entries = load_data()
        if loaded_entries:
            for entry in loaded_entries:
                pprint(entry)
    else:
        print("No raw data to clean.") 
