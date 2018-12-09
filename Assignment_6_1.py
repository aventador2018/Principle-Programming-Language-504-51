"""
This is a sample code meant to provide a framework for completing
the exercise based on Problem 16.28 of Chapra textbook.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    WEIGHT = 20000.0
    sigma = 0.3

    V0 = 200.0  # Initial guess for velocity that minimizes drag

    # Create a NumPy array of sample v values, then pass
    # that into the plotting routine along with scalar values
    # for sigma and weight
    v = np.linspace(100,1200)
    plot_drag_vs_v(s=sigma, W=WEIGHT, V=v)

    # Compute the velocity that minimizes the drag for specified
    # values of sigma and weight, starting from an initial
    # guess, V0
    min_v = newton_min(v0=V0, s=sigma, W=WEIGHT)

    print("\nVelocity that minimizes drag: " + str(min_v))


def newton_min(v0=None, s=None, W=None):
    """
    Given an initial velocity guess, v0, a scalar value sigma (s)
    and a scalar value W (weight), use Newton's method to determine
    the velocity which minimizes the drag.

    This function assumes the presence of the following functions

    D(s, V, W) : Drag, as function of s, V and W
    dDdV(s, V, W) : First derivative of drag, as function of s, V and W
    d2DdV2(s, V, W) : Second derivative of drag, as function of s, V and W

    If convergence occurs within MAXITS iterations, then the value of
    v is returned.  Otherwise, a "None" is returned
    """
    EPSILON = 1.0E-2
    MAXITS = 10

    converged = False

    iters = 0
    v_new = v0

    print('     v_old         v_new       error')
    while not converged and iters<MAXITS:
        v_new = v0 - dDdV(s, v0, W)/d2DdV2(s, v0, W)
        print('{:13.6e} {:13.6e} {:10.3e}'.format(v0, v_new, abs(v_new-v0)))
        if abs(v_new-v0) < EPSILON:
            converged = True
        iters += 1
        v0 = v_new

    if converged:
        return_value = v_new
    else:
        return_value = None

    return return_value


def plot_drag_vs_v(s=None, V=None, W=None):
    # s : (sigma) scalar value
    # V : (velocity) NumPy array of x-axis values
    # W : (weight) scalar value

    # For the domain of V, plot D, D' and D''
    fig = plt.figure()
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)

    # Plot drag function
    d = D(s=s, V=V, W=W)
    ax1.plot(V, d)

    # Plot first derivative
    dddv = dDdV(s=s, V=V, W=W)
    ax2.plot(V, dddv)

    # Plot second derivative
    d2ddv2 = d2DdV2(s=s, V=V, W=W)
    ax3.plot(V, d2ddv2)
    plt.show()


def D(s=None, V=None, W=None):
    # Compute drag as a function of
    #
    # s: (sigma) ratio of air density between flight altitude and sea level
    # V: velocity
    # W: weight

    d = 0.01*s*V**2 + (0.95/s)*(W/V)**2

    return d


def dDdV(s=None, V=None, W=None):
    # Compute first derivative of D wrt V
    #
    # s: (sigma) ratio of air density between flight altitude and sea level
    # V: velocity
    # W: weight
    #
    # This should be computed using a central difference formula for
    # the first derivative of the function D().

    h = 0.01

    # Calculate first derivative
    fd = (D(s, V+h, W) - D(s, V-h, W))/(2*h)

    # print("Testing first derivative: ")
    # print("Accurate first derivative: ", 0.02*s*V - 2*0.95*W**2/(V**3*s))
    # print("Result from Central Difference Formula: ", fd)

    return fd


def d2DdV2(s=None, V=None, W=None):
    # Compute second derivative of D wrt V
    #
    # s: (sigma) ratio of air density between flight altitude and sea level
    # V: velocity
    # W: weight
    #
    # This should be computed using a central difference formula for
    # the second derivative of the function D().

    h = 0.01

    # Calculate second derivative
    sd = (dDdV(s, V+h, W) - dDdV(s, V-h, W))/(2*h)

    # print("Testing second derivative: ")
    # print("Accurate first derivative: ", 0.02 * s + 6 * 0.95 * W ** 2 / (V ** 4 * s))
    # print("Result from Central Difference Formula: ", sd)

    return sd


if __name__ == "__main__":
    main()
