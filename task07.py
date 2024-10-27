import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_trials):
    sum_counts = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

    for _ in range(num_trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1

    probabilities = {x: count / num_trials for x, count in sum_counts.items()}
    return probabilities


def plot_monte_carlo_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(sums, [p * 100 for p in probs], color='skyblue', edgecolor='black')

    plt.xlabel('Сума')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при кидках двох кубиків - метод Монте-Карло)')
    plt.xticks(sums)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.2f}%', 
                 ha='center', va='bottom', fontsize=10)

    plt.show()

num_trials = 100000

monte_carlo_probs = monte_carlo_simulation(num_trials)
print("Ймовірності отримання суми методом Монте-Карло)")
for s, prob in monte_carlo_probs.items():
    print(f"Сума {s}: {prob * 100:.2f}%")

plot_monte_carlo_probabilities(monte_carlo_probs)