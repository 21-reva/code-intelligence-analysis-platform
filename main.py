import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))



from file_reader import get_python_files
from reader import read_file
from analyzer import analyze_code
from report_generator import generate_report
from metrics import calculate_metrics
from function_metrics import analyze_function_sizes
from complexity import calculate_complexity
from duplicate_detector import find_duplicate_functions
from todo_detector import detect_tasks
from dependency_graph import build_dependency_graph
from unused_imports import find_unused_imports
from unused_variables import find_unused_variables
from naming_checker import check_function_names
from long_function_detector import detect_long_functions
from docstring_detector import detect_missing_docstrings
from argument_detector import detect_many_arguments
from nested_loop_detector import detect_nested_loops
from exception_detector import detect_empty_exceptions
from global_variable_detector import detect_global_variables
from magic_number_detector import detect_magic_numbers
from json_report import generate_json_report
from html_report import generate_html_report
from charts import create_summary_chart
from function_call_counter import count_function_calls
from recursive_detector import detect_recursive_functions
from class_detector import detect_classes_without_init
from dead_code_detector import detect_dead_code
from many_methods_detector import detect_many_methods
from inheritance_detector import detect_inheritance
from lambda_detector import detect_lambda_functions
from try_finally_detector import detect_try_without_finally
from hardcoded_password_detector import detect_hardcoded_passwords
from large_class_detector import detect_large_classes
from import_alias_detector import detect_import_aliases

# Lesson 70-76 additions
from function_complexity import analyze_function_complexity
from file_metrics import calculate_file_metrics
from maintainability_index import calculate_maintainability_index
from security_score import calculate_security_score
from health_score import calculate_health_score, complexity_to_score
from requirements_generator import generate_requirements
from readme_generator import generate_readme

project_path = "sample_projects"

python_files = get_python_files(project_path)

all_functions = []
all_classes = []
all_imports = []
all_duplicates = []
all_dependencies = []
all_unused_imports = []
all_unused_variables = []
all_bad_function_names = []
all_detected_long_functions = []
all_missing_docstrings = []
all_many_argument_functions = []
all_empty_exception_handlers = []
all_global_variables = []
all_magic_numbers = []
all_function_calls = {}
all_recursive_functions = []
all_classes_without_init = []
all_many_method_classes = []
all_inheritance = []
all_lambda_functions = []
all_dead_code = []
all_try_without_finally = []
all_hardcoded_passwords = []
all_large_classes = []
all_import_aliases = []
all_function_complexity = []
all_file_metrics = []
maintainability_scores = []


total_project_lines = 0
total_blank_lines = 0
total_comment_lines = 0
total_code_lines = 0

total_complexity = 0

total_todo = 0
total_fixme = 0
total_bug = 0

maximum_nested_depth = 0

for file in python_files:

    code = read_file(file)

    functions, classes, imports = analyze_code(code)

    total, blank, comments, code_lines = calculate_metrics(code)

    complexity = calculate_complexity(code)

    duplicates = find_duplicate_functions(code)

    todo, fixme, bug = detect_tasks(code)

    dependencies = build_dependency_graph(code)

    unused = find_unused_imports(code)

    unused_variables = find_unused_variables(code)

    bad_names = check_function_names(code)

    detected_long_functions = detect_long_functions(code)

    missing_docstrings = detect_missing_docstrings(code)

    many_argument_functions = detect_many_arguments(code)

    nested_depth = detect_nested_loops(code)

    empty_exception_handlers = detect_empty_exceptions(code)

    global_variables = detect_global_variables(code)

    magic_numbers = detect_magic_numbers(code)

    function_calls = count_function_calls(code)

    recursive_functions = detect_recursive_functions(code)

    classes_without_init = detect_classes_without_init(code)

    many_method_classes = detect_many_methods(code)

    lambda_functions = detect_lambda_functions(code)

    inheritance = detect_inheritance(code)

    dead_code = detect_dead_code(code)

    try_without_finally = detect_try_without_finally(code)

    hardcoded_passwords = detect_hardcoded_passwords(code)

    large_classes = detect_large_classes(code)

    import_aliases = detect_import_aliases(code)

    function_complexity = analyze_function_complexity(code)

    for entry in function_complexity:
        entry["file"] = file

    
    file_metrics = calculate_file_metrics(file, code)

   
    file_maintainability = calculate_maintainability_index(code, complexity)


    maximum_nested_depth = max(
        maximum_nested_depth,
        nested_depth
    )

    total_complexity += complexity

    total_todo += todo
    total_fixme += fixme
    total_bug += bug

    all_functions.extend(functions)
    all_classes.extend(classes)
    all_imports.extend(imports)
    all_duplicates.extend(duplicates)
    all_dependencies.extend(dependencies)
    all_unused_imports.extend(unused)
    all_unused_variables.extend(unused_variables)
    all_bad_function_names.extend(bad_names)
    all_detected_long_functions.extend(detected_long_functions)
    all_missing_docstrings.extend(missing_docstrings)
    all_many_argument_functions.extend(many_argument_functions)
    all_empty_exception_handlers.extend(empty_exception_handlers)
    all_global_variables.extend(global_variables)
    all_magic_numbers.extend(magic_numbers)
    all_recursive_functions.extend(recursive_functions)
    all_classes_without_init.extend(classes_without_init)
    all_many_method_classes.extend(many_method_classes)
    all_lambda_functions.extend(lambda_functions)
    all_inheritance.extend(inheritance)
    all_try_without_finally.extend(try_without_finally)
    all_dead_code.extend(dead_code)
    all_hardcoded_passwords.extend(hardcoded_passwords)
    all_large_classes.extend(large_classes)
    all_import_aliases.extend(import_aliases)

    all_function_complexity.extend(function_complexity)
    all_file_metrics.append(file_metrics)
    maintainability_scores.append(file_maintainability)

    for function, count in function_calls.items():

        if function not in all_function_calls:
            all_function_calls[function] = 0

        all_function_calls[function] += count

    total_project_lines += total
    total_blank_lines += blank
    total_comment_lines += comments
    total_code_lines += code_lines

(
    largest_function,
    smallest_function,
    average_function_size,
    long_functions
) = analyze_function_sizes(all_functions)

unique_dependencies = sorted(set(all_dependencies))
unique_unused_imports = sorted(set(all_unused_imports))
unique_unused_variables = sorted(set(all_unused_variables))
unique_bad_function_names = sorted(set(all_bad_function_names))
unique_long_functions = sorted(set(all_detected_long_functions))
unique_missing_docstrings = sorted(set(all_missing_docstrings))
unique_many_argument_functions = sorted(set(all_many_argument_functions))
unique_empty_exception_handlers = sorted(set(all_empty_exception_handlers))
unique_global_variables = sorted(set(all_global_variables))
unique_magic_numbers = sorted(set(all_magic_numbers))
unique_recursive_functions = sorted(set(all_recursive_functions))
unique_classes_without_init = sorted(set(all_classes_without_init))
unique_many_method_classes = sorted(set(all_many_method_classes))
unique_lambda_functions = sorted(set(all_lambda_functions))
unique_inheritance = sorted(set(all_inheritance))
unique_try_without_finally = sorted(set(all_try_without_finally))
unique_dead_code = sorted(set(all_dead_code))
unique_hardcoded_passwords = sorted(set(all_hardcoded_passwords))
unique_large_classes = sorted(set(all_large_classes))
unique_import_aliases = sorted(set(all_import_aliases))

if total_complexity <= 10:
    rating = "Excellent"
elif total_complexity <= 25:
    rating = "Good"
elif total_complexity <= 50:
    rating = "Needs Improvement"
else:
    rating = "Complex"


avg_maintainability = (
    round(sum(maintainability_scores) / len(maintainability_scores), 2)
    if maintainability_scores else 0
)


security_report = calculate_security_score(
    hardcoded_passwords=unique_hardcoded_passwords,
    empty_exception_handlers=unique_empty_exception_handlers,
    global_variables=unique_global_variables,
    dead_code=unique_dead_code,
    unused_variables=unique_unused_variables
)


health_report = calculate_health_score(
    complexity_rating_score=complexity_to_score(total_complexity),
    maintainability_score=avg_maintainability,
    security_score=security_report["score"],
    duplicate_count=len(all_duplicates),
    dead_code_count=len(unique_dead_code)
)


requirements_list = generate_requirements(python_files, read_file)

generate_report(
    all_functions,
    all_classes,
    all_imports,
    total_project_lines,
    total_blank_lines,
    total_comment_lines,
    total_code_lines,
    largest_function,
    smallest_function,
    average_function_size,
    long_functions,
    total_complexity,
    rating,
    all_duplicates,
    total_todo,
    total_fixme,
    total_bug,
    unique_dependencies,
    unique_unused_imports,
    unique_unused_variables,
    unique_bad_function_names,
    unique_long_functions,
    unique_missing_docstrings,
    unique_many_argument_functions,
    maximum_nested_depth,
    unique_empty_exception_handlers,
    unique_global_variables,
    unique_magic_numbers,
    all_function_calls,
    unique_recursive_functions,
    unique_classes_without_init,
    unique_dead_code,
    unique_many_method_classes,
    unique_inheritance,
    unique_lambda_functions,
    unique_try_without_finally,
    unique_hardcoded_passwords,
    unique_large_classes,
    unique_import_aliases,
    all_function_complexity,
    all_file_metrics,
    avg_maintainability,
    security_report,
    health_report,
    requirements_list
)

report_data = {
    "functions": len(all_functions),
    "classes": len(all_classes),
    "imports": len(all_imports),
    "total_lines": total_project_lines,
    "code_lines": total_code_lines,
    "blank_lines": total_blank_lines,
    "comment_lines": total_comment_lines,
    "largest_function": largest_function,
    "smallest_function": smallest_function,
    "average_function_size": average_function_size,
    "long_functions": long_functions,
    "complexity": total_complexity,
    "rating": rating,
    "duplicate_functions": all_duplicates,
    "todo_comments": total_todo,
    "fixme_comments": total_fixme,
    "bug_comments": total_bug,
    "dependencies": unique_dependencies,
    "unused_imports": unique_unused_imports,
    "unused_variables": unique_unused_variables,
    "bad_function_names": unique_bad_function_names,
    "long_functions_detected": unique_long_functions,
    "missing_docstrings": unique_missing_docstrings,
    "many_argument_functions": unique_many_argument_functions,
    "nested_loop_depth": maximum_nested_depth,
    "empty_exception_handlers": unique_empty_exception_handlers,
    "global_variables": unique_global_variables,
    "magic_numbers": unique_magic_numbers,
    "function_calls": all_function_calls,
    "recursive_functions": unique_recursive_functions,
    "dead_code": unique_dead_code,
    "classes_without_init": unique_classes_without_init,
    "many_method_classes": unique_many_method_classes,
    "inheritance": unique_inheritance,
    "lambda_functions": unique_lambda_functions,
    "try_without_finally": unique_try_without_finally,
    "hardcoded_passwords": unique_hardcoded_passwords,
    "large_classes": unique_large_classes,
    "import_aliases": unique_import_aliases,

    
    "function_complexity": all_function_complexity,
    "file_metrics": all_file_metrics,
    "maintainability_score": avg_maintainability,
    "security_report": security_report,
    "health_report": health_report,
    "requirements": requirements_list
}

generate_json_report(report_data)

generate_html_report(report_data)

generate_readme(report_data)

create_summary_chart(report_data)
