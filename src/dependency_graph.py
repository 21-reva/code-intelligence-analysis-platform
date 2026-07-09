import ast


def build_dependency_graph(code):

    tree = ast.parse(code)

    dependencies = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:

                dependencies.append(alias.name)

        elif isinstance(node, ast.ImportFrom):

            if node.module is not None:

                dependencies.append(node.module)

    return dependencies