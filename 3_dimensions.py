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

class ParametricCurve3d(ThreeDScene):
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
       
        self.set_camera_orientation(phi = 75*DEGREES, theta = 45*DEGREES,
                                    distance = 9)
        self.add(axes)

        curve1 = ParametricFunction(lambda t: np.array([np.cos(t), np.sin(3*t),
        np.cos(5*t)]), color = YELLOW, t_min = -TAU, t_max = TAU)
        
        curve2 = ParametricFunction(lambda t:
                                   np.array([np.exp(-0.1*t)*np.cos(t),
                                             np.exp(-0.1*t)*np.sin(t), 
        2*t]), color = RED, t_min = -TAU , t_max = TAU)
        


        self.begin_ambient_camera_rotation(rate = 0.9)
        
        self.play(ShowCreation(curve1), run_time = 2)
        self.wait()
        self.play(Transform(curve1, curve2))
        self.wait()

class ParametricSurfacesAnimation(ThreeDScene):
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
        self.add(axes)
        self.set_camera_orientation(phi = 70*DEGREES, theta = 45*DEGREES,
                                    distance = 6)
        self.begin_ambient_camera_rotation(rate = 0.2)
       
        bowl = ParametricSurface(lambda u, v: np.array([np.cos(v)*u,
                                                        np.sin(v)*u, u**2]), v_max = TAU,
        resolution = (5, 16), checkerboard_colors = [MAROON_C, MAROON_E])
        
        self.play(ShowCreation(bowl.scale(2)), run_time = 8)
        self.wait(2)


class IceCream(ThreeDScene):
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
        self.add(axes)
        self.set_camera_orientation(phi = 65*DEGREES, theta = 0*DEGREES,
                                    distance = 7)
        
        cone = ParametricSurface(lambda u, v: np.array([0.5*u*np.cos(v),
                                                        0.5*u*np.sin(v),
                                                          u]),v_min = 0, v_max
                                 = TAU, u_min = 0, u_max = 2,
        resolution = (4, 12), checkerboard_colors = [GREY_BROWN, GREY_BROWN])
        
        sphere = ParametricSurface(lambda u, v:
                                   np.array([0.5*np.cos(u)*np.cos(v),
                                             0.5*np.cos(u)*np.sin(v),
                                               0.5*np.sin(u) + 2.5]), v_min
                                                 = 0, v_max = TAU, u_min
                                                 = -PI/2, u_max = PI/2,
        resolution = (4, 12), checkerboard_colors = [MAROON_A,
                                                     MAROON_B]).scale(2)
        
        self.play(ShowCreation(cone), run_time = 3)
        self.play(ShowCreation(sphere), run_time = 4)
        self.wait(2)


        HeatedSurface = ParametricSurface(lambda u, v: np.array([u, v,
                                                                 np.sin(v)
                                                                 + np.cos(u)]),
        v_min = -5, v_max = 5, u_min = -5, u_max = 5,
        resolution = (5, 16), checkerboard_colors = [RED, RED])
        
        CooledSurface = ParametricSurface(lambda u, v: np.array([u, v,
                                                                 0.1*np.cos(v)
                                                                   + 0.2*np.sin(u)]),
        v_min = -5, v_max  = 5, u_min = -5, u_max = 5,
        resolution = (5, 16), checkerboard_colors = [BLUE, BLUE])
        
        self.begin_ambient_camera_rotation(rate = 0.3)
        

        group = VGroup().add(cone, sphere) 

        self.play(Transform(group, HeatedSurface), run_time = 2)

        self.wait(2) 

        self.play(Transform(group, CooledSurface), run_time = 4)

        self.wait(2)
