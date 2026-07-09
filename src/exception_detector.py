import ast


def detect_empty_exceptions(code):

    tree = ast.parse(code)

    empty_handlers = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Try):

            for handler in node.handlers:

                if (
                    len(handler.body) == 1
                    and
                    isinstance(handler.body[0], ast.Pass)
                ):

                    empty_handlers.append(handler.lineno)

    return empty_handlers