import ast


def count_function_calls(code):

    tree = ast.parse(code)

    call_counts = {}

    for node in ast.walk(tree):

        if isinstance(node, ast.Call):

            if isinstance(node.func, ast.Name):

                name = node.func.id

                if name not in call_counts:
                    call_counts[name] = 0

                call_counts[name] += 1

    return call_counts