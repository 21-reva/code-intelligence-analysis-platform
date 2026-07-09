import ast


def calculate_complexity(code):

    tree = ast.parse(code)

    complexity = 0

    for node in ast.walk(tree):

        if isinstance(node, ast.If):
            complexity += 1

        elif isinstance(node, ast.For):
            complexity += 1

        elif isinstance(node, ast.While):
            complexity += 1

        elif isinstance(node, ast.Try):
            complexity += 1

        elif isinstance(node, ast.With):
            complexity += 1

        elif hasattr(ast, "Match") and isinstance(node, ast.Match):
            complexity += 1

    return complexity