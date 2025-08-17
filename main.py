import numpy as np
import matplotlib.pyplot as plt

# variable declaration
dice_lower_limit = 1
dice_upper_limit = 6
number_of_dice = 10000000

# simulating the dice rolls
def rollDice(lower_limit, upper_limit, no_dice):
    return np.random.randint(lower_limit, upper_limit+1, (no_dice), dtype=np.int8)

# calculating the average
def rollsAverage(rolls):
    avg = np.mean(rolls)
    avg = round(avg, 3)
    return avg

# calculating probability
def rollsProb(rolls):
    prob = dict()
    for i in range(dice_lower_limit, dice_upper_limit+1):
        p = round(float(np.count_nonzero(rolls == i) / len(rolls)), 3)
        prob[i] = p
    return prob

def rollsPlot(rolls):
    plt.hist(rolls, bins=np.arange(dice_lower_limit, dice_upper_limit+2)-0.5, edgecolor='black')
    plt.xticks(range(dice_lower_limit, dice_upper_limit+1))
    plt.title('Frequency Distribution (Histogram)')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

rolls = rollDice(dice_lower_limit, dice_upper_limit, number_of_dice)
print(f"Average: {rollsAverage(rolls)}")
print(f"Probability: {rollsProb(rolls)}")
rollsPlot(rolls)