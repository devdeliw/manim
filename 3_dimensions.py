from manim import *
from manimlib.imports import *
import numpy as np

class Hello3dWorld(ThreeDScene):
    def construct(self):
        axis_config = { 
            "x_min": -5,
            "x_max": 5,
            "y_min": -5,
            "y_max": 5, 
            "z_min": -5, 
            "z_max": 5,
        }
        axes = ThreeDAxes(**axis_config)
        self.set_camera_orientation(phi = 80*DEGREES, theta = -40*DEGREES, distance = 6)
       
        text3d = TextMobject("Hello 3d World").scale(2)
        text3d.rotate(PI/2, axis = RIGHT)

        text2d = TextMobject("Hello Viewer").scale(2) 
        text2d.to_edge(UP + RIGHT)
        
        self.add_fixed_in_frame_mobjects(text2d)

        self.play(ShowCreation(axes))

        self.play(ShowCreation(text3d))

        self.play(ShowCreation(text2d))

        self.move_camera(phi = 45*DEGREES, theta = 45*DEGREES, distance = 6)
        

        self.begin_ambient_camera_rotation(rate = 2)
        
        self.wait(5)

        self.stop_ambient_camera_rotation()
         
