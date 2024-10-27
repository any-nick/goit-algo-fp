
def greedy_algorithm(items, budget):
    sorted_items = sorted( items.items(), key=lambda x: x[1]['calories'], reverse=True )

    total_calories = 0
    chosen_items = []

    for name, info in sorted_items:
        if info['cost'] <= budget:
            chosen_items.append(name)
            total_calories += info['calories']
            budget -= info['cost']

    return chosen_items, total_calories

def dynamic_programming(items, budget):
    costs = [info['cost'] for info in items.values()]
    calories = [info['calories'] for info in items.values()]
    names = list(items.keys())
    n = len(items)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget + 1):
            if costs[i - 1] <= b:
                dp[i][b] = max(
                    dp[i - 1][b],
                    dp[i - 1][b - costs[i - 1]] + calories[i - 1]
                )
            else:
                dp[i][b] = dp[i - 1][b]

    total_calories = dp[n][budget]
    chosen_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            chosen_items.append(names[i - 1])
            b -= costs[i - 1]

    return chosen_items, total_calories


budget = 110

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

print("Жадібний алгоритм:")
greedy_result, greedy_calories = greedy_algorithm(items, budget)
print("Вибрані страви:", greedy_result)
print("Сумарна калорійність:", greedy_calories)

print("\nДинамічне програмування:")
dp_result, dp_calories = dynamic_programming(items, budget)
print("Вибрані страви:", dp_result)
print("Сумарна калорійність:", dp_calories)
