import ast


def detect_many_arguments(code):

    tree = ast.parse(code)

    functions = []

    LIMIT = 5

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            argument_count = len(node.args.args)

            if argument_count > LIMIT:

                functions.append(
                    (
                        node.name,
                        argument_count
                    )
                )

    return functions