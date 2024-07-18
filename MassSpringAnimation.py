import numpy as np
from manim import *
from MassSpringCalculation import equationOfMotion



class massSpring(Scene):
    def construct(self):
        valueTracker = ValueTracker(0)
        def springShape(x):
            return np.array([x, 0.5*np.sin(x),0])
        def springLength(start,end):
            # the last 0.1 makes it faster for some reason
            return np.array([start, end, 0.1])
        
        #Initilizing the Math objects
        spring = ParametricFunction(springShape,
                                t_range=springLength(-4*TAU,4.1*TAU)).align_to(np.array([-6,0,0]), np.array([-1,0,0]))
        mass = Square(0.25,
                      color=RED_A)
        
        #This is the fucntion that redraws the spring each frame
        def springUpdater(spring):
            shiftX = valueTracker.get_value()
            # the x values of the spring get redrawn with respect to a value tracker on how much to shift x by
            # unfourantley had to use a lot of copy and pasted code but maybe I can figure out a better way to do this one day 
            spring.become(ParametricFunction(lambda u : np.array([0.09*shiftX*u, 0.5*np.sin(u), 0.5*np.sin(u)]),
                                t_range=springLength(-4*TAU,4*TAU)).align_to(np.array([-6,0,0]), np.array([-1,0,0])))

        #Adds objects and there updaters to the scence
        spring.add_updater(springUpdater)
        self.add(spring)
        mass.move_to(spring.get_end())
        mass.add_updater(lambda m: mass.move_to(spring.get_end()))
        self.add(mass)
        massTwo = Square(0.25,
                      color=RED_A)
        massTwo.move_to(np.array([7,1,0]))
        self.add(massTwo)
        
        array = equationOfMotion(3,2,1,0,2)
        
        for num in array[0]:
            if num == 1:
                self.wait()
                print("hi")
            self.play(valueTracker.animate.set_value(num))
        self.play(valueTracker.animate.set_value(0))
        
        return super().construct()
          