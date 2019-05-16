import numpy as np
import matplotlib.pyplot as plt
import math as math
N = 6  # fourie展開の展開数
num = 100  # 区間の刻み回数
range_ = 10.0
left = -1 / 2 * range_
dt = range_ / num
t = np.zeros(num)
fou = np.zeros(num)
ori = np.zeros(num)


def original(x: float) -> float:
    if math.ceil(x) % 2 == 0:
        return 0
    else:
        x = x - np.floor(x)
        return x * (1 - x)


def fourier(x: float) -> float:
    result = 0
    initial_value = 1.0 / 12
    a_n = np.zeros(N)
    b_n = np.zeros(N)
    for count in range(N):
        if count == 0:
            a_n[count] = initial_value
            result += a_n[count]
        else:
            a_n[count] = -(np.cos(count * np.pi) + 1) / (count**2 * np.pi**2)
            b_n[count] = (2 - 2 * np.cos(count * np.pi)) / (count**3 * np.pi**3)
            result += a_n[count] * np.cos(count * np.pi * x) + b_n[count] * np.sin(count * np.pi * x)
    return result


for j in range(num):
    t[j] = j * dt + left
    # print(t[j])
    fou[j] = fourier(t[j])
    ori[j] = original(t[j])

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)
plt.plot(t, fou, label="fourier")
plt.plot(t, ori, label="original")
plt.xlabel("x", fontsize=20)
plt.ylabel("y", fontsize=20)
plt.xlim(-5, 5)
plt.ylim(-0.1, 0.4)
plt.legend(loc="best", fontsize=20)
ax.text(2, -0.05, f'N = {N}', size=20, color="black")
plt.savefig("fourie" + ".png")
plt.show()
