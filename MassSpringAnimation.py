import numpy as np
from manim import *
from sympy import *
from sympy.abc import t
from MassSpringCalculation import equationOfMotion



class MassSpring(Scene):
    
    # Functions to define the shape of the spring
    def springShape(self,x):
        # returns the shape of the spring (a sin wave)
        return np.array([0.09*x, 0.5*np.sin(x),0])
    def springLength(self,start,end):
        # returns the length of the spring in the frame
        # the last 0.1 makes it faster for some reason
        return np.array([start, end, 0.1])  
    
    # The scence itself
    def construct(self,mass,damping,stiffness,x_atZero,xPrime_atZero,forcingFactor=0):
        
        # Objects in scence
        springObject = ParametricFunction(self.springShape,
                                t_range=self.springLength(-4*TAU,4.1*TAU)).align_to(np.array([-7,0,0]), np.array([-1,0,0]))
        massObject = Square(0.5,
                      color=RED_A)     
        baseObject = Rectangle(width=1,height=3,color=BLUE_E)
        valueTracker = ValueTracker(0)

        # These are fucntions that redraw the spring and mass each frame.
        def springUpdater(spring):
            shiftX = massObject.get_center()[0]
            # Fix the left end at a specific point, (-7, 0, 0)
            left_end = np.array([-7.0, 0, 0])
            # Determine the new position of the right end (center of the mass)
            right_end = massObject.get_center()
            # Calculate the new length of the spring based on the distance between the ends(this is needed to keep the amplitude looking the same throughout the animation)
            spring_length = np.linalg.norm(right_end - left_end)
            # Define the new parametric function for the spring
            spring.become(ParametricFunction(lambda u: np.array([left_end[0] + (right_end[0] - left_end[0]) * u / spring_length,
                                                                 0.5 * np.sin(8 * np.pi * u / spring_length),  # change the amplitude of this sin wave to ur liking
                                                                 0]),
                                            t_range=[0, spring_length]))    
        def massUpdater(mass):
            shiftXNEW = valueTracker.get_value()
            # if you want to keep the motion on the screen activate("clampedX = np.clip(shiftXNEW, -7, 7)") this (and set mass.setx(clampedX)) maybe it wasnt working last time
            mass.set_x(shiftXNEW)
        
        # Adds objects to the scence
        self.add(massObject)
        self.add(springObject)
        self.add(baseObject)
        

        # Add the updater of each respective object
        springObject.add_updater(springUpdater)
        massObject.add_updater(massUpdater)
            
        
        # Postion objects
        baseObject.set_fill(BLUE_E)
        massObject.move_to(np.array([0,0,0]))
        massObject.set_fill(RED_E)

        baseObject.move_to(np.array([-7,0,0]))

        # Generate points
        equationData = equationOfMotion(mass,damping,stiffness,x_atZero,xPrime_atZero,forcingFactor)  # type: ignore
              
        # calling the numerical values of x(t) and setting the valueTracker = x(t) and that drives the motion of the scence
        # THIS DRIVEs THE MOTION OF THE SCENCE!
        for x_val in equationData[0]:
            self.play(valueTracker.animate.set_value(x_val),run_time=0.05, rate_func=linear)
    
       




        
    