import numpy as np
from manim import *



class massSpring(Scene):
    """
    def construct(self):
        #This tracks some value
        valueTracker = ValueTracker(0.5)
        
        #This defines what the spring will look like
        def springShape(x):
            return np.array([x, 0.5*np.cos(x),0])
        
        #This defines the domain of the function/spring
        def springLength(start,end):
            #usally -4 tau, 4.25 tau (2pi = tau)
            return np.array([start, end,0.1])     

        # The align_to postions it in the frame 
        spring = ParametricFunction(springShape,  t_range=np.array([-4*TAU, 4.25*TAU, 0.1])).align_to((np.array([-4,0,0]), np.array([-1,0,0])))
        
        def changeLength(mob):
            i = valueTracker.get_value()
            mob.become(ParametricFunction(lambda u : np.array([0.08*i*u, 0.5*np.cos(u), 0]), t_range=np.array([-4*TAU, 4.25*TAU, 0.1])).align_to((np.array([-4,0,0]), np.array([-1,0,0]))))

        spring.add_updater(changeLength)

        self.add(spring)

        # Set up the mass
        mass = Circle(
            radius=0.5,
            color=RED,
            fill_opacity=1,
            stroke_width=0
        )

        mass.move_to(spring.get_end())
        mass.add_updater(lambda m: mass.move_to(spring.get_end()))
        self.add(mass)
        for _ in range(4):
            self.play(valueTracker.animate.set_value(2))
            self.play(valueTracker.animate.set_value(0))
    """ 

    def construct(self):
        valueTracker = ValueTracker(0.5)
        def springShape(x):
            return np.array([x, 0.5*np.sin(x),0])
        def springLength(start,end):
            # the last 0.1 makes it faster for some reason
            return np.array([start, end, 0.1])
        
        #Initilizing the Math objects
        spring = ParametricFunction(springShape,
                                t_range=springLength(-4*TAU,4.1*TAU)).align_to(np.array([-4,0,0]), np.array([-1,0,0]))
        mass = Square(0.25,
                      color=RED_A)
        
        #This is the fucntion that redraws the spring each frame
        def springUpdater(spring):
            shiftX = valueTracker.get_value()
            # the x values of the spring get redrawn with respect to a value tracker on how much to shift x by
            # unfourantley had to use a lot of copy and pasted code but maybe I can figure out a better way to do this one day 
            spring.become(ParametricFunction(lambda u : np.array([0.09*shiftX*u, 0.5*np.sin(u), 0.5*np.sin(u)]),
                                t_range=springLength(-4*TAU,4*TAU)).align_to(np.array([-4,0,0]), np.array([-1,0,0])))

        #Adds objects and there updaters to the scence
        spring.add_updater(springUpdater)
        self.add(spring)
        mass.move_to(spring.get_end())
        mass.add_updater(lambda m: mass.move_to(spring.get_end()))
        self.add(mass)
        
        
        for _ in range(4):
            self.play(valueTracker.animate.set_value(2))
            self.play(valueTracker.animate.set_value(0.5))
        self.play(valueTracker.animate.set_value(0))
        return super().construct()
          