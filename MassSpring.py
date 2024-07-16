import numpy as np
from manim import *



class UseParametricFunction(Scene):
    def construct(self):
        #This tracks some value
        valueTracker = ValueTracker(0.5)
        
        #This defines what the spring will look like
        def reversedLambda(x):
            return np.array([x, 0.5*np.cos(x),0])
        

        # The t range makes it longer or shorter I think 
        graph = ParametricFunction(reversedLambda,
                                t_range=np.array([-4*TAU, 4.25*TAU, 0.1])).align_to(np.array([-4,0,0]), np.array([-1,0,0]))
        

        def changeLength(mob):
            i = valueTracker.get_value()
            mob.become(ParametricFunction(lambda u : np.array([0.08*i*u, 0.5*np.cos(u), 0]),
                                t_range=np.array([-4*TAU, 4.25*TAU, 0.1])).align_to(np.array([-4,0,0]), np.array([-1,0,0])))

        graph.add_updater(changeLength)

        self.add(graph)
        # Set up the mass
        mass = Circle(
            radius=0.5,
            color=RED,
            fill_opacity=1,
            stroke_width=0
        )

        mass.move_to(graph.get_end())
        mass.add_updater(lambda m: mass.move_to(graph.get_end()))
        self.add(mass)
        for _ in range(4):
            self.play(valueTracker.animate.set_value(2))
            self.play(valueTracker.animate.set_value(0))
        

"""
class YoungModulus(Scene):
    def construct(self):
        # Set up the spring
        spring = always_redraw(lambda: ParametricFunction(
            lambda t: [t, np.sin(3*t), 0],
            t_range=[-4, 4],
            color=YELLOW
        ))

        # Set up the mass
        mass = Circle(
            radius=0.5,
            color=RED,
            fill_opacity=1,
            stroke_width=0
        )

        mass.move_to(spring.get_end())
        mass.add_updater(lambda m: mass.move_to(spring.get_end()))

        self.play(FadeIn(mass, spring))
        self.play(spring.animate.to_edge(RIGHT))
"""
"""        
class massSpring(Scene):
    def construct(self):
        sqaure = Square()
"""     