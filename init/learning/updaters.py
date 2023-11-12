from manim import * 

class ValueTracker(Scene):
    def construct(self):
        a = ValueTracker(1)
        ax = Axes(x_range = [-2,2,1], y_range = [-8.5, 8.5, 1], x_length = 4,
                  y_length = 6)
        
        parabola = ax.plot(lambda x: x**2 , color = RED)    
        parabola.add_updater(lambda mob: mob.become(ax.plot(lambda x:
                                                            a.get_value()
                                                            * x**2, color
                                                            = RED)))
        a_number = DecimalNumber(
                a.get_value(),
                color = RED,
                num_decimal_places = 3,
                show_ellipsis = True
        )

        a_number.add_updater(
                lambda mob: mob.set_value(a.get_value()).next_to(parabola,
                                                                 RIGHT)
        )

        self.add(ax, parabola, a_number)
        self.play(a.animate.set_value(2))
        self.play(a.animate.set_value(-2))
        self.play(a.animate.set_value(1))
        self.wait(1)

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

class Paradox(Scene):
    def construct(self):

        axes = (Axes(x_range = [0,10,1], y_range = [0,20,5], x_length = 9,
                    y_length = 6, axis_config = {"include_numbers": True,
                                                 "include_tip":
                                                 False},).to_edge(DL)) 


        func = axes.plot(
                lambda x: 0.1 * (x-2) * (x-5) * (x-7) + 7, x_range = [0,10],
                color = BLUE
        )

        x = ValueTracker(7)
        dx = ValueTracker(2) 

        secant = always_redraw( 
            lambda: axes.get_secant_slope_group(
                x = x.get_value(),
                graph = func,
                dx = dx.get_value(), 
                dx_line_color = YELLOW,
                dy_line_color = ORANGE,
                dx_label = "dx", 
                dy_label = "dy", 
                secant_line_color = GREEN,
                secant_line_length = 8
            )
        )

        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(),
                              func.underlying_function(x.get_value()))))
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p((x).get_value() + dx.get_value(),
                              func.underlying_function(x.get_value()
                                                       + dx.get_value()),
                              )
                     )
            )

        self.add(axes, axes_labels, func)
        self.play(Create(VGroup(dot1, dot2, secant)))
        self.play(dx.animate.set_value(0.001), run_time = 8) 
        self.wait(2) 
        self.play(x.animate.set_value(1), run_time = 5) 
        self.wait()
        self.play(x.animate.set_value(7), run_time =5)
        self.wait()
        self.play(dx.animate.set_value(2), run_time = 6) 
        self.wait

class ValueTrackerExample(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        label = Dot(radius=3).add_updater(lambda x : x.set_x(tracker.get_value()))
        self.add(label)
        self.add(tracker)
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(2)


def get_horizontal_line_to_graph(axes, functino, x, width, color): 
    result = VGroup()
    line = DashedLine(
            start = axes.c2p(0, function.underlying_function(x)), 
            end = axes.c2p(x, function.underlying_function(x)), 
            stroke_width = width,
            stroke_color = color,
    )
    dot = Dot().set_color(color).move_to(axes.c2p(x,
                                                  function.underlying_function(x)))
    result.add(line, dot)
    return result

class Derivatives(Scene):
    def construct(self):
        k = ValueTracker(-3)

        plane1 = (
            NumberPlane(x_range = [-3,4,1], x_length = 5, y_range = [-8,9,2],
                        y_length = 5).add_coordinates().shift(LEFT * 3.5)
        )

        func1 = plane1.plot(lambda x: (1/3)*x ** 3, x_range = [-3,3], color
                            = RED_C) 

        func1_lab = (
            MathTex("f(x) = \\frac{1}{3} {x}^{3}").set(width
                                                       = 2.5).next_to(plane1,
                                                                      UP, buff
                                                                      = 0.2).set_color(RED_C))

        moving_slope = always_redraw(
                lambda: plane1.get_secant_slope_group(
                    x = k.get_value(), 
                    graph = func1, 
                    dx = 0.05, 
                    secant_line_length = 4,
                    secant_line_color = YELLOW, 
                )
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: x**2, x_range = [-3, k.get_value()], color = GREEN
            )
        )

        func2_lab = (
                MathTex("f(x) = {x} ^ {2}").set(width = 2.5).next_to(plane2,
                                                                     UP, buff
                                                                     = 0.2).set_color(GREEN))

        moveing_h_line = always_redraw(lambda:
                                       get_horizontal_line_to_graph(axes
                                                                    = plane2,
                                                                    function
                                                                    = func2,
                                                                    x = k.get_value(),
                                                                    width = 4, 
                                                                    color
                                                                    = YELLOW))

        slope_value_text = (
                Tex("Slope value: ").next_to(plane1, DOWN, buff
                                             = 0.1).set_color(YELLOW).add_background_rectangle())
        slope_value = always_redraw(
                lambda: DecimalNumber(num_decimal_places = 1)
                .set_value(func2.underlying_function(k.get_value()))
                .next_to(slope_value_text, RIGHT, buff = 0.1) 
                .set_color(YELLOW)).add_background_rectangle()


        self.play( 
            LaggedStart(
                DrawBorderThenFill(plane1), 
                DrawBorderThenFill(plane2), 
                Create(func1), 
                Write(func1_lab), 
                Write(func2_lab), 
                run_time = 5, 
                lag_ratio = 0.5, 
            )
        )

        self.add(moving_slope, moving_h_line, func2, slope_value,
                 slope_value_text, dot)
        self.play(k.animate.set_value(3), run_time = 15, rate_func = smooth) 
        self.wait(3)
