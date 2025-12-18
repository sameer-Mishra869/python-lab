import csv
from recipe_class import Recipe, Ingredient


class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.inventory = {}

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def load_recipes_from_csv(self, filename="recipes.csv"):
        self.recipes.clear()
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                ing_list = []
                if row["ingredients"]:
                    for token in row["ingredients"].split("|"):
                        n, q, u = token.split(":")
                        ing_list.append(Ingredient(n, float(q), u))
                steps = row["steps"].split("|") if row["steps"] else []
                dietary = row["dietary_tags"].split("|") if row["dietary_tags"] else []
                recipe = Recipe(
                    name=row["name"],
                    cuisine=row["cuisine"],
                    difficulty=row["difficulty"],
                    prep_time=int(row["prep_time"]),
                    cook_time=int(row["cook_time"]),
                    servings=int(row["servings"]),
                    category=row["category"],
                    dietary_tags=dietary,
                    ingredients=ing_list,
                    steps=steps
                )
                self.recipes.append(recipe)

    def load_inventory(self, filename="inventory.txt"):
        self.inventory.clear()
        with open(filename, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                name, qty, unit = line.split(",")
                self.inventory[name.title()] = {"qty": float(qty), "unit": unit}

    def update_inventory(self, name, qty, unit):
        self.inventory[name.title()] = {"qty": qty, "unit": unit}


class IngredientSearchEngine:
    def __init__(self, manager: RecipeManager):
        self.manager = manager

    def match_recipe(self, available_ingredients: set, recipe: Recipe):
        recipe_ings = {i.name.title() for i in recipe.ingredients}
        present = recipe_ings & available_ingredients
        missing = recipe_ings - available_ingredients
        if not recipe_ings:
            return 0, []
        completeness = int(len(present) / len(recipe_ings) * 100)
        return completeness, list(missing)

    def search_by_ingredients(self, available_ingredients: list):
        avail_set = {item.title() for item in available_ingredients}
        matches = []
        for r in self.manager.recipes:
            percent, missing = self.match_recipe(avail_set, r)
            if percent > 0:
                matches.append({
                    "recipe": r,
                    "percent": percent,
                    "missing": missing
                })
        matches.sort(key=lambda x: x["percent"], reverse=True)
        return matches
