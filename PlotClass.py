import numpy as np
import matplotlib.pyplot as plt
x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.bar(x, y, label="Bars")
plt.xlabel('x')
plt.ylabel('y')

plt.title("New Graph")
plt.legend()
plt.show()
