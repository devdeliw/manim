from manim import * 
import numpy as np

class Test(Scene):
    def construct(self):
        number_plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.play(ShowCreation(number_plane))

class Hello3dWorld(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(x_range = (-6, 6, 1), y_range = (-5, 5, 1), z_range
        = (-4, 4, 1), x_length = 10, y_length = 10, z_length = 10)
        

        self.set_camera_orientation(phi = 80*DEGREES, theta = -40*DEGREES, distance = 6)
       
        text3d = Tex("Hello 3d World").scale(2)
        text3d.rotate(PI/2, axis = RIGHT)

        text2d = Tex("Hello Viewer").scale(2) 
        text2d.to_edge(UP + RIGHT)
        
        self.add_fixed_in_frame_mobjects(text2d)

        self.play(Create(axes))

        self.play(Create(text3d))

        self.play(Create(text2d))

        self.move_camera(phi = 45*DEGREES, theta = 45*DEGREES, distance = 6)
        

        self.begin_ambient_camera_rotation(rate = 2)
        
        self.wait(5)

        self.stop_ambient_camera_rotation()

class ParametricCurve3d(ThreeDScene):
    def construct(self):
       
        axes = ThreeDAxes(x_range = (-5, 5, 1), y_range = (-5, 5, 1), z_range
        = (-5, 5, 1), x_length = 8, y_length = 8, z_length = 8)
        
       
        self.set_camera_orientation(phi = 75*DEGREES, theta = 45*DEGREES,
                                    distance = 9)
        self.add(axes)

        curve1 = ParametricFunction(lambda t: np.array([np.cos(t), np.sin(3*t),
        np.cos(5*t)]), color = YELLOW, t_range = [-TAU, TAU])
        
        curve2 = ParametricFunction(lambda t:
                                   np.array([np.exp(-0.1*t)*np.cos(t),
                                             np.exp(-0.1*t)*np.sin(t), 
        2*t]), color = RED, t_range = [-TAU, TAU])
        


        self.begin_ambient_camera_rotation(rate = 0.9)
        
        self.play(Create(curve1), run_time = 2)
        self.wait()
        self.play(Transform(curve1, curve2))
        self.wait()

class ParametricSurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range = (-5, 5, 1), 
            y_range = (-5, 5, 1), 
            z_range = (-5, 5, 1), 
            x_length = 8, 
            y_length = 8, 
            z_length = 8
        )

        self.add(axes)
        self.set_camera_orientation(phi = 70*DEGREES, theta = 45*DEGREES,
                                    distance = 6)
        self.begin_ambient_camera_rotation(rate = 0.2)


        bowl = Surface(
            lambda u, v: np.array([np.cos(v)*u, np.sin(v)*u, u**2]),
            v_range = [0, TAU], 
            resolution = [5, 16], 
            checkerboard_colors = [MAROON_C, MAROON_E]
        )
        
        self.play(Create(bowl.scale(2)), run_time = 8)
        self.wait(2)


class IceCream(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes(
            x_range = (-5, 5, 1), 
            y_range = (-5, 5, 1), 
            z_range = (-5, 5, 1), 
            x_length = 5, 
            y_length = 5, 
            z_length = 5
        )

        self.add(axes)
        self.set_camera_orientation(phi = 65*DEGREES, theta = 0*DEGREES,
                                    distance = 7)
        
        cone = Surface(lambda u, v: np.array([0.5*u*np.cos(v),
                                                        0.5*u*np.sin(v),
                                                          u]),v_range = [0,
                                                                         TAU], 
                       u_range = [0, 2],
        resolution = (4, 12), checkerboard_colors = [GREY_BROWN, GREY_BROWN])
        
        sphere = Surface(lambda u, v:
                                   np.array([0.5*np.cos(u)*np.cos(v),
                                             0.5*np.cos(u)*np.sin(v),
                                               0.5*np.sin(u) + 2.5]), v_range
                                                 = [0, TAU], u_range = [-PI/2,
                                                                        PI/2],
        resolution = (4, 12), checkerboard_colors = [MAROON_A,
                                                     MAROON_B]).scale(2)
        
        self.play(Create(cone), run_time = 3)
        self.play(Create(sphere), run_time = 4)
        self.wait(2)


        HeatedSurface = Surface(lambda u, v: np.array([u, v,
                                                                 np.sin(v)
                                                                 + np.cos(u)]),
                                v_range = [-5, 5], u_range = [-5,5],
        resolution = (5, 16), checkerboard_colors = [RED, RED])
        
        CooledSurface = Surface(lambda u, v: np.array([u, v,
                                                                 0.1*np.cos(v)
                                                                   + 0.2*np.sin(u)]),
                                u_range = [-5, 5], v_range = [-5, 5], 
        resolution = (5, 16), checkerboard_colors = [BLUE, BLUE])
        
        self.begin_ambient_camera_rotation(rate = 0.3)
        

        group = VGroup().add(cone, sphere) 

        self.play(Transform(group, HeatedSurface), run_time = 2)

        self.wait(2) 

        self.play(Transform(group, CooledSurface), run_time = 4)

        self.wait(2)

