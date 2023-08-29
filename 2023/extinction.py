from manim import * 
import numpy as np
import math

class Galaxy(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(
            phi = 0*DEGREES,
            theta = 0*DEGREES, 
            gamma = 0*DEGREES,
            distance = 20
        )

        self.begin_ambient_camera_rotation(rate = 0.05)

        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3

        stream_lines = StreamLines(func, 
                                   colors = [YELLOW, BLUE, PINK],
                                   max_anchors_per_line= 20, 
                                   padding = 20
        )

        stream_lines.scale(3)

        self.play(stream_lines.create(),
                  run_time = 10
        )

        black_hole = ImageMobject("~/Desktop/manim/2023/media/images/blackhole.png")
        black_hole.scale(0.1)
    
        self.play(stream_lines.animate.scale(8), FadeIn(black_hole))
        self.wait()

        group = VGroup(stream_lines)
        self.play(FadeOut(group), run_time = 2)

        self.play(FadeOut(black_hole))

        self.stop_ambient_camera_rotation()

class LightBeam(Scene):
    def construct(self):

        div_func = lambda p: p/3


        light_stream = StreamLines(div_func,
                                   max_anchors_per_line = 20,
                                   stroke_width = 1
        )

        self.add(light_stream)

        light_stream.start_animation(warm_up = True,
                                     flow_speed = 2,
                                     time_width = 0.8,
                                     rate_func = rate_functions.ease_in_cubic
        )
        self.wait(5)

        earth = ImageMobject("~/Desktop/manim/2023/media/images/earth.png")
        earth.scale(0.005 )
        self.play(earth.animate.scale(35), run_time = 4)


        self.play(FadeOut(light_stream), FadeOut(earth))

        self.wait(1)

class LightWave(ThreeDScene):
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
            phi = 80*DEGREES,
            theta = 15*DEGREES, 
            distance = 3
        )
        
        self.begin_ambient_camera_rotation(rate = 0.08)

        electric_field = ParametricFunction(
            lambda t: np.array([t, 0.3*np.sin(t), 0]),
            color = PURE_RED, 
            t_range = [0, 3*PI])
    
        e_area = axes.get_area(
                electric_field, 
                x_range = (0, 6*PI), 
                color = RED_A,
                opacity = 0.4
        )

        magnetic_field = ParametricFunction(
            lambda t: np.array([t, 0, 0.3*np.sin(t)]),
            color = DARK_BLUE, 
            t_range = [0, 3*PI])

        m_area = axes.get_area(
                magnetic_field, 
                x_range = (0, 6*PI),
                color = BLUE_A, 
                opacity = 0.4
        )


        func = lambda pos: ((pos[0] * UR + pos[1] * LEFT) - pos) / 3

        stream_lines = StreamLines(func,
                                   colors = [YELLOW, BLUE, PINK],
                                   max_anchors_per_line= 20,
                                   padding = 20
        )

        stream_lines.scale(3)
        stream_lines.rotate_about_origin(angle = PI/2, axis = [0,1,0])

        self.play(Create(electric_field),
                  Create(magnetic_field),
                  Create(e_area),
                  Create(m_area),
                  stream_lines.create(),
                  run_time = 10
        )


        self.wait(3)

        group = VGroup(electric_field, magnetic_field, e_area, m_area,
                       stream_lines) 

        self.play(FadeOut(group), run_time = 2)

        self.stop_ambient_camera_rotation()

class Scattering(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(
            phi = 65*DEGREES,
            theta = 30*DEGREES, 
        )

        axes = ThreeDAxes()

        initial_wave = ParametricFunction(
            lambda t: np.array([t, np.sin(1.5*t), 0]),
            color = WHITE, 
            t_range = [-6*PI, 0])

        scattered_wave = ParametricFunction(
            lambda t: np.array([t, np.sin(1.5*t), 0]),
            color = BLUE, 
            t_range = [0, 6*PI])

        scattered_wave.rotate_about_origin(angle = PI/4, axis = [0,1,0])

        transmitted_wave = ParametricFunction(
            lambda t: np.array([t, 0.9*np.sin(1.5*t), 0]),
            color = RED, 
            t_range = [0, 6*PI])
   
        border = ParametricFunction(
            lambda t: np.array([0, 0, t]),
            color = WHITE, 
            t_range = [-TAU, TAU])

        self.begin_ambient_camera_rotation(rate = 0.1)


        self.play(Create(border), Create(initial_wave), run_time = 9, rate_func = linear)
        self.play(Create(transmitted_wave), Create(scattered_wave), run_time
                  = 9, rate_func = linear)

        group = VGroup(border, initial_wave, transmitted_wave, scattered_wave) 
        
        self.play(FadeOut(group), run_time = 2)

        self.stop_ambient_camera_rotation()

class Sunset(Scene):
    def construct(self):
       
        ax = Axes( 
            x_range = (-10, 10), 
            y_range = (-10, 10),
            x_length = 10, 
            y_length = 10
        )

        stream_lines = StreamLines(lambda p: p/3,
                                   colors = [RED, ORANGE, BLUE, PURPLE],
                                   stroke_width = 20
        )

        sun = Circle(radius = 1, color = YELLOW, fill_opacity = 1)

        sun.shift(4*DOWN)
        stream_lines.shift(4*DOWN)
        group = VGroup(sun, stream_lines)
        group.scale(2)


        self.play(FadeIn(sun), run_time = 2)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up = True,
                                     flow_speed = 3,
                                     time_width = 0.4,
                                     rate_func = rate_functions.ease_in_cubic
        )
        self.wait(10)

        group3 = VGroup(sun, stream_lines) 
        self.play(FadeOut(group3), run_time = 2)

class JWST(ThreeDScene):
    def construct(self):

        ax = Axes( 
            x_range = (-10, 10), 
            y_range = (-10, 10),
            x_length = 10, 
            y_length = 10
        )
        
        light_1 = ax.plot(
                lambda x: np.sin(1.5*x),
                color = RED_A,
                x_range = [-20, 0]
        )
        light_1.rotate_about_origin(angle = PI/3)

        light_2 = ax.plot(
                lambda x: np.sin(3*x), 
                color = YELLOW_B,
                x_range = [-20, 0]
        )
        light_2.rotate_about_origin(angle = -PI/6)

        light_3 = ax.plot(
                lambda x: np.sin(x), 
                color = GOLD_A,
                x_range = [-20, 0] 
        )
        light_3.rotate_about_origin(angle = -PI/4)

        light_4 = ax.plot(
                lambda x: np.sin(0.8*x), 
                color = TEAL_A,
                x_range = [-20, 0]
        )

        image = ImageMobject(r"jwst.png").scale(0.3)

        light_1.shift(2*RIGHT)
        light_2.shift(2*RIGHT)
        light_3.shift(2*RIGHT)
        light_4.shift(2*RIGHT)
        image.shift(2*RIGHT)
        image.shift(0.75*DOWN)




        self.play(FadeIn(image))
        self.play(LaggedStart(Create(light_1), Create(light_2),
                              Create(light_3), Create(light_4), lag_ratio
                              = 0.25), run_time = 10)

        group = VGroup(light_1, light_2, light_3, light_4) 

        self.play(FadeOut(group), FadeOut(image), run_time = 2)
        



