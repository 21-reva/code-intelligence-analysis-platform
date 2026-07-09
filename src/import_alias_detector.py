import ast


def detect_import_aliases(code):

    tree = ast.parse(code)

    aliases = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:

                if alias.asname:

                    aliases.append(
                        (
                            alias.name,
                            alias.asname
                        )
                    )

    return aliases