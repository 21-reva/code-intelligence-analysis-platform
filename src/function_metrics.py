def analyze_function_sizes(functions):

    if len(functions) == 0:
        return None

    largest = max(functions, key=lambda item: item[1])

    smallest = min(functions, key=lambda item: item[1])

    total_size = 0

    for name, size in functions:
        total_size += size

    average = total_size / len(functions)

    long_functions = []

    for name, size in functions:

        if size > 30:
            long_functions.append((name, size))

    return (
        largest,
        smallest,
        average,
        long_functions
    )