import matplotlib.pyplot as plt


def create_summary_chart(report_data):

    labels = [
        "Functions",
        "Classes",
        "Imports"
    ]

    values = [
        report_data["functions"],
        report_data["classes"],
        report_data["imports"]
    ]

    plt.figure(figsize=(6, 4))

    plt.bar(labels, values)

    plt.title("Project Summary")

    plt.xlabel("Category")

    plt.ylabel("Count")

    plt.savefig("summary_chart.png")

    plt.close()

    print("Summary chart generated.")