# Module 5: SQL Data Analysis

This project involves loading data scraped from Grad Cafe into a PostgreSQL database, performing SQL-based data analysis, and displaying the results on a Flask webpage.

## Project Structure

```
module_5/
├── load_data.py            # Script to load data into PostgreSQL
├── query_data.py           # Python functions for SQL queries
├── requirements.txt        # Python package dependencies
├── limitations.pdf         # Written analysis on data limitations
├── module_5_results.pdf    # Results from the output of query_data.py
├── app/
│   └── app.py                  # Flask application
│   └── templates/
│       └── index.html          # HTML template for the Flask app
│   └── static/
│       └── style.css           # CSS styles for the Flask app
```

## Setup

1.  **Database Setup**:
    *   Ensure you have PostgreSQL installed and running, or use a service like Neon's PostgreSQL.
    *   Update the database connection details in `load_data.py` and `query_data.py` (and `app.py` if it connects directly).
    *   The `applicants` table schema is defined in `load_data.py`.

2.  **Python Environment**:
    *   It's recommended to use a virtual environment.
    *   Install the required packages:
        ```bash
        pip install -r requirements.txt
        ```

3.  **Data Loading**:
    *   Place your cleaned Grad Cafe data (from Module 1, likely a CSV or JSON file) in an accessible location.
    *   Update the `load_data_from_source` function in `load_data.py` to point to your data file and handle its format.
    *   Run the script to create the table and load the data:
        ```bash
        python module_5/load_data.py
        ```

## Running the Analysis

*   The `query_data.py` script contains functions to answer the specific analytical questions. You can run this script (after uncommenting the example calls in `if __name__ == "__main__":`) to see the results in your terminal, or import its functions into other scripts/notebooks.
    ```bash
    python module_5/query_data.py 
    ```
    *(Ensure database is populated first)*

## Running the Flask Web Application

*   Once your data is loaded and queries are working, run the Flask app:
    ```bash
    python module_5/app.py
    ```
*   Open your web browser and navigate to the address provided by Flask (usually `http://127.0.0.1:5000/`).

## Deliverables

1.  The SSH URL to your GitHub repository.
2.  `load_data.py` under `module_5/`.
3.  `query_data.py` under `module_5/`.
4.  `limitations.pdf` under `module_5/`.
5.  `app.py` under `module_5/`.
6.  Associated Flask app files (`templates/index.html`, `static/style.css`) under `module_5/app/`.
6.  This `README.md` under `module_5/`.
7.  `requirements.txt` under `module_5/`. 
