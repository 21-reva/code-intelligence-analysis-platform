import ast


def detect_global_variables(code):

    tree = ast.parse(code)

    globals_found = []

    for node in tree.body:

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):

                    globals_found.append(target.id)

    return globals_found