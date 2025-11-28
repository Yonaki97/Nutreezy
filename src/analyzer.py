def classify_benefit(row):
    try:
        protein = float(row["protein"])
        calories = float(row["calories"])
        carbs = float(row.get("carbs", 0))
        fiber = float(row["fiber"])
    except:
        return "Unknown ❓"

    if protein >= 20:
        return "Otot 💪"
    elif calories >= 300 and carbs >= 40:
        return "Energi ⚡"
    elif fiber >= 5 and calories < 200:
        return "Diet 🥗"
    else:
        return "Imunitas 🛡"


def nutriscore(row):
    try:
        calories = float(row["calories"])
        sugar = float(row["sugar"])
        fat = float(row["fat"])
        fiber = float(row["fiber"])
    except:
        return "E"

    score = 0
    if calories > 250: score += 1
    if sugar > 15: score += 1
    if fat > 15: score += 1
    if fiber < 3: score += 1

    return ["A","B","C","D","E"][min(score,4)]