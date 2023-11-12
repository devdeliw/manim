from manim import * 
import numpy as np

class Integral(Scene):
    def construct(self):
        ax = Axes( 
            x_range = (0, 5), 
            y_range = (-1, 1),
            x_length = 7, 
            y_length = 7
        )
        
        curve = ax.plot(
                lambda x: np.sin(x),
                color = YELLOW
        )

        self.play(Create(ax), Create(curve))
        self.wait(1)

        rectangles = ax.get_riemann_rectangles(curve, x_range = [0,5], dx
                                                  = 0.1)
        self.play(Write(rectangles))

        self.wait(2)


class ThreeD(ThreeDScene):
    def construct(self): 
        axes = ThreeDAxes(
            x_range = (-5, 5, 1), 
            y_range = (-5, 5, 1), 
            z_range = (-5, 5, 1), 
            x_length = 5, 
            y_length = 5, 
            z_length = 5
        )

        self.set_camera_orientation(
            phi = 30*DEGREES,
            theta = 30*DEGREES, 
            distance = 4
        )

        sin = ParametricFunction(
            lambda t: np.array([np.sin(t), t, 0]),
            color = YELLOW, 
            t_range = [-TAU, TAU])

        self.play(Create(axes), Create(sin))
        self.wait(2)

        rectangles = axes.get_riemann_rectangles(sin, x_range = [0,5], dx
                                                 = 0.2)


        self.begin_ambient_camera_rotation(rate = 2) 

        self.play(Write(rectangles))

        self.wait(2)

