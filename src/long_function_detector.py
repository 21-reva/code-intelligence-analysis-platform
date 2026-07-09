import ast


def detect_long_functions(code):

    tree = ast.parse(code)

    long_functions = []

    LIMIT = 40

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            function_size = (
                node.end_lineno
                - node.lineno
                + 1
            )

            if function_size > LIMIT:

                long_functions.append(
                    (
                        node.name,
                        function_size
                    )
                )

    return long_functions