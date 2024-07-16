import scipy as sp
from sympy import Function, dsolve, Derivative, checkodesol
from sympy.abc import t

def equationOfMotion(mass,damping,stiffness,x_atZero,xPrim_atZero):
    # 3 cases based on roots
    x = Function('x')
    # Solve the ODE
    result = dsolve(mass*Derivative(x(t), t, 2) 
                    + damping*Derivative(x(t), t) 
                    +stiffness*x(t)
                    , x(t)
                    ,ics={x(0): x_atZero, x(t).diff(t).subs(t,0): xPrim_atZero})
    print(result)

equationOfMotion(3,0,1,0,6)