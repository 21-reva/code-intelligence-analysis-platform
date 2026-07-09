import ast


def detect_inheritance(code):

    tree = ast.parse(code)

    inheritance = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):

            for base in node.bases:

                if isinstance(base, ast.Name):

                    inheritance.append(
                        (node.name, base.id)
                    )

    return inheritance