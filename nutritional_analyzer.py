import csv
from recipe_class import Recipe


class NutritionalAnalyzer:
    def __init__(self, nutrition_file="ingredients.csv"):
        self.nutrition_db = {}
        with open(nutrition_file, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.nutrition_db[row["name"].title()] = {
                    "calories": float(row["calories"]),
                    "protein": float(row["protein"]),
                    "carbs": float(row["carbs"]),
                    "fat": float(row["fat"]),
                    "fiber": float(row["fiber"]),
                    "sodium": float(row["sodium"])
                }

    def analyze_recipe(self, recipe: Recipe):
        totals = {"calories": 0, "protein": 0, "carbs": 0,
                  "fat": 0, "fiber": 0, "sodium": 0}
        for ing in recipe.ingredients:
            base = self.nutrition_db.get(ing.name.title())
            if not base:
                continue
            factor = ing.quantity         # assume nutrition per 1 unit
            for k in totals:
                totals[k] += base[k] * factor
        per_serving = {k: round(v / recipe.servings, 1) for k, v in totals.items()}
        return per_serving
