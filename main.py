import numpy as np
import matplotlib.pyplot as plt

# variable declaration
dice_lower_limit = 1
dice_upper_limit = 6
number_of_dice = 10000000

# simulating the dice rolls
rolls = np.random.randint(dice_lower_limit, dice_upper_limit+1, (number_of_dice))

# calculating the average
average = np.mean(rolls)
average = round(average, 3)
print(f"Average / Mean: {average}")

# calculating probability
prop = dict()
for i in range(dice_lower_limit, dice_upper_limit+1):
    p = float(np.count_nonzero(rolls == i) / len(rolls))
    prop[i] = p
print(f"Probability of Each Number: {prop}")

plt.hist(rolls, bins=np.arange(dice_lower_limit, dice_upper_limit+2)-0.5, edgecolor='black')
plt.xticks(range(dice_lower_limit, dice_upper_limit+1))
# gpt above 2 lines
plt.title('Frequency Distribution (Histogram)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()