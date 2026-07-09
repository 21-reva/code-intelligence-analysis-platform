import ast


def get_complexity_rating(complexity):
    if complexity <= 5:
        return "Simple"
    elif complexity <= 10:
        return "Moderate"
    elif complexity <= 20:
        return "Complex"
    else:
        return "Very Complex"


def analyze_function_complexity(code):
    """
    Calculates cyclomatic complexity for every function in the code.
    Returns a list of dicts: {name, line, complexity, rating}
    """
    tree = ast.parse(code)
    function_reports = []

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            complexity = 1

            for child in ast.walk(node):
                if isinstance(child, (ast.If, ast.For, ast.AsyncFor, ast.While,
                                       ast.Try, ast.ExceptHandler, ast.With,
                                       ast.AsyncWith, ast.Assert)):
                    complexity += 1
                elif isinstance(child, ast.BoolOp):
                    complexity += len(child.values) - 1
                elif isinstance(child, ast.comprehension):
                    complexity += len(child.ifs)

            function_reports.append({
                "name": node.name,
                "line": node.lineno,
                "complexity": complexity,
                "rating": get_complexity_rating(complexity)
            })

    return function_reports


if __name__ == "__main__":
    sample = """
def simple():
    return 1

def complex_func(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(i)
            else:
                print(-i)
    else:
        try:
            return 1 / x
        except ZeroDivisionError:
            return 0
"""
    for report in analyze_function_complexity(sample):
        print(report)