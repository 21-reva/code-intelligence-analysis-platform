def detect_tasks(code):

    todo = 0
    fixme = 0
    bug = 0

    for line in code.splitlines():

        if "TODO" in line:
            todo += 1

        if "FIXME" in line:
            fixme += 1

        if "BUG" in line:
            bug += 1

    return (
        todo,
        fixme,
        bug
    )