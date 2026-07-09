import ast


def detect_magic_numbers(code):

    tree = ast.parse(code)

    magic_numbers = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Constant):

            if isinstance(node.value, (int, float)):

                if node.value not in (0, 1, -1):

                    magic_numbers.append(node.value)

    return magic_numbers