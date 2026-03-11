def calculate_priority(case):
    score = 0
    reasons = []

    importance = case.get("importance", 1)
    case_type = case.get("type", "").lower()
    status = case.get("status", "").lower()
    hearing_days = case.get("hearing_days", 30)

    score += importance * 10
    reasons.append(f"importance={importance}")

    if case_type == "criminal":
        score += 30
        reasons.append("criminal case")
    elif case_type == "financial":
        score += 20
        reasons.append("financial case")
    elif case_type == "labor":
        score += 15
        reasons.append("labor case")
    else:
        score += 10
        reasons.append("other case type")

    if status == "open":
        score += 20
        reasons.append("status is open")
    elif status == "in progress":
        score += 15
        reasons.append("status in progress")
    elif status == "closed":
        score -= 50
        reasons.append("case is closed")

    if hearing_days <= 3:
        score += 30
        reasons.append("hearing very soon")
    elif hearing_days <= 7:
        score += 20
        reasons.append("hearing soon")
    elif hearing_days <= 14:
        score += 10
        reasons.append("hearing approaching")

    return score, reasons


def highest_priority(cases):
    if not cases:
        return None, None, None

    best_case = None
    best_score = -9999
    best_reasons = []

    for case in cases:
        score, reasons = calculate_priority(case)
        if score > best_score:
            best_score = score
            best_case = case
            best_reasons = reasons

    return best_case, best_score, best_reasons