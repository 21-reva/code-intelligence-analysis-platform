import ast


def detect_many_methods(code):

    tree = ast.parse(code)

    classes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):

            method_count = 0

            for item in node.body:

                if isinstance(item, ast.FunctionDef):

                    method_count += 1

            if method_count > 5:

                classes.append(
                    (
                        node.name,
                        method_count
                    )
                )

    return classes