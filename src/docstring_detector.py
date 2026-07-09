import ast


def detect_missing_docstrings(code):

    tree = ast.parse(code)

    missing_docstrings = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            if ast.get_docstring(node) is None:

                missing_docstrings.append(node.name)

    return missing_docstrings