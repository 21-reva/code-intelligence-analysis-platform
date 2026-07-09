import ast


def get_loop_depth(node):

    maximum = 1

    for child in ast.iter_child_nodes(node):

        if isinstance(child, (ast.For, ast.While)):

            maximum = max(
                maximum,
                1 + get_loop_depth(child)
            )

        else:

            maximum = max(
                maximum,
                get_loop_depth(child)
            )

    return maximum


def detect_nested_loops(code):

    tree = ast.parse(code)

    maximum_depth = 0

    for node in ast.walk(tree):

        if isinstance(node, (ast.For, ast.While)):

            maximum_depth = max(
                maximum_depth,
                get_loop_depth(node)
            )

    return maximum_depth