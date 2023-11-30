import matplotlib.pyplot as plt
import numpy as np

# Skill levels
python = (85, 67, 23, 98)
java = (50, 67, 89, 14)
networking = (60, 20, 56, 22)
machine_learning = (88, 23, 40, 87)

# List of names
people = ['Bob', 'Anna', 'John', 'Mark']

index = np.arange(4)
plt.bar(index, python, width=0.2, label="This is python skill")
plt.bar(index + 0.2, java, width=0.2, label="This is java skill")
plt.bar(index + 0.4, networking, width=0.2, label="This is networking skill")
plt.bar(index + 0.6, machine_learning, width=0.2, label="This is machine learning skill")

plt.title("IT Skill Levels")
plt.xlabel("Person")
plt.ylabel("Skill Level")
plt.xticks(index + 0.2, people)
plt.legend(loc='upper left')
plt.ylim(0, 120)

plt.show()
