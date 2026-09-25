def predict_priority(age, severity):
    """
    0 = Low
    1 = Medium
    2 = High
    """
    if severity >= 8 or age >= 70:
        return 2
    elif severity >= 4:
        return 1
    else:
        return 0
