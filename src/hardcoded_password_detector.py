import ast


def detect_hardcoded_passwords(code):

    tree = ast.parse(code)

    hardcoded_passwords = []

    keywords = [
        "password",
        "passwd",
        "pwd",
        "secret",
        "token",
        "apikey",
        "api_key"
    ]

    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):

                    variable = target.id.lower()

                    if any(word in variable for word in keywords):

                        if isinstance(node.value, ast.Constant):

                            if isinstance(node.value.value, str):

                                hardcoded_passwords.append(
                                    (target.id, node.lineno)
                                )

    return hardcoded_passwords