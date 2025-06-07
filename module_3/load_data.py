import json
from pathlib import Path

import psycopg2

# Database connection details (replace with your actual details or use environment variables)
DB_URL = "postgresql://module_3_owner:npg_iGxjBF1N6bnU@ep-long-glitter-a5i0np1e-pooler.us-east-2.aws.neon.tech/module_3?sslmode=require"


def create_table():
    """Creates the applicants table in the database."""
    conn = None
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute(
            """
            DROP TABLE IF EXISTS applicants;
            CREATE TABLE IF NOT EXISTS applicants (
                p_id SERIAL PRIMARY KEY,
                program_name TEXT,
                degree_type TEXT,
                university TEXT,
                comments TEXT,
                date_added DATE,
                url TEXT,
                program_season_year TEXT,
                student_nationality TEXT,
                gre_total FLOAT,
                gre_verbal FLOAT,
                gre_aw FLOAT,
                gpa FLOAT,
                applicant_status TEXT,
                decision_date TEXT,
                program TEXT
            );
        """
        )
        conn.commit()
        print("Table 'applicants' created successfully or already exists.")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error creating table: {error}")
    finally:
        if conn is not None:
            conn.close()


def load_data_from_source():
    """
    Loads data from the specified source (e.g., a CSV file from Module 1)
    into the 'applicants' table.
    """
    data = json.loads(Path("../module_2/applicant_data.json").read_text())
    with psycopg2.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            query_sql = """ 
              INSERT INTO applicants (program_name, degree_type, university, comments, date_added, url, 
                                    program_season_year, student_nationality, gre_total, gre_verbal, 
                                    gre_aw, gpa, applicant_status, decision_date, program)
              SELECT program_name, degree_type, university, comments, date_added, url, 
                     program_season_year, student_nationality, gre_total, gre_verbal, 
                     gre_aw, gpa, applicant_status, decision_date,
                     CONCAT_WS(' - ', university, program_name) as program
              FROM json_populate_recordset(NULL::applicants, %s) 
          """
            cur.execute(query_sql, (json.dumps(data),))


def update_column_names():
    """Updates the column names of the applicants table."""
    conn = None
    sql = """
              ALTER TABLE applicants RENAME COLUMN program_season_year TO term;
              ALTER TABLE applicants RENAME COLUMN degree_type TO degree;
              ALTER TABLE applicants RENAME COLUMN gre_total TO gre;
              ALTER TABLE applicants RENAME COLUMN gre_verbal TO gre_v;
              ALTER TABLE applicants RENAME COLUMN applicant_status TO status;
              ALTER TABLE applicants RENAME COLUMN student_nationality TO us_or_international;"""
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error inserting data: {error}")
    finally:
        if conn is not None:
            conn.close()


if __name__ == "__main__":
    print("Creating table")
    create_table()
    print("Loading data")
    load_data_from_source()
    print("Updating column names")
    update_column_names()
    print("load_data.py executed. Table creation and data loading attempted.")
