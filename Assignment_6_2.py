import numpy as np
import matplotlib.pyplot as plt


def main():
    WEIGHT = 15000.0
    V = 200.0

    sigma = 0.5 # Initial guess for sigma that minimizes drag

    # Create a NumPy array of sigma values, then plot the graph with constant weight and velocity
    s = np.linspace(0.1,5)
    plot_drag_vs_s(s=s, W=WEIGHT, V=V)

    # Compute the min sigma
    min_s = newton_min(v=V, s_old=sigma, W=WEIGHT)

    print("\nSigma that minimizes drag: " + str(min_s))


def newton_min(v=None, s_old=None, W=None):
    # EPSILON will be the signal of convergence
    # MAXITS represents the max iterations the function is going to run
    EPSILON = 1.0E-2
    MAXITS = 10

    converged = False

    iters = 0
    s_new = s_old

    print('     v_old         v_new       error')
    while not converged and iters<MAXITS:
        s_new = s_old - dDds(s_old, v, W)/d2Dds2(s_old, v, W)
        print('{:13.6e} {:13.6e} {:10.3e}'.format(s_old, s_new, abs(s_new-s_old)))
        if abs(s_new-s_old) < EPSILON:
            converged = True
        iters += 1
        s_old = s_new

    if converged:
        return_value = s_new
    else:
        return_value = None

    return return_value


def plot_drag_vs_s(s=None, V=None, W=None):
    # s : (sigma) scalar value
    # V : (velocity) NumPy array of x-axis values
    # W : (weight) scalar value

    # For the domain of s, plot D, D' and D''
    fig = plt.figure()
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)

    # Plot drag function
    d = D(s=s, V=V, W=W)
    ax1.plot(s, d)

    # Plot first derivative
    ddds = dDds(s=s, V=V, W=W)
    ax2.plot(s, ddds)

    # Plot second derivative
    d2dds2 = d2Dds2(s=s, V=V, W=W)
    ax3.plot(s, d2dds2)
    plt.show()


def D(s=None, V=None, W=None):
    # Compute drag as a function of
    #
    # s: (sigma) ratio of air density between flight altitude and sea level
    # V: velocity
    # W: weight

    d = 0.01*s*V**2 + (0.95/s)*(W/V)**2

    return d


def dDds(s=None, V=None, W=None):
    # Compute first derivative of D wrt V
    #
    # s: (sigma) ratio of air density between flight altitude and sea level
    # V: velocity
    # W: weight

    h = 0.000001

    # Calculate first derivative
    fd = (D(s+h, V, W) - D(s-h, V, W))/(2*h)

    # print("Testing first derivative: ")
    # print("Accurate first derivative: ", 0.01*V**2 - 0.95*W**2/(V*s)**2)
    # print("Result from Central Difference Formula: ", fd)

    return fd


def d2Dds2(s=None, V=None, W=None):
    # Compute second derivative of D wrt V
    #
    # s: (sigma) ratio of air density between flight altitude and sea level
    # V: velocity
    # W: weight

    h = 0.000001

    # Calculate second derivative
    sd = (dDds(s+h, V, W) - dDds(s-h, V, W))/(2*h)

    # print("Testing second derivative: ")
    # print("Accurate first derivative: ", 2 * 0.95 * (W/V)**2/s**3)
    # print("Result from Central Difference Formula: ", sd)

    return sd


if __name__ == "__main__":
    main()
