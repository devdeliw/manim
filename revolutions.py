from manim import * 

class One(ThreeDScene):
    def construct(self): 
        
        l = 2
        w = 4
        h = 1

        rect_prism = Prism(dimensions = [l,w,h]).to_edge(LEFT, buff = 1)

        kwargs = {"stroke_color": BLUE_D, "fill_color": BLUE_B, "fill_opacity":
                  0.8} 

        bottom = Rectangle(width = w, height = 1, **kwargs)

        s1 = Rectangle(height = h, width = w, **kwargs).next_to(bottom, UP, buff = 0)
        s2 = Rectangle(height = h, width = w, **kwargs).next_to(bottom, DOWN, buff = 0)
        l1 = Rectangle(height = 1, width = h, **kwargs).next_to(bottom, LEFT, buff = 0)
        l2 = Rectangle(height = 1, width = h, **kwargs).next_to(bottom, RIGHT, buff = 0)
        top = Rectangle(width = w, height = 1, **kwargs).next_to(s1, UP, buff = 0)
        net = VGroup(top, bottom, s1, s2, l1, l2).rotate(-PI/2).to_edge(RIGHT, buff = 1)

            
        arrow = Line(start = rect_prism.get_right(), end = net.get_left(), buff
                     = 0.2).add_tip()

        self.begin_ambient_camera_rotation()
       
        self.set_camera_orientation(
            phi = 45*DEGREES,
            theta = 45*DEGREES, 
        )

        self.play(Create(rect_prism))
        self.play(
                LaggedStart(Create(arrow), Transform(rect_prism.copy(), net)),
                run_time = 2, 
                lag_ratio = 0.5, 
        )

        self.wait() 
        self.play(FadeOut(Group(*self.mobjects)))
        self.stop_ambient_camera_rotation()

        self.set_camera_orientation(
            phi = 0*DEGREES,
            theta = -90*DEGREES, 
        )

        x = ValueTracker(0)

        text = Tex("Surface Area of a Solid Revolution?") 

        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

        self.begin_ambient_camera_rotation()
        self.move_camera(
            phi = 45*DEGREES, 
            theta = -45*DEGREES
        )

        axes = ThreeDAxes(
            x_range = (0, 4.1, 1), 
            y_range = (-4, 4.1, 1), 
            z_range = (-4, 4.1, 1), 
            x_length = 5, 
            y_length = 5, 
            z_length = 5
        ).add_coordinates()

        function = axes.plot(lambda x: 0.25 * x ** 2, x_range = [0,4], color
                                  = YELLOW)
        area = axes.get_area(graph = function, x_range = [0,4], color
                              = [BLUE_B, BLUE_D])

        surface = Surface(
            lambda u, v: axes.c2p(v, 0.25 * v ** 2 * np.cos(u), 0.25 * v **
                                  2 * np.sin(u)),
            u_range = [0, 2*PI],
            v_range = [0, 4], 
            checkerboard_colors = [BLUE_B, BLUE_D]
        )

        self.play(
                LaggedStart(Create(axes), Create(function), Create(area),
                            Create(surface)), 
                run_time = 4, 
                lag_ratio = 0.5, 
                )

        self.play(Rotating(VGroup(function, area), axis = RIGHT, radians
                           = 2 * PI, about_point = axes.c2p(0,0,0),), run_time
                  = 5, rate_func = smooth,)
        self.wait(3)

