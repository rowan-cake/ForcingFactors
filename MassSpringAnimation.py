import numpy as np
from manim import *
from MassSpringCalculation import equationOfMotion



class massSpring(Scene):
    def springShape(self,x):
        # returns the shape of the spring (a sin wave)
        return np.array([x, 0.5*np.sin(x),0])
    def springLength(self,start,end):
        # returns the length of the spring in the frame
        # the last 0.1 makes it faster for some reason
        return np.array([start, end, 0.1])
    def construct(self):
        valueTracker = ValueTracker(0)        
        
        #Initilizing the Math objects
        spring = ParametricFunction(self.springShape,
                                t_range=self.springLength(-4*TAU,4.1*TAU)).align_to(np.array([-7,0,0]), np.array([-1,0,0]))
        mass = Square(0.25,
                      color=RED_A)
        
        #This is the fucntion that redraws the spring each frame
        def springUpdater(spring):
            shiftX = valueTracker.get_value()
            # the x values of the spring get redrawn with respect to a value tracker on how much to shift x by
            # unfourantley had to use a lot of copy and pasted code but maybe I can figure out a better way to do this one day 
            spring.become(ParametricFunction((lambda u : np.array([0.09*shiftX*u, 0.5*np.sin(u), 0.5*np.sin(u)])),
                                             t_range=self.springLength(-4*TAU,4.1*TAU)).align_to(np.array([-7,0,0]), np.array([-1,0,0])))

        #Adds objects and there updaters to the scence
        spring.add_updater(springUpdater)
        self.add(spring)
        mass.move_to(spring.get_end())
        mass.add_updater(lambda m: mass.move_to(spring.get_end()))
        self.add(mass)
        massTwo = Square(0.25,
                      color=RED_A)
        massThree= Square(0.25,
                      color=RED_A)
        massTwo.move_to(np.array([-7,1,0]))
        massThree.move_to(np.array([-1,1,0]))

        self.add(massTwo)
        self.add(massThree)
        array = equationOfMotion(3,0,1,0,1)
        newValueTracker = ValueTracker(-1)
        def updater(mass):
            shiftXNEW = newValueTracker.get_value()
            mass.set_x(shiftXNEW)
        massThree.add_updater(updater)
        
        #calling the numerical values of x(t)
        for num in array[0]:
            print(num)
            if num == 1:
                self.wait()
                print("hi")
            self.play(valueTracker.animate.set_value(num))
            self.play(newValueTracker.animate.set_value(num))
        self.play(valueTracker.animate.set_value(0))
        
        return super().construct()
    