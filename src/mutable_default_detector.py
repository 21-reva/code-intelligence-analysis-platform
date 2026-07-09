import ast


def detect_mutable_defaults(code):

    tree = ast.parse(code)

    mutable_functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            for default in node.args.defaults:

                if isinstance(default, (ast.List, ast.Dict, ast.Set)):

                    mutable_functions.append(
                        (node.name, node.lineno)
                    )

    return mutable_functions