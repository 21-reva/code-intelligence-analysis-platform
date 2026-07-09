import ast


def find_duplicate_functions(code):

    tree = ast.parse(code)

    seen = {}

    duplicates = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            structure = ast.dump(node)

            if structure in seen:

                duplicates.append(node.name)

            else:

                seen[structure] = node.name

    return duplicates