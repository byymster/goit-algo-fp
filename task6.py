items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if budget >= details['cost']:
            selected_items.append(item)
            total_calories += details['calories']
            budget -= details['cost']

    return selected_items, total_calories

# Динамічне програмування
def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, details = item_list[i - 1]
        for w in range(budget + 1):
            if details['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - details['cost']] + details['calories'])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення обраних предметів
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, details = item_list[i - 1]
            selected_items.append(item_name)
            w -= details['cost']

    total_calories = dp[n][budget]
    return selected_items, total_calories

if __name__ == "__main__":
    budget = 100

    # Жадібний алгоритм
    greedy_items, greedy_calories = greedy_algorithm(items, budget)
    print("Greedy Algorithm:")
    print(f"Selected items: {greedy_items}")
    print(f"Total calories: {greedy_calories}")

    # Динамічне програмування
    dp_items, dp_calories = dynamic_programming(items, budget)
    print("\nDynamic Programming:")
    print(f"Selected items: {dp_items}")
    print(f"Total calories: {dp_calories}")
