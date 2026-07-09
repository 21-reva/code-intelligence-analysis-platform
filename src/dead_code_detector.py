import ast


def detect_dead_code(code):

    tree = ast.parse(code)

    dead_lines = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):

            body = node.body

            unreachable = False

            for statement in body:

                if unreachable:

                    dead_lines.append(statement.lineno)

                if isinstance(
                    statement,
                    (
                        ast.Return,
                        ast.Raise,
                        ast.Break,
                        ast.Continue
                    )
                ):

                    unreachable = True

    return dead_lines