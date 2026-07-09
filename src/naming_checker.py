import ast
import re


def check_function_names(code):

    tree = ast.parse(code)

    bad_function_names = []

    pattern = r"^[a-z_][a-z0-9_]*$"

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            if not re.match(pattern, node.name):

                bad_function_names.append(node.name)

    return bad_function_names