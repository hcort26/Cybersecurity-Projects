def rule_based_score(transaction):
    score = 0

    if transaction["amount"] > 1500:
        score += 1
    if transaction["transaction_velocity"] > 4:
        score += 1
    if transaction["is_foreign_transaction"] == 1:
        score += 1
    if transaction["failed_login_attempts"] > 2:
        score += 1
    if transaction["location_change_since_last_tx"] == 1:
        score += 1

    return 1 if score >= 2 else 0