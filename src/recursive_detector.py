import ast


class RecursiveVisitor(ast.NodeVisitor):

    def __init__(self):
        self.recursive_functions = []

    def visit_FunctionDef(self, node):

        for child in ast.walk(node):

            if isinstance(child, ast.Call):

                if isinstance(child.func, ast.Name):

                    if child.func.id == node.name:
                        self.recursive_functions.append(node.name)

        self.generic_visit(node)


def detect_recursive_functions(code):

    tree = ast.parse(code)

    visitor = RecursiveVisitor()

    visitor.visit(tree)

    return visitor.recursive_functions