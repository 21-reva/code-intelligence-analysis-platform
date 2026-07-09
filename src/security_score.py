def get_security_rating(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Needs Attention"
    else:
        return "Poor"


def calculate_security_score(hardcoded_passwords=None, empty_exception_handlers=None,
                              global_variables=None, dead_code=None, unused_variables=None):
    """
    Calculates a security score out of 100 based on issues already
    detected by your other modules (hardcoded_password_detector,
    exception_detector, global_variable_detector, dead_code_detector,
    unused_variables). Pass in the lists you already collect in main.py.
    """
    hardcoded_passwords = hardcoded_passwords or []
    empty_exception_handlers = empty_exception_handlers or []
    global_variables = global_variables or []
    dead_code = dead_code or []
    unused_variables = unused_variables or []

    score = 100
    score -= len(hardcoded_passwords) * 15
    score -= len(empty_exception_handlers) * 5
    score -= len(global_variables) * 3
    score -= len(dead_code) * 2
    score -= len(unused_variables) * 1
    score = max(0, min(100, score))

    return {
        "score": score,
        "rating": get_security_rating(score),
        "issues_found": {
            "hardcoded_passwords": len(hardcoded_passwords),
            "empty_exception_handlers": len(empty_exception_handlers),
            "global_variables": len(global_variables),
            "dead_code": len(dead_code),
            "unused_variables": len(unused_variables)
        }
    }


if __name__ == "__main__":
    result = calculate_security_score(
        hardcoded_passwords=["password = '123'"],
        empty_exception_handlers=["except: pass"],
        global_variables=["counter"]
    )
    print(result)
