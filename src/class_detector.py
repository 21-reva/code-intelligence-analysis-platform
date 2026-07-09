import ast


def detect_classes_without_init(code):

    tree = ast.parse(code)

    classes_without_init = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):

            has_constructor = False

            for item in node.body:

                if isinstance(item, ast.FunctionDef):

                    if item.name == "__init__":

                        has_constructor = True
                        break

            if not has_constructor:

                classes_without_init.append(node.name)

    return classes_without_init