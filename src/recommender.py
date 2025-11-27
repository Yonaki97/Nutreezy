
import pandas as pd

def healthier_alternatives(selected_food, df, top_n=3):

    if selected_food not in df["food"].values:
        return []

    selected = df[df["food"] == selected_food].iloc[0]

    candidates = df[df["food"] != selected_food].copy()

    def score_row(r):
        s = 0
        if r["calories"] < selected["calories"]:
            s += 2
        if r["sugar"] < selected["sugar"]:
            s += 1
        if r["fiber"] > selected["fiber"]:
            s += 1
        return s

    candidates["score"] = candidates.apply(score_row, axis=1)

    candidates = candidates[candidates["score"] > 0]
    if candidates.empty:
        return []

    candidates = candidates.sort_values(["score", "fiber", "calories"], ascending=[False, False, True])
    results = []
    for _, r in candidates.head(top_n).iterrows():
        reason_parts = []
        if r["calories"] < selected["calories"]:
            reason_parts.append(f"kalori {int(selected['calories']-r['calories'])} kcal lebih rendah")
        if r["sugar"] < selected["sugar"]:
            reason_parts.append(f"gula {r['sugar']:.1f}g (lebih rendah)")
        if r["fiber"] > selected["fiber"]:
            reason_parts.append(f"serat {r['fiber']:.1f}g (lebih tinggi)")
        results.append({
            "food": r["food"],
            "reason": ", ".join(reason_parts),
            "calories": r["calories"],
            "protein": r["protein"],
            "fiber": r["fiber"],
            "sugar": r["sugar"]
        })
    return results
