from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        self.wait()
        self.play(Create(triangle))
        self.wait()
        self.play(triangle.animate.to_edge(LEFT))
        number = 0
        while number<10:
            triangle.set_x(-6)
            triangle.set_x(6)
            number+=1
        self.play(Transform(triangle, circle))
        self.play(FadeOut(triangle))
        
        arrows = [Arrow(2 * LEFT, 2 * RIGHT), Arrow(2 * DR, 2 * UL)]
        VGroup(*arrows).set_x(0).arrange(buff=2)
        self.play(GrowArrow(arrows[0]))
        self.play(GrowArrow(arrows[1], point_color=RED))
