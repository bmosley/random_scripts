
# import matplotlib.pyplot as plt
# import numpy as np
  

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Any suitable title")

# x1 = [2, 4, 6, 8]
# y1 = [3, 5, 7, 9]
# plt.plot(x1, y1, '-.')
# plt.savefig("/tmp/fig.png", bbox_inches="tight")
# #plt.show()


import matplotlib.pyplot as plt

data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categorical Plotting')

cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

fig, ax = plt.subplots()
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
ax.legend()

plt.show()