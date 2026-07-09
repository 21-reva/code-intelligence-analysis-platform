import ast


def find_unused_imports(code):

    tree = ast.parse(code)

    imported_modules = []

    used_modules = set()

    unused_modules = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:

                imported_modules.append(alias.name)

        elif isinstance(node, ast.ImportFrom):

            imported_modules.append(node.module)

        elif isinstance(node, ast.Name):

            used_modules.add(node.id)

    for module in imported_modules:

        module_name = module.split(".")[0]

        if module_name not in used_modules:

            unused_modules.append(module)

    return unused_modules