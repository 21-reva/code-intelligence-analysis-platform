import ast


def detect_try_without_finally(code):

    tree = ast.parse(code)

    missing_finally = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Try):

            if len(node.finalbody) == 0:

                missing_finally.append(node.lineno)

    return missing_finally