def generate_html_report(report_data):

    dependency_items = ""

    for dependency in report_data["dependencies"]:
        dependency_items += f"<li>{dependency}</li>"

    if dependency_items == "":
        dependency_items = "<li>No dependencies found.</li>"


    unused_items = ""

    for module in report_data["unused_imports"]:
        unused_items += f"<li>{module}</li>"

    if unused_items == "":
        unused_items = "<li>No unused imports found.</li>"


    unused_variable_items = ""

    for variable in report_data["unused_variables"]:
        unused_variable_items += f"<li>{variable}</li>"

    if unused_variable_items == "":
        unused_variable_items = "<li>No unused variables found.</li>"


    bad_name_items = ""

    for name in report_data["bad_function_names"]:
        bad_name_items += f"<li>{name}</li>"

    if bad_name_items == "":
        bad_name_items = "<li>All function names follow snake_case.</li>"


    long_function_items = ""

    for name, size in report_data["long_functions_detected"]:
        long_function_items += f"<li>{name} ({size} lines)</li>"

    if long_function_items == "":
        long_function_items = "<li>No long functions found.</li>"


    docstring_items = ""

    for function in report_data["missing_docstrings"]:
        docstring_items += f"<li>{function}</li>"

    if docstring_items == "":
        docstring_items = "<li>Every function has a docstring.</li>"


    argument_items = ""

    for name, count in report_data["many_argument_functions"]:
        argument_items += f"<li>{name} ({count} arguments)</li>"

    if argument_items == "":
        argument_items = "<li>No functions exceed the argument limit.</li>"


    exception_items = ""

    for line in report_data["empty_exception_handlers"]:
        exception_items += f"<li>Line {line}</li>"

    if exception_items == "":
        exception_items = "<li>No empty exception handlers found.</li>"


    global_variable_items = ""

    for variable in report_data["global_variables"]:
        global_variable_items += f"<li>{variable}</li>"

    if global_variable_items == "":
        global_variable_items = "<li>No global variables found.</li>"


    magic_number_items = ""

    for number in report_data["magic_numbers"]:
        magic_number_items += f"<li>{number}</li>"

    if magic_number_items == "":
        magic_number_items = "<li>No magic numbers found.</li>"


    function_call_items = ""

    for function, count in report_data["function_calls"].items():
        function_call_items += f"<li>{function} : {count}</li>"

    if function_call_items == "":
        function_call_items = "<li>No function calls found.</li>"


    recursive_items = ""

    for function in report_data["recursive_functions"]:
        recursive_items += f"<li>{function}</li>"

    if recursive_items == "":
        recursive_items = "<li>No recursive functions found.</li>"


   
    class_items = ""

    for cls in report_data["classes_without_init"]:
        class_items += f"<li>{cls}</li>"

    if class_items == "":
        class_items = "<li>All classes have __init__() method.</li>"


    
    dead_code_items = ""

    for function in report_data["dead_code"]:
        dead_code_items += f"<li>{function}</li>"

    if dead_code_items == "":
        dead_code_items = "<li>No dead code detected.</li>"

    many_method_items = ""

    for name, count in report_data["many_method_classes"]:

        many_method_items += (f"<li>{name} ({count} methods)</li>")

    if many_method_items == "":

        many_method_items = ("<li>No large classes found.</li>")

    inheritance_items = ""

    for child, parent in report_data["inheritance"]:

        inheritance_items += (f"<li>{child} → {parent}</li>")

    if inheritance_items == "":

        inheritance_items = ("<li>No inheritance detected.</li>")

    lambda_items = ""

    for line in report_data["lambda_functions"]:

        lambda_items += f"<li>Line {line}</li>"

    if lambda_items == "":

        lambda_items = "<li>No lambda functions found.</li>"

    try_items = ""

    for line in report_data["try_without_finally"]:

        try_items += f"<li>Line {line}</li>"

    if try_items == "":

        try_items = "<li>All try blocks contain finally.</li>"

    password_items = ""

    for variable, line in report_data["hardcoded_passwords"]:

        password_items += f"<li>{variable} (Line {line})</li>"

    if password_items == "":

        password_items = "<li>No hardcoded passwords found.</li>"

    large_class_items = ""

    for name, methods in report_data["large_classes"]:

        large_class_items += (f"<li>{name} ({methods} methods)</li>")

    if large_class_items == "":

        large_class_items = ("<li>No large classes found.</li>")

    alias_items = ""

    for module, alias in report_data["import_aliases"]:

        alias_items += (f"<li>{module} → {alias}</li>")

    if alias_items == "":

        alias_items = ("<li>No import aliases found.</li>")


    
    function_complexity_items = ""

    for entry in report_data["function_complexity"]:

        badge_class = "badge-good"
        if entry["rating"] == "Complex":
            badge_class = "badge-warning"
        elif entry["rating"] == "Very Complex":
            badge_class = "badge-bad"

        function_complexity_items += (
            f"<li>{entry['name']} ({entry['file']}, line {entry['line']}) "
            f"— Complexity {entry['complexity']} "
            f"<span class='badge {badge_class}'>{entry['rating']}</span></li>"
        )

    if function_complexity_items == "":
        function_complexity_items = "<li>No functions found to analyze.</li>"


    file_metrics_items = ""

    for f in report_data["file_metrics"]:
        file_metrics_items += (
            f"<li><b>{f['file']}</b> — Lines: {f['total_lines']}, "
            f"Code: {f['code_lines']}, Blank: {f['blank_lines']}, "
            f"Comments: {f['comment_lines']}, Functions: {f['function_count']}, "
            f"Classes: {f['class_count']}, Complexity: {f['total_complexity']}</li>"
        )

    if file_metrics_items == "":
        file_metrics_items = "<li>No file metrics available.</li>"


    
    requirements_items = ""

    for package in report_data["requirements"]:
        requirements_items += f"<li>{package}</li>"

    if requirements_items == "":
        requirements_items = "<li>No third-party packages detected.</li>"


    nested_loop_html = f"""

<div class="section">

<h2>Nested Loop Analysis</h2>

<p>
<b>Maximum Loop Depth:</b>
{report_data["nested_loop_depth"]}
</p>

<p>
{
"Deeply Nested Loops Found"
if report_data["nested_loop_depth"] >= 3
else
"Loop nesting is acceptable."
}
</p>

</div>

"""

    # Lesson 72-74 - summary cards (maintainability, security, health)
    maintainability_score = report_data["maintainability_score"]
    security_report = report_data["security_report"]
    health_report = report_data["health_report"]

    def grade_color(grade):
        colors = {
            "A": "#2ecc71",
            "B": "#82c91e",
            "C": "#f1c40f",
            "D": "#e67e22",
            "F": "#e74c3c"
        }
        return colors.get(grade, "#95a5a6")

    summary_cards_html = f"""

<div class="cards">

<div class="card">
<h3>Overall Health</h3>
<div class="score" style="color:{grade_color(health_report['grade'])}">
{health_report['overall_score']}%
</div>
<div class="grade-badge" style="background:{grade_color(health_report['grade'])}">
Grade {health_report['grade']}
</div>
</div>

<div class="card">
<h3>Maintainability</h3>
<div class="score">{maintainability_score}%</div>
</div>

<div class="card">
<h3>Security Score</h3>
<div class="score">{security_report['score']}%</div>
<div class="status-badge">{security_report['rating']}</div>
</div>

<div class="card">
<h3>Complexity Rating</h3>
<div class="score">{report_data['rating']}</div>
</div>

</div>

"""

    html = f"""

<!DOCTYPE html>

<html>

<head>

<title>Code Analysis Dashboard</title>


<style>

body{{
font-family:Arial;
background:#f4f4f4;
margin:40px;
}}

.section{{
background:white;
padding:20px;
margin-top:20px;
border-radius:10px;
box-shadow:0px 0px 10px gray;
}}

h1{{
text-align:center;
}}

ul{{
padding-left:20px;
}}

.cards{{
display:flex;
flex-wrap:wrap;
gap:20px;
justify-content:center;
margin-top:20px;
}}

.card{{
background:white;
padding:20px;
border-radius:10px;
box-shadow:0px 0px 10px gray;
text-align:center;
min-width:180px;
flex:1;
}}

.card h3{{
margin:0 0 10px 0;
color:#555;
}}

.score{{
font-size:28px;
font-weight:bold;
}}

.grade-badge{{
display:inline-block;
margin-top:10px;
padding:4px 12px;
border-radius:20px;
color:white;
font-weight:bold;
}}

.status-badge{{
display:inline-block;
margin-top:10px;
padding:4px 12px;
border-radius:20px;
background:#eee;
font-weight:bold;
}}

.badge{{
display:inline-block;
padding:2px 8px;
border-radius:12px;
font-size:12px;
margin-left:8px;
color:white;
}}

.badge-good{{
background:#2ecc71;
}}

.badge-warning{{
background:#f1c40f;
color:#333;
}}

.badge-bad{{
background:#e74c3c;
}}

</style>


</head>


<body>


<h1>
Code Analysis Dashboard
</h1>

{summary_cards_html}


<div class="section">

<h2>
Naming Convention Warnings
</h2>

<ul>

{bad_name_items}

</ul>

</div>



<div class="section">

<h2>
Functions Missing Docstrings
</h2>

<ul>

{docstring_items}

</ul>

</div>



<div class="section">

<h2>
Functions With Too Many Arguments
</h2>

<ul>

{argument_items}

</ul>

</div>



<div class="section">

<h2>
Unused Imports
</h2>

<ul>

{unused_items}

</ul>

</div>



<div class="section">

<h2>
Unused Variables
</h2>

<ul>

{unused_variable_items}

</ul>

</div>



<div class="section">

<h2>
Long Functions
</h2>

<ul>

{long_function_items}

</ul>

</div>



<div class="section">

<h2>
Dependencies
</h2>

<ul>

{dependency_items}

</ul>

</div>



{nested_loop_html}




<div class="section">

<h2>
Empty Exception Handlers
</h2>

<ul>

{exception_items}

</ul>

</div>




<div class="section">

<h2>
Global Variables
</h2>

<ul>

{global_variable_items}

</ul>

</div>




<div class="section">

<h2>
Magic Numbers
</h2>

<ul>

{magic_number_items}

</ul>

</div>




<div class="section">

<h2>
Function Call Counts
</h2>

<ul>

{function_call_items}

</ul>

</div>




<div class="section">

<h2>
Recursive Functions
</h2>

<ul>

{recursive_items}

</ul>

</div>




<!-- Lesson 63 -->

<div class="section">

<h2>
Dead Code Detection
</h2>

<ul>

{dead_code_items}

</ul>

</div>





<!-- Lesson 64 -->

<div class="section">

<h2>
Classes Without __init__()
</h2>

<ul>

{class_items}

</ul>

</div>
<div class="section">

<h2>Classes With Too Many Methods</h2>

<ul>

{many_method_items}

</ul>

</div>

<div class="section">

<h2>Inheritance Relationships</h2>

<ul>

{inheritance_items}

</ul>

</div>
<div class="section">

<h2>
Lambda Functions
</h2>

<ul>

{lambda_items}

</ul>

</div>
<div class="section">

<h2>
Try Blocks Without Finally
</h2>

<ul>

{try_items}

</ul>

</div>
<div class="section">

<h2>Hardcoded Passwords</h2>

<ul>

{password_items}

</ul>

</div>
<div class="section">

<h2>
Large Classes
</h2>

<ul>

{large_class_items}

</ul>

</div>
<div class="section">

<h2>Import Aliases</h2>

<ul>

{alias_items}

</ul>

</div>


<!-- Lesson 70 -->
<div class="section">

<h2>Function Complexity Report</h2>

<ul>

{function_complexity_items}

</ul>

</div>


<!-- Lesson 71 -->
<div class="section">

<h2>File-wise Metrics</h2>

<ul>

{file_metrics_items}

</ul>

</div>


<!-- Lesson 76 -->
<div class="section">

<h2>Detected Third-Party Requirements</h2>

<ul>

{requirements_items}

</ul>

</div>


<div class="section">

<h2>
Summary Chart
</h2>


<img src="summary_chart.png" width="600">


</div>




</body>


</html>

"""


    with open("report.html", "w", encoding="utf-8") as file:
        file.write(html)


    print("HTML report generated successfully.")
