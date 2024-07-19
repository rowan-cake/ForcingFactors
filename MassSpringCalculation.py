import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import Function, dsolve, Derivative, checkodesol
from sympy.abc import t


def equationOfMotion(mass,damping,stiffness,x_atZero,xPrim_atZero):
    """
    # Effects: 
    ==============
    - Takes coeffiecents and intial coniditions of a second order homogenous ODE equation and returns its solution ploted values in a 
    numpy array. 
    
    # Paremeters: 
    ==============
    - mass(float): the mass of the spring?
    - damping(float): the friction on the system
    - stiffness(float): the stiffness of the spring
    - x_atZero(float): one intial condition (a x(t) value for t=0)
    - xPrim_atZero(float): another intial condition (a x'(t) value for t=0)

    # Returns:
    ============== 
    - equationOfMotion(Equation(SciPY)): returns a equation type from scipy?
    """
    x = Function('x')
    # Solve the ODE
    equationOfMotion = dsolve(mass*Derivative(x(t), t, 2) 
                    + damping*Derivative(x(t), t) 
                    +stiffness*x(t)
                    , x(t)
                    ,ics={x(0): x_atZero, x(t).diff(t).subs(t,0): xPrim_atZero})
    rightHandSide = equationOfMotion.rhs
    numerical_function = sp.lambdify(t, rightHandSide, 'numpy')
    t_vals = np.linspace(0, 10, 12)
    x_vals = numerical_function(t_vals)
    for num in x_vals:
        print(num)
    return x_vals,t_vals,rightHandSide

if __name__ == "__main__":
    eq = equationOfMotion(6,4,2,-1,6)
    #rhs = eq.rhs
    #numerical_function = sp.lambdify(t, rhs, 'numpy')


    # Define the range of t values , 400 points between 0-100 (with some numerical errors)
    #t_vals = np.linspace(0, 100, 400)
    # Evaluate the numerical function this outputs a list of x points for every time value
    #x_vals = numerical_function(t_vals)

    # Create the plot
    plt.figure(figsize=(8, 8))
    stringRHS = str(eq[2])
    plt.plot(eq[1], eq[0], label=r'$x(t) = '+stringRHS+'$')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Plot of the function $x(t) = ' + stringRHS + '$')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

