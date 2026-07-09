import ast


def detect_lambda_functions(code):

    tree = ast.parse(code)

    lambda_lines = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Lambda):

            lambda_lines.append(node.lineno)

    return lambda_lines