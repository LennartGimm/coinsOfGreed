import numpy as np
import matplotlib.pyplot as plt

# Ten weeks
time = 1680

goldEaten = np.zeros(time)
coinsOfGreed = np.zeros(time)
coinsOfGreed[0] = 1


for i in range(1, time):
    goldEaten[i] = goldEaten[i-1] + coinsOfGreed[i-1]
    coinsOfGreed[i] = coinsOfGreed[i - 1]
    for n in range(int(coinsOfGreed[i])):
        if np.random.rand(1) < 1/100:
            coinsOfGreed[i] += 1
    print("\r", int(100 * i / time), "% done", end="")

plt.xlabel("Hours after introduction of the Coin of Greed")
plt.ylabel("Coins Eaten")
plt.plot(goldEaten, color='blue')
plt.grid()
plt.draw()
plt.savefig('coinsEaten.png')
plt.show()

plt.xlabel("Hours after introduction of the Coin of Greed")
plt.ylabel("Coins of Greed")
plt.plot(coinsOfGreed, color='red')
plt.grid()
plt.draw()
plt.savefig('coinsOfGreed.png')
plt.show()
