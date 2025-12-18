class Ingredient:
    def __init__(self, name, quantity, unit,
                 calories=0, protein=0, carbs=0, fat=0, fiber=0, sodium=0,
                 category="General", available=True):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.fiber = fiber
        self.sodium = sodium
        self.category = category
        self.available = available


class Recipe:
    def __init__(self, name, cuisine, difficulty,
                 prep_time, cook_time, servings,
                 category,              # breakfast / lunch / dinner / dessert
                 dietary_tags=None,     # list of strings
                 ingredients=None,      # list of Ingredient
                 steps=None):           # list of strings
        self.name = name
        self.cuisine = cuisine
        self.difficulty = difficulty
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.category = category
        self.dietary_tags = dietary_tags or []
        self.ingredients = ingredients or []
        self.steps = steps or []

    @property
    def total_time(self):
        return self.prep_time + self.cook_time
