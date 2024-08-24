import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy import Function, dsolve, Derivative, checkodesol, Eq, sin
from sympy.abc import t

# Create the plot
def createPlot(equation):
    plt.figure(figsize=(8, 8))
    stringRHS = str(equation[2]) #unpacking the equation of motion function
    plt.plot(equation[1], equation[0], label=r'$x(t) = $'+stringRHS)
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.title('Plot of the function $x(t) = ' + stringRHS + '$')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

def equationOfMotion(mass,damping,stiffness,x_atZero,xPrime_atZero,forcingFactor=0):
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
    #Convert string to sympy equation
    forcingFactor = sp.sympify(forcingFactor)
    # Solve the ODE
    odeEquation = Eq(mass*Derivative(x(t), t, 2)+ damping*Derivative(x(t), t)+ stiffness*x(t),forcingFactor)
    equationOfMotion = dsolve(odeEquation,x(t)
                    ,ics={x(0): x_atZero, x(t).diff(t).subs(t,0): xPrime_atZero})
    # RHS of the solved ODE
    rightHandSide = equationOfMotion.rhs
    # Now we have a function that can take inputs and turn them to proper outputs based on the RHS of the solved ODE
    numerical_function = sp.lambdify(t, rightHandSide, 'numpy')
    # Input points to the solved ODE (start,end,howManyPointsInBetween)
    t_vals = np.linspace(0, 13, 200)
    # Take inputs and turn them to outputs
    x_vals = numerical_function(t_vals)
    # print them just to see
    # return the x_vals the t_vals and the solved symbolic RHS (done for ploting purposes) in a tuple
    naturalFrequency = np.sqrt((stiffness/mass)-(damping**2/(2*mass**2)))
    return x_vals,t_vals,rightHandSide,naturalFrequency

if __name__ == "__main__":    
    equation = equationOfMotion(-1,0,-2,2,-2,sin(1.4142135623730951*t)) # type: ignore        
    createPlot(equation)
    