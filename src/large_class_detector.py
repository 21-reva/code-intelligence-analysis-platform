import ast


def detect_large_classes(code):

    tree = ast.parse(code)

    large_classes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):

            method_count = 0

            for item in node.body:

                if isinstance(item, ast.FunctionDef):

                    method_count += 1

            if method_count > 7:

                large_classes.append(
                    (
                        node.name,
                        method_count
                    )
                )

    return large_classes