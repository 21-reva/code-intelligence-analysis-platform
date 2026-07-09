def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def complexity_to_score(total_complexity):
    """
    Helper: converts a raw complexity number (from calculate_complexity)
    into a 0-100 friendly score - lower complexity = higher score.
    """
    if total_complexity <= 10:
        return 100
    elif total_complexity <= 25:
        return 80
    elif total_complexity <= 50:
        return 60
    else:
        return max(0, 100 - total_complexity)


def calculate_health_score(complexity_rating_score, maintainability_score, security_score,
                            duplicate_count=0, dead_code_count=0):
    """
    Combines complexity, maintainability, security, and code cleanliness
    into one overall health score (0-100) and letter grade.
    """
    weights = {
        "complexity": 0.25,
        "maintainability": 0.35,
        "security": 0.30,
        "cleanliness": 0.10
    }

    cleanliness_score = 100
    cleanliness_score -= duplicate_count * 3
    cleanliness_score -= dead_code_count * 2
    cleanliness_score = max(0, min(100, cleanliness_score))

    overall = (
        complexity_rating_score * weights["complexity"] +
        maintainability_score * weights["maintainability"] +
        security_score * weights["security"] +
        cleanliness_score * weights["cleanliness"]
    )
    overall = round(overall, 2)

    return {
        "overall_score": overall,
        "grade": get_grade(overall),
        "breakdown": {
            "complexity_score": complexity_rating_score,
            "maintainability_score": maintainability_score,
            "security_score": security_score,
            "cleanliness_score": cleanliness_score
        }
    }


if __name__ == "__main__":
    c_score = complexity_to_score(15)
    result = calculate_health_score(
        complexity_rating_score=c_score,
        maintainability_score=78,
        security_score=90,
        duplicate_count=2,
        dead_code_count=1
    )
    print(result)
