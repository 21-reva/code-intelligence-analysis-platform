import ast

def analyze_code(code):

    tree = ast.parse(code)

    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            function_size = (
                node.end_lineno
                - node.lineno
                + 1
            )

            functions.append(
                (
                    node.name,
                    function_size
                )
            )

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

    return functions, classes, imports