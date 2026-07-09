import ast


def find_unused_variables(code):

    tree = ast.parse(code)

    assigned_variables = set()

    used_variables = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):

                    assigned_variables.add(target.id)

        elif isinstance(node, ast.Name):

            if isinstance(node.ctx, ast.Load):

                used_variables.add(node.id)

    unused_variables = sorted(
        assigned_variables - used_variables
    )

    return unused_variables