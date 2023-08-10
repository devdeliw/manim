from manim import * 

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


