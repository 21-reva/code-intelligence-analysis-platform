import ast
import math


def _collect_halstead_tokens(tree):
    operators = []
    operands = []
    operator_nodes = (ast.operator, ast.boolop, ast.unaryop, ast.cmpop)

    for node in ast.walk(tree):
        if isinstance(node, operator_nodes):
            operators.append(type(node).__name__)
        elif isinstance(node, ast.Name):
            operands.append(node.id)
        elif isinstance(node, ast.Constant):
            operands.append(repr(node.value))

    return operators, operands


def calculate_halstead_volume(code):
    """
    Simplified Halstead Volume calculation used to feed the
    maintainability index formula.
    """
    tree = ast.parse(code)
    operators, operands = _collect_halstead_tokens(tree)

    n1 = len(set(operators))
    n2 = len(set(operands))
    N1 = len(operators)
    N2 = len(operands)

    vocabulary = n1 + n2
    length = N1 + N2

    if vocabulary == 0 or length == 0:
        return 0

    return length * math.log2(vocabulary)


def calculate_maintainability_index(code, complexity):
    """
    Calculates a maintainability index (0-100).
    Based on a simplified version of the standard Microsoft formula:
    MI = 171 - 5.2*ln(V) - 0.23*CC - 16.2*ln(LOC), normalized to 0-100.

    'complexity' should be the total cyclomatic complexity for this file
    (you already compute this with calculate_complexity(code)).
    """
    lines = [line for line in code.split("\n") if line.strip() != ""]
    loc = len(lines) if lines else 1

    volume = calculate_halstead_volume(code)
    if volume == 0:
        volume = 1

    raw_mi = 171 - 5.2 * math.log(volume) - 0.23 * complexity - 16.2 * math.log(loc)
    normalized_mi = max(0, min(100, (raw_mi * 100) / 171))

    return round(normalized_mi, 2)


def get_maintainability_rating(mi_score):
    if mi_score >= 85:
        return "Highly Maintainable"
    elif mi_score >= 65:
        return "Moderately Maintainable"
    elif mi_score >= 40:
        return "Difficult to Maintain"
    else:
        return "Very Difficult to Maintain"


if __name__ == "__main__":
    sample = """
def add(a, b):
    return a + b

def process(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result
"""
    complexity = 5
    mi = calculate_maintainability_index(sample, complexity)
    print(mi, get_maintainability_rating(mi))
