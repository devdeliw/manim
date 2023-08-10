from manim import * 
import numpy as np

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

    
        self.play(stream_lines.animate.scale(2))
        self.wait()


        group = VGroup(stream_lines)
        self.play(FadeOut(group), run_time = 2)

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
        light_stream.end_animation()


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
        
        self.begin_ambient_camera_rotation(rate = 0.05)

        electric_field = ParametricFunction(
            lambda t: np.array([t, np.sin(t), 0]),
            color = PURE_RED, 
            t_range = [0, 3*PI])
    
        e_area = axes.get_area(
                electric_field, 
                x_range = (0, 6*PI), 
                color = RED_A,
                opacity = 0.4
        )

        magnetic_field = ParametricFunction(
            lambda t: np.array([t, 0, np.sin(t)]),
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
                  Write(e_area),
                  Write(m_area),
                  stream_lines.create(),
                  run_time = 8
        )


