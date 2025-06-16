"""
This module contains the functions to query the database and return the results.
"""

import psycopg2

DB_URL = "postgresql://\
module_3_owner:npg_iGxjBF1N6bnU\
@ep-long-glitter-a5i0np1e-pooler.us-east-2.aws.neon.tech/\
module_3?sslmode=require"


def get_db_connection():
    """Establishes and returns a database connection."""
    conn = psycopg2.connect(DB_URL)
    return conn


def question_1_fall_2024_entries():
    """How many entries do you have in your database who have applied for Fall 2024?"""
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT COUNT(*) FROM applicants WHERE term = 'Fall 2024';"
    cur.execute(query)
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count, query


def question_2_international_percentage():
    """
    What percentage of entries are from international
    students (not American or Other) (to two decimal places)?
    """
    conn = get_db_connection()
    cur = conn.cursor()
    query_international = (
        "SELECT COUNT(*) FROM applicants WHERE us_or_international = 'International';"
    )
    cur.execute(query_international)
    international_count = cur.fetchone()[0]

    query_total = "SELECT COUNT(*) FROM applicants;"
    cur.execute(query_total)
    total_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    if total_count == 0:
        return 0.00, query_international + " " + query_total

    percentage = (international_count / total_count) * 100
    return round(percentage, 2), query_international + " " + query_total


def question_3_average_metrics():
    """What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?"""
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
    SELECT 
        AVG(gpa) as avg_gpa, 
        AVG(gre) as avg_gre, 
        AVG(gre_v) as avg_gre_v, 
        AVG(gre_aw) as avg_gre_aw 
    FROM applicants 
    WHERE gpa IS NOT NULL OR gre IS NOT NULL OR gre_v IS NOT NULL OR gre_aw IS NOT NULL;
    """
    cur.execute(query)
    averages = cur.fetchone()
    cur.close()
    conn.close()
    # averages will be a tuple (avg_gpa, avg_gre, avg_gre_v, avg_gre_aw)
    return averages, query


def question_4_avg_gpa_american_fall_2024():
    """What is their average GPA of American students in Fall 2024?"""
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
        SELECT AVG(gpa) 
        FROM applicants 
        WHERE us_or_international = 'American' 
        AND term = 'Fall 2024' 
        AND gpa IS NOT NULL;
    """
    cur.execute(query)
    avg_gpa = cur.fetchone()[0]
    cur.close()
    conn.close()
    return avg_gpa, query


def question_5_fall_2024_acceptance_percentage():
    """What percent of entries for Fall 2024 are Acceptances (to two decimal places)?"""
    conn = get_db_connection()
    cur = conn.cursor()

    query_acceptances = """
    SELECT COUNT(*) 
    FROM applicants 
    WHERE term = 'Fall 2024' 
    AND status = 'Accepted';
    """
    cur.execute(query_acceptances)
    acceptance_count = cur.fetchone()[0]

    query_total_fall_2024 = """
    SELECT COUNT(*) 
    FROM applicants 
    WHERE term = 'Fall 2024';
    """
    cur.execute(query_total_fall_2024)
    total_fall_2024_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    if total_fall_2024_count == 0:
        return 0.00, query_acceptances + " " + query_total_fall_2024

    percentage = (acceptance_count / total_fall_2024_count) * 100
    return round(percentage, 2), query_acceptances + " " + query_total_fall_2024


def question_6_avg_gpa_accepted_fall_2024():
    """What is the average GPA of applicants who applied for Fall 2024 who are Acceptances?"""
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
    SELECT AVG(gpa) 
    FROM applicants 
    WHERE term = 'Fall 2024' 
    AND status = 'Accepted' 
    AND gpa IS NOT NULL;
    """
    cur.execute(query)
    avg_gpa = cur.fetchone()[0]
    cur.close()
    conn.close()
    return avg_gpa, query


def question_7_jhu_cs_masters_entries():
    """
    How many entries are from applicants who applied to JHU
    for a masters degrees in Computer Science?
    """
    conn = get_db_connection()
    cur = conn.cursor()
    query = """
    SELECT COUNT(*) 
    FROM applicants 
    WHERE program ILIKE '%Johns Hopkins%' 
    AND program ILIKE '%Computer Science%' 
    AND degree = 'Masters';
    """
    cur.execute(query)
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count, query


if __name__ == "__main__":
    print("Establishing database connection and executing queries...")

    try:
        q1_count, q1_query = question_1_fall_2024_entries()
        print(f"1. Fall 2024 Entries: {q1_count}")
        print(f"   Query: {q1_query}\n")

        q2_percentage, q2_query = question_2_international_percentage()
        print(f"2. International Student Percentage: {q2_percentage}%")
        print(f"   Query: {q2_query}\n")

        q3_avgs, q3_query = question_3_average_metrics()
        print(f"3. Average Metrics (GPA, GRE, GRE V, GRE AW): {q3_avgs}")
        print(f"   Query: {q3_query}\n")

        q4_avg_gpa, q4_query = question_4_avg_gpa_american_fall_2024()
        print(f"4. Avg GPA American Students (Fall 2024): {q4_avg_gpa}")
        print(f"   Query: {q4_query}\n")

        q5_percentage, q5_query = question_5_fall_2024_acceptance_percentage()
        print(f"5. Fall 2024 Acceptance Percentage: {q5_percentage}%")
        print(f"   Query: {q5_query}\n")

        q6_avg_gpa, q6_query = question_6_avg_gpa_accepted_fall_2024()
        print(f"6. Avg GPA Accepted Applicants (Fall 2024): {q6_avg_gpa}")
        print(f"   Query: {q6_query}\n")

        q7_count, q7_query = question_7_jhu_cs_masters_entries()
        print(f"7. JHU CS Masters Entries: {q7_count}")
        print(f"   Query: {q7_query}\n")

    except psycopg2.Error as e:
        print(f"Database connection error or query error: {e}")
        print(
            """
            Please ensure your PostgreSQL server is running, credentials are correct, 
            and the table exists with data.
            """
        )
