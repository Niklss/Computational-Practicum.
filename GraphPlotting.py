import matplotlib.pyplot as plt
import numpy as np


# My initial function
def f(x, y):
    return -x - y


# Creating arrays for plotting the graphics, because
def makeAnArraysForGraphics(x0, y0, X, k):
    h = (X - x0) / k
    x = np.linspace(x0, X, k)
    yEuler = [y0]
    yUEuler = [y0]
    yRK = [y0]
    yOriginal = []
    errorUEuler = []
    errorEuler = []
    errorRK = []
    for i in x[:k - 1]:
        yEuler.append(yEuler[-1] + h * f(i, yEuler[-1]))
        yUEuler.append(yUEuler[-1] + h / 2 * (f(i + h, yUEuler[-1] + h * f(i, yUEuler[-1])) + f(i, yUEuler[-1])))
        k1 = h * f(i, yRK[-1])
        k2 = h * f(i + h / 2, yRK[-1] + k1 / 2)
        k3 = h * f(i + h / 2, yRK[-1] + k2 / 2)
        k4 = h * f(i + h, yRK[-1] + k3)
        yRK.append(yRK[-1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

    for i in x:
        yOriginal.append(-1 * i + 1)

    for i in range(k):
        errorEuler.append(yOriginal[i] - yEuler[i])
        errorUEuler.append(yOriginal[i] - yUEuler[i])
        errorRK.append(yOriginal[i] - yRK[i])
    return x, yEuler, yUEuler, yRK, yOriginal, errorEuler, errorUEuler, errorRK


def plotTheGraphics(x, yEuler, yUEuler, yRK, yOriginal, errorEuler, errorUEuler, errorRK):
    figure = plt.figure()
    sbplt1 = figure.add_subplot(311)
    sbplt1.grid(True)
    sbplt1.plot(x, yEuler, "red", label="Euler method")
    sbplt1.plot(x, yUEuler, "blue", label="Improved Euler method")
    sbplt1.plot(x, yRK, "green", label="Runge-Kutta method")
    sbplt1.set_title('Numerical methods')
    sbplt1.legend()

    sbplt2 = figure.add_subplot(312)
    sbplt2.grid(True)
    sbplt2.plot(x, yOriginal, "black", label="Original function")
    sbplt2.set_title('Original function')
    sbplt2.legend()

    sbplt3 = figure.add_subplot(313)
    sbplt3.grid(True)
    sbplt3.plot(x, errorEuler, "red", label="Euler method error")
    sbplt3.plot(x, errorUEuler, "blue", label="Improved Euler method error")
    sbplt3.plot(x, errorRK, "green", label="Runge-Kutta method error")
    sbplt3.set_title('Error')
    sbplt3.legend()

    plt.show()

    return plt


x0 = 0
y0 = 1
X = 10
k = 10000
arrays = makeAnArraysForGraphics(x0, y0, X, k)
plotTheGraphics(arrays[0], arrays[1], arrays[2], arrays[3], arrays[4], arrays[5], arrays[6], arrays[7])
