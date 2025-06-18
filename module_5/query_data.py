"""
This module contains the functions to query the database and return the results.
"""

import psycopg2
from psycopg2 import sql

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

    # Prepare the query using SQL composition
    query = sql.SQL(
        """
        SELECT COUNT(*) 
        FROM {} 
        WHERE {} = {} 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("applicants"), sql.Identifier("term"), sql.Literal("Fall 2024")
    )

    # Execute the query
    cur.execute(query)
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count, query.as_string(conn)


def question_2_international_percentage():
    """
    What percentage of entries are from international
    students (not American or Other) (to two decimal places)?
    """
    conn = get_db_connection()
    cur = conn.cursor()

    # Prepare international count query
    query_international = sql.SQL(
        """
        SELECT COUNT(*) 
        FROM {} 
        WHERE {} = {} 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("applicants"),
        sql.Identifier("us_or_international"),
        sql.Literal("International"),
    )

    # Prepare total count query
    query_total = sql.SQL(
        """
        SELECT COUNT(*) 
        FROM {} 
        LIMIT 1000
    """
    ).format(sql.Identifier("applicants"))

    # Execute queries
    cur.execute(query_international)
    international_count = cur.fetchone()[0]

    cur.execute(query_total)
    total_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    if total_count == 0:
        return (
            0.00,
            f"{query_international.as_string(conn)} {query_total.as_string(conn)}",
        )

    percentage = (international_count / total_count) * 100
    return (
        round(percentage, 2),
        f"{query_international.as_string(conn)} {query_total.as_string(conn)}",
    )


def question_3_average_metrics():
    """What is the average GPA, GRE, GRE V, GRE AW of applicants who provide these metrics?"""
    conn = get_db_connection()
    cur = conn.cursor()

    # Prepare the query
    query = sql.SQL(
        """
        SELECT 
            AVG({}) as avg_gpa, 
            AVG({}) as avg_gre, 
            AVG({}) as avg_gre_v, 
            AVG({}) as avg_gre_aw 
        FROM {} 
        WHERE {} IS NOT NULL 
            OR {} IS NOT NULL 
            OR {} IS NOT NULL 
            OR {} IS NOT NULL 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("gpa"),
        sql.Identifier("gre"),
        sql.Identifier("gre_v"),
        sql.Identifier("gre_aw"),
        sql.Identifier("applicants"),
        sql.Identifier("gpa"),
        sql.Identifier("gre"),
        sql.Identifier("gre_v"),
        sql.Identifier("gre_aw"),
    )

    # Execute the query
    cur.execute(query)
    averages = cur.fetchone()
    cur.close()
    conn.close()
    return averages, query.as_string(conn)


def question_4_avg_gpa_american_fall_2024():
    """What is their average GPA of American students in Fall 2024?"""
    conn = get_db_connection()
    cur = conn.cursor()

    # Prepare the query
    query = sql.SQL(
        """
        SELECT AVG({}) 
        FROM {} 
        WHERE {} = {} 
            AND {} = {} 
            AND {} IS NOT NULL 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("gpa"),
        sql.Identifier("applicants"),
        sql.Identifier("us_or_international"),
        sql.Literal("American"),
        sql.Identifier("term"),
        sql.Literal("Fall 2024"),
        sql.Identifier("gpa"),
    )

    # Execute the query
    cur.execute(query)
    avg_gpa = cur.fetchone()[0]
    cur.close()
    conn.close()
    return avg_gpa, query.as_string(conn)


def question_5_fall_2024_acceptance_percentage():
    """What percent of entries for Fall 2024 are Acceptances (to two decimal places)?"""
    conn = get_db_connection()
    cur = conn.cursor()

    # Prepare acceptance count query
    query_acceptances = sql.SQL(
        """
        SELECT COUNT(*) 
        FROM {} 
        WHERE {} = {} 
            AND {} = {} 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("applicants"),
        sql.Identifier("term"),
        sql.Literal("Fall 2024"),
        sql.Identifier("status"),
        sql.Literal("Accepted"),
    )

    # Prepare total count query
    query_total_fall_2024 = sql.SQL(
        """
        SELECT COUNT(*) 
        FROM {} 
        WHERE {} = {} 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("applicants"), sql.Identifier("term"), sql.Literal("Fall 2024")
    )

    # Execute queries
    cur.execute(query_acceptances)
    acceptance_count = cur.fetchone()[0]

    cur.execute(query_total_fall_2024)
    total_fall_2024_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    if total_fall_2024_count == 0:
        return (
            0.00,
            f"{query_acceptances.as_string(conn)} {query_total_fall_2024.as_string(conn)}",
        )

    percentage = (acceptance_count / total_fall_2024_count) * 100
    return (
        round(percentage, 2),
        f"{query_acceptances.as_string(conn)} {query_total_fall_2024.as_string(conn)}",
    )


def question_6_avg_gpa_accepted_fall_2024():
    """What is the average GPA of applicants who applied for Fall 2024 who are Acceptances?"""
    conn = get_db_connection()
    cur = conn.cursor()

    # Prepare the query
    query = sql.SQL(
        """
        SELECT AVG({}) 
        FROM {} 
        WHERE {} = {} 
            AND {} = {} 
            AND {} IS NOT NULL 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("gpa"),
        sql.Identifier("applicants"),
        sql.Identifier("term"),
        sql.Literal("Fall 2024"),
        sql.Identifier("status"),
        sql.Literal("Accepted"),
        sql.Identifier("gpa"),
    )

    # Execute the query
    cur.execute(query)
    avg_gpa = cur.fetchone()[0]
    cur.close()
    conn.close()
    return avg_gpa, query.as_string(conn)


def question_7_jhu_cs_masters_entries():
    """
    How many entries are from applicants who applied to JHU
    for a masters degrees in Computer Science?
    """
    conn = get_db_connection()
    cur = conn.cursor()

    # Prepare the query
    query = sql.SQL(
        """
        SELECT COUNT(*) 
        FROM {} 
        WHERE {} ILIKE {} 
            AND {} ILIKE {} 
            AND {} = {} 
        LIMIT 1000
    """
    ).format(
        sql.Identifier("applicants"),
        sql.Identifier("program"),
        sql.Literal("%Johns Hopkins%"),
        sql.Identifier("program"),
        sql.Literal("%Computer Science%"),
        sql.Identifier("degree"),
        sql.Literal("Masters"),
    )

    # Execute the query
    cur.execute(query)
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count, query.as_string(conn)


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
