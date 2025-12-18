from search_engine import RecipeManager, IngredientSearchEngine
from nutritional_analyzer import NutritionalAnalyzer


def display_recipe(r, nutrition=None):
    print("\nSELECTED RECIPE:")
    print(f"Recipe: {r.name}")
    print(f"Cuisine: {r.cuisine}")
    print(f"Difficulty: {r.difficulty}")
    print(f"Serves: {r.servings}")
    print(f"Prep Time: {r.prep_time} minutes")
    print(f"Cook Time: {r.cook_time} minutes")
    print(f"Total Time: {r.total_time} minutes")

    print("\nINGREDIENTS:")
    for ing in r.ingredients:
        print(f"{ing.name} - {ing.quantity} {ing.unit} (Available)")

    print("\nCOOKING INSTRUCTIONS:")
    for i, step in enumerate(r.steps, start=1):
        print(f"{i}. {step}")

    if nutrition:
        print("\nNUTRITIONAL INFORMATION (per serving):")
        print(f"Calories: {nutrition['calories']} kcal")
        print(f"Protein: {nutrition['protein']} g")
        print(f"Carbohydrates: {nutrition['carbs']} g")
        print(f"Fat: {nutrition['fat']} g")
        print(f"Fiber: {nutrition['fiber']} g")
        print(f"Sodium: {nutrition['sodium']} mg")


def ingredient_search_flow(manager):
    engine = IngredientSearchEngine(manager)
    analyzer = NutritionalAnalyzer()

    print("\nEnter available ingredients separated by commas")
    print("Example: Tomato, Onion, Garlic, Chicken, Oil")
    user_input = input("Ingredients: ")
    available = [t.strip().title() for t in user_input.split(",") if t.strip()]

    matches = engine.search_by_ingredients(available)

    if not matches:
        print("No recipes found.")
        return

    print("\nMATCHING RECIPES:")
    print(f"{'Rank':<5}{'Recipe Name':<25}{'Match %':<10}{'Missing Ingredients'}")
    for idx, m in enumerate(matches[:5], start=1):
        r = m["recipe"]
        miss_str = ", ".join(m["missing"]) if m["missing"] else "None (Perfect match!)"
        print(f"{idx:<5}{r.name:<25}{m['percent']:<10}{miss_str}")

    choice = int(input("\nEnter rank of recipe to view details: "))
    selected = matches[choice - 1]["recipe"]
    nutrition = analyzer.analyze_recipe(selected)
    display_recipe(selected, nutrition)


def main():
    manager = RecipeManager()
    manager.load_recipes_from_csv()
    manager.load_inventory()

    while True:
        print("\n=== RECIPE MANAGER ===")
        print("1. Search recipes by ingredients")
        print("2. Exit")
        choice = input("Enter your choice: ")


    


if __name__ == "__main__":
    main()
