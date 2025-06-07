import os
import sys

import psycopg2
from flask import Flask, render_template

# Add the parent directory to the Python path to enable imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from query_data import (
    question_1_fall_2024_entries,
    question_2_international_percentage,
    question_3_average_metrics,
    question_4_avg_gpa_american_fall_2024,
    question_5_fall_2024_acceptance_percentage,
    question_6_avg_gpa_accepted_fall_2024,
    question_7_jhu_cs_masters_entries,
)

app = Flask(__name__)


@app.route("/")
def index():
    results = {}
    queries = {}
    error_message = None
    try:
        results["q1"], queries["q1"] = question_1_fall_2024_entries()
        results["q2"], queries["q2"] = question_2_international_percentage()
        avg_metrics, queries["q3"] = question_3_average_metrics()
        if avg_metrics:
            results["q3_avg_gpa"] = avg_metrics[0]
            results["q3_avg_gre"] = avg_metrics[1]
            results["q3_avg_gre_v"] = avg_metrics[2]
            results["q3_avg_gre_aw"] = avg_metrics[3]
        else:
            results["q3_avg_gpa"] = results["q3_avg_gre"] = results["q3_avg_gre_v"] = (
                results["q3_avg_gre_aw"]
            ) = "N/A"

        results["q4"], queries["q4"] = question_4_avg_gpa_american_fall_2024()
        results["q5"], queries["q5"] = question_5_fall_2024_acceptance_percentage()
        results["q6"], queries["q6"] = question_6_avg_gpa_accepted_fall_2024()
        results["q7"], queries["q7"] = question_7_jhu_cs_masters_entries()

    except psycopg2.Error as e:
        error_message = f"Database error: {e}. Please ensure the database is running, accessible, and populated."
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"

    return render_template(
        "index.html", results=results, queries=queries, error_message=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)
