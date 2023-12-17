import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return math.cos(x) * math.exp(-x*x)

def f_pr(x):
    return - math.exp(-x*x) * math.sin(x) - 2 * x * math.exp(-x*x) * math.cos(x)

def yk(t, x):
    return f(t) + f_pr(t) * (x - t)

tochka_kasaniya = 0.2
h = float(input())
h = round(1 / h)
x = np.linspace(0, 1, h)
y = [f(i) for i in x]

x1 = [0.0, 1.0]
y1 = [yk(tochka_kasaniya, i) for i in x1]

plt.title('График') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.grid()
plt.plot(x, y, label='f(x)')
plt.plot(x1, y1, label='Tangent at t=0.2')
plt.plot(tochka_kasaniya, f(tochka_kasaniya), "ro", label='Point of Tangency')

plt.legend()
plt.show()