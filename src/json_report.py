import json


def generate_json_report(report_data):

    with open("report.json", "w", encoding="utf-8") as file:

        json.dump(
            report_data,
            file,
            indent=4
        )

    print()

    print("JSON report generated successfully.")