import ast
from function_complexity import analyze_function_complexity


def calculate_file_metrics(file_path, code):
    """
    Calculates a set of statistics for a single file.
    Returns a dict.
    """
    lines = code.split("\n")
    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if line.strip() == "")
    comment_lines = sum(1 for line in lines if line.strip().startswith("#"))
    code_lines = total_lines - blank_lines - comment_lines

    tree = ast.parse(code)
    function_count = sum(
        1 for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    )
    class_count = sum(1 for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
    import_count = sum(
        1 for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
    )

    function_reports = analyze_function_complexity(code)
    file_complexity = sum(f["complexity"] for f in function_reports) if function_reports else 0
    avg_complexity = round(file_complexity / len(function_reports), 2) if function_reports else 0

    return {
        "file": file_path,
        "total_lines": total_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "code_lines": code_lines,
        "function_count": function_count,
        "class_count": class_count,
        "import_count": import_count,
        "total_complexity": file_complexity,
        "average_function_complexity": avg_complexity
    }


if __name__ == "__main__":
    sample = "def f():\n    # comment\n    return 1\n\n"
    print(calculate_file_metrics("sample.py", sample))
