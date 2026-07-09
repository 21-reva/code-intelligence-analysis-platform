def calculate_metrics(code):

    lines = code.splitlines()

    total_lines = len(lines)

    blank_lines = 0
    comment_lines = 0

    for line in lines:

        if line.strip() == "":
            blank_lines += 1

        elif line.strip().startswith("#"):
            comment_lines += 1

    code_lines = total_lines - blank_lines - comment_lines

    return (
        total_lines,
        blank_lines,
        comment_lines,
        code_lines
    )