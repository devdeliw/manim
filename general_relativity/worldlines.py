from manim import * 
import math 
import numpy as np

class Intro(Scene):
    def construct(self):

        title = Tex(r" General Relativity ").scale(1.8).move_to([0, 2.5, 0])
        
        self.wait(2)
        self.play(Write(title), run_time = 2)
        self.wait(15)
        self.play(Unwrite(title), run_time = 1.5)
        self.wait(0.2)


class Surfaces(ThreeDScene):

    def param_surface(u, v):
        x = u
        y = v
        z = y * math.e ** (x**2 - 5)
        return z

    def construct(self): 

        axes = ThreeDAxes(
            x_range = (-5, 5, 5), 
            y_range = (-5, 5, 5), 
            z_range = (-5, 5, 5), 
            x_length = 5, 
            y_length = 5, 
            z_length = 5
        )    

        self.set_camera_orientation(
            phi = 60*DEGREES,
            theta = 80*DEGREES, 
            distance = 10
        )
        

        z1 = Surface( 
           lambda u, v: np.array([u, v, v * 0.3*np.sin(u) - u *0.3*np.cos(v)]), 
           resolution = (16, 32),
           v_range = [-2, 2], 
           u_range = [-2, 2],
           fill_opacity = 0.2
        ).set_opacity(0.6)

        z1.set_color_by_gradient(TEAL, MAROON, YELLOW)

        z2 = Surface(
           lambda u, v: np.array([u, v, u * 4*math.e**(-u**2 - v**2)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.2
        ).set_opacity(0.6)

        z2.set_color_by_gradient(MAROON, YELLOW, TEAL)

        z3 = Surface(
           lambda u, v: np.array([u, v, v * -0.3*np.sin(u) - u * -0.3*np.cos(v)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.2
        ).set_opacity(0.6)

        z3.set_color_by_gradient(YELLOW, MAROON, TEAL)

        z4 = Surface(
           lambda u, v: np.array([u, v, u * -4*math.e**(-u**2 - v**2)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.2
        ).set_opacity(0.6)

        z4.set_color_by_gradient(TEAL, YELLOW, MAROON)

        sheet = Surface(
           lambda u, v: np.array([u, v, 0]),
           resolution = (1, 1),
           v_range = [-4, 4],
           u_range = [-2, 2],
           fill_opacity = 0.2
        ).set_opacity(0.6).set_color([TEAL, MAROON, YELLOW])

        z11 = z1.copy()
        z12 = z1.copy()

        z21 = z2.copy()
        z22 = z2.copy()

        z31 = z3.copy()

        z41 = z4.copy()

        self.begin_ambient_camera_rotation(rate = 0.2)

        self.play(Write(z1), Write(z2), run_time = 2)
        self.wait(1)

        self.play(ReplacementTransform(z1, z3), ReplacementTransform(z2, z4), run_time = 2)
        self.play(ReplacementTransform(z3, z11), ReplacementTransform(z4, z21), run_time = 2)
        self.play(ReplacementTransform(z11, z31), ReplacementTransform(z21, z41), run_time = 2)
        self.play(ReplacementTransform(z31, z12), ReplacementTransform(z41, z22), run_time = 2)

        self.wait(2)
            
        self.play(ReplacementTransform(VGroup(z12, z22), sheet), run_time = 2)
        self.wait()
        self.play(sheet.animate.set_color([WHITE]), run_time = 2)
        self.wait(5)

        self.play(Unwrite(sheet), run_time = 1.5)
        self.wait()
        self.stop_ambient_camera_rotation()


class Logo(Scene):
    def construct(self):
        
        cat = SVGMobject("/Users/devaldeliwala/downloads/cat.svg", height = 4.4, width = 4.4).set_color([TEAL_B, MAROON_A])
        self.play(DrawBorderThenFill(cat), run_time = 2)
        self.wait(4)
        self.play(Unwrite(cat), run_time = 1.5)
        self.wait()


class ScienceClic(Scene):
    def construct(self):
        
        thumb = ImageMobject("/Users/devaldeliwala/desktop/thumb3.png").scale(0.4)
        logo = ImageMobject("/Users/devaldeliwala/desktop/logo.png").scale(0.3).move_to([-4.1, -2.2, 0])

        thumbrect1 = SurroundingRectangle(thumb).set_color([TEAL_B, PINK, YELLOW])

        self.play(Write(thumbrect1), FadeIn(thumb), run_time = 1.5)
        self.play(FadeIn(logo))

        self.wait(5)

        self.play(Unwrite(thumbrect1), FadeOut(thumb), FadeOut(logo))
        self.wait()


class Flat(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(
            phi = 75*DEGREES,
            theta = 30*DEGREES, 
            distance = 5
            )

        vline = Line([0, -3, 0], [0, 3, 0])
        self.add_fixed_in_frame_mobjects(vline)
        self.remove(vline)
        vline.shift(LEFT*3.5)
        t = MathTex(r"t").move_to([0.3, 3, 0]).scale(0.7).shift(LEFT*3.5)
        self.add_fixed_in_frame_mobjects(t)
        self.remove(t)
        
        slice1 = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range = [-2, 2],
            v_range = [-2, 2], 
            resolution = [8, 8], 
        ).set_color([WHITE]).move_to([0, 0, -1]).set_opacity(0.2)

        slice2 = slice1.copy().move_to([0, 0, 0])
        slice3 = slice1.copy().move_to([0, 0, 1])

        slices = VGroup(slice1, slice2, slice3)

        self.play(Write(slices), run_time = 2)
        self.wait(2)
        self.play(Write(vline), run_time = 1)
        self.wait()
        self.play(Write(t))

        self.wait(4)

        worldline = ParametricFunction(
            lambda t: np.array([0.7*np.sin(t), 0.7*np.cos(t), t]),
            color = YELLOW, 
            t_range = [-2.5, 2.5]
        )

        dot1 = Dot3D([0.7* -0.84, 0.7*0.54, -1]).scale(0.4)
        dot2 = Dot3D([0, 0.7, 0]).scale(0.4)
        dot3 = Dot3D([0.7*0.84, 0.7*0.54, 1]).scale(0.4)

        dot = VGroup(dot1, dot2, dot3)

        worldline_text = Tex(r"worldline").move_to([0, -2.8, 0]).set_color([TEAL_B, MAROON_A]).scale(1.2)
        self.add_fixed_in_frame_mobjects(worldline_text)
        self.remove(worldline_text)

        self.play(Write(worldline), Write(dot), run_time = 2)
        
        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(6)

        self.play(Write(worldline_text))
        self.wait(4)

        self.play(Unwrite(VGroup(slices, vline, t,  dot, worldline, worldline_text)), run_time = 6)
        self.stop_ambient_camera_rotation()

        self.wait(2)


class Chapter1(ThreeDScene):
    def construct(self):
        
        title = Tex("Chapter 1").scale(2).move_to([0, 0.5, 0])
        title2 = Tex("Special Relativity and Flat Spacetime").scale(1).move_to([0, -0.5, 0])
        self.set_camera_orientation(
            phi = 60*DEGREES,
            theta = 80*DEGREES, 
            distance = 10 
        )
        

        self.add_fixed_in_frame_mobjects(title, title2)
        self.remove(title, title2)

        self.play(Write(title))
        self.wait()

        z1 = Surface(
           lambda u, v: np.array([u, v, v * 0.3*np.sin(u) - u *0.3*np.cos(v)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z1.set_color_by_gradient(TEAL, MAROON, YELLOW)

        z2 = Surface(
           lambda u, v: np.array([u, v, u * 4*math.e**(-u**2 - v**2)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z2.set_color_by_gradient(MAROON, YELLOW, TEAL)

        z3 = Surface(
           lambda u, v: np.array([u, v, v * -0.3*np.sin(u) - u * -0.3*np.cos(v)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z3.set_color_by_gradient(YELLOW, MAROON, TEAL)

        z4 = Surface(
           lambda u, v: np.array([u, v, u * -4*math.e**(-u**2 - v**2)]),
           resolution = (16, 32),
           v_range = [-2, 2],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2)

        z4.set_color_by_gradient(TEAL, YELLOW, MAROON)

        sheet = Surface(
           lambda u, v: np.array([u, v, 0]),
           resolution = (1, 1),
           v_range = [-4, 4],
           u_range = [-2, 2],
           fill_opacity = 0.1
        ).set_opacity(0.2).set_color([TEAL, MAROON, YELLOW])

        z11 = z1.copy()
        z12 = z1.copy()

        z21 = z2.copy()
        z22 = z2.copy()

        z31 = z3.copy()

        z41 = z4.copy()

        self.play(DrawBorderThenFill(title2), Write(z1), Write(z2), run_time = 1.5)
        self.play(ReplacementTransform(z1, z3), ReplacementTransform(z2, z4), run_time = 2)
        self.play(ReplacementTransform(z3, z11), ReplacementTransform(z4, z21), run_time = 2)

        self.play(Unwrite(VGroup(title, title2, z11, z21)), run_time = 2)

        self.wait()

class Flat2(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(
            phi = 75*DEGREES,
            theta = -30*DEGREES,
            distance = 10
        )

        title2 = Tex(r" Special Relativity ").to_edge(UL)
        self.add_fixed_in_frame_mobjects(title2)
        self.remove(title2)

        lightcone_up = Cone(0.3, 0.3, [0,0,-1], resolution = 5).set_color([YELLOW])
        lightcone_down = Cone(0.3, 0.3, [0,0,1], resolution = 5).set_color([YELLOW])
        lightcone = VGroup(lightcone_up, lightcone_down)

        lightcone1 = lightcone.copy().move_to([0.7*-0.84, 0.7*0.54, -1])
        lightcone2 = lightcone.copy().move_to([0, 0.7, 0])
        lightcone3 = lightcone.copy().move_to([0.7*0.84, 0.7*0.54, 1])
        lightcone4 = lightcone.copy().move_to([1, -2.4, 1.4])
        lightcone5 = lightcone.copy().move_to([-1.8, 1.3, 0.5])

        lightcones = VGroup(lightcone1, lightcone2, lightcone3, lightcone4, lightcone5).set_color([TEAL]).set_opacity(0.4)

        present = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range = [-2, 2],
            v_range = [-2, 2],
            resolution = [1, 1],
        ).set_color([TEAL_B]).set_opacity(0.2).scale(1.2)

        axes = ThreeDAxes(
            x_range = (-3, 3, 3),
            y_range = (-3, 3, 3),
            z_range = (-3, 3, 3),
            x_length = 5,
            y_length = 5,
            z_length = 5,
            axis_config={'tip_shape': StealthTip}
        )

        labels = axes.get_axis_labels(
            Tex("SPACE").scale(0.7), Tex(r"SPACE").scale(0.7),
            Tex(r"$t$")
        )

        worldline2 = ParametricFunction(
            lambda t: np.array([0.7*np.sin(t), 0.7*np.cos(t), t]),
            color = YELLOW,
            t_range = [-2.5, 2.5]
        )

        past = Tex(r"\textit{past}").move_to([3, -1.7, 0]).set_color([TEAL_B,MAROON_A])
        future = Tex(r"\textit{future}").move_to([3, 1.7, 0]).set_color([YELLOW,PINK])
        self.add_fixed_in_frame_mobjects(past, future)
        self.remove(past, future)


    
        self.play(Write(title2), run_time = 1)
        self.play(Write(lightcone.scale(6).set_opacity(0.3).set_color([TEAL])),
                  Write(present),
                  Write(axes),
                  Write(labels), run_time = 5
        )

        self.wait(6)

        self.play(DrawBorderThenFill(VGroup(past, future)), run_time = 2)

        self.wait(3)
        self.play(Unwrite(VGroup(lightcone, present, axes, labels, past, future)), run_time = 2)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate = 0.1)

        self.play(Write(worldline2), Write(lightcones), run_time = 2)
        self.wait(10)

        self.play(Unwrite(VGroup(title2, worldline2, lightcones)), run_time = 2)
        self.stop_ambient_camera_rotation()
        self.wait()


class MinkowskiSpace(ThreeDScene):
    def construct(self): 
        
        spacetime = Surface(
            lambda u, v: np.array([u, v, -1.5]),
            u_range = [-3, 3],
            v_range = [-3, 3], 
            resolution = [8, 8], 
        ).set_color([GRAY_E])

        self.set_camera_orientation(
            phi = 75*DEGREES,
            theta = 30*DEGREES, 
            distance = 5
        )

        self.begin_ambient_camera_rotation(rate = 0.1)

        self.play(Write(spacetime), run_time = 2)

        self.wait(3)
        self.stop_ambient_camera_rotation()

        self.move_camera(
            phi = 0*DEGREES, 
            theta = -90*DEGREES,
            distance = 3, 
            run_time = 2
        )

        self.wait()

        axes = ThreeDAxes( 
            x_range = (-5, 5, 5), 
            y_range = (-5, 5, 5),
            z_range = (-5, 5, 5),
            x_length = 5.5, 
            y_length = 5.5,
            z_length = 5.5,
            axis_config={'tip_shape': StealthTip}
        ) 

        labels = axes.get_axis_labels(
            Tex(r"$x$"), Tex(r"$y$"), Tex(r"$z$")
        )

        self.play(Write(axes), Write(labels))
        self.wait(4)

        v1 = Arrow3D([0, 0, 0], [-2, 2, -2], resolution=3)
        v2 = Arrow3D([0, 0, 0], [2, 0.6, 3], resolution=3)
        s = Arrow3D([2, 0.6, 3], [-2, 2, -2], resolution = 8).set_color_by_gradient(TEAL_B, PINK, YELLOW)

        self.play(spacetime.animate.set_opacity(0.4), run_time = 2)
        self.wait(1)

        self.play(Write(VGroup(v1, v2)))

        self.wait(2)

        self.play(Write(s), run_time = 2)

        slabel = MathTex(r"\Delta s").move_to([0.5, 1.6, 0])
        norm = MathTex(r" (\Delta s)^2 = (\Delta x)^2 + (\Delta y)^2 ").to_edge(DOWN).scale(0.8)
        self.add_fixed_in_frame_mobjects(slabel, norm)
        self.remove(slabel, norm)

        self.wait(2)

        self.play(Write(slabel))
        self.wait(2)
        self.play(Write(norm), run_time = 2)

        self.wait(4)

        self.play(Unwrite(VGroup(norm, slabel)))
        
        self.move_camera(
            phi = 70*DEGREES, 
            theta = -180*DEGREES,
            distance = 5,
            run_time = 2
        )

        self.play(spacetime.animate.move_to([0, 0, 2.1]), run_time = 2)
        self.play(spacetime.animate.move_to([0, 0, -1.5]), run_time = 2)
        
        self.wait(2)

        norm3d = MathTex(r" (\Delta s)^2 = (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2 ").scale(0.8).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(norm3d)
        self.remove(norm3d)

        self.play(Write(norm3d), run_time = 1)

        self.wait(5)

        self.play(Unwrite(norm3d))

        cube = Cube(side_length=4, fill_opacity=0.3, fill_color=GRAY_D)

        self.move_camera(
            phi = 78*DEGREES, 
            theta = 30*DEGREES,
            distance = 2,
            run_time = 2
        )

        self.play(Unwrite(VGroup(v1, v2, s)), run_time = 1)
        self.wait(2)
        
        axes2 = ThreeDAxes(
            x_range = (-5, 5, 5), 
            y_range = (-5, 5, 5), 
            z_range = (0, 5, 5), 
            x_length = 7, 
            y_length = 7, 
            z_length = 5, 
            axis_config={'tip_shape': StealthTip}
        ).move_to([0,0,2.5])
        
        labels2 = axes.get_axis_labels(
            Tex(r"SPACE").scale(0.7), Tex(r"SPACE").scale(0.7), Tex(r"")
        )

        t = MathTex(r"t").move_to([0, 0, 3.45])
        self.add_fixed_orientation_mobjects(t)
        self.remove(t)

        arr1 = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([2, 2, 1]),
            resolution = 5, 
            color = WHITE, 
        )
        
        arr2 = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([1, 2, 4]),
            resolution = 5, 
            color = WHITE, 
        )

        sdiff = Arrow3D(
            start = np.array([2, 2, 1]),
            end = np.array([1, 2, 4]),
            resolution = 8, 
        ).set_color_by_gradient(TEAL_B, YELLOW, PINK)
        
        
        VGroup(axes2, arr1, arr2, sdiff, labels2).move_to([0, 0, 0.45])

        self.play(ReplacementTransform(VGroup(axes, labels), VGroup(axes2, labels2)), Write(t), run_time = 2)
        self.wait()
        self.play(ReplacementTransform(spacetime, cube), run_time = 2)

        self.begin_ambient_camera_rotation(rate = 0.1)

        self.wait(2)

        self.play(Write(VGroup(arr1, arr2)), run_time = 2)
        
        self.wait(2)

        self.play(Write(sdiff), run_time = 2) 

        self.wait(6)

        spacetime_interval = MathTex(r" (\Delta s)^2 = -(c\Delta t)^2 + (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2").scale(0.7).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(spacetime_interval)
        self.remove(spacetime_interval)

        spacetime_interval2 = MathTex(r" (\Delta s)^2 = -(c\Delta t')^2 + (\Delta x')^2 + (\Delta y')^2 + (\Delta z')^2").scale(0.7).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(spacetime_interval2)
        self.remove(spacetime_interval2)

        self.play(Write(spacetime_interval), run_time = 2)

        self.wait(10)

        self.play(Unwrite(spacetime_interval), run_time = 1)
        
        self.wait(2)

        self.play(Rotate(VGroup(axes2, labels2, t, arr1, arr2, sdiff, cube), angle = PI/4, axis = [1,-1,0]), run_time = 2)

        self.play(Write(spacetime_interval2), run_time = 2)

        self.wait(5)

        minkowski = Tex(r" Minkowski Spacetime ").scale(1.2).set_color([TEAL_B, MAROON_A]).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(minkowski)
        self.remove(minkowski)

        self.play(Unwrite(spacetime_interval2), run_time = 2)
        self.wait(5)

        self.play(DrawBorderThenFill(minkowski), run_time = 2)

        self.wait(6)

        self.play(Unwrite(VGroup(cube, axes2, labels2, t, arr1, arr2, sdiff, minkowski)), run_time = 6)
        self.wait()

        self.stop_ambient_camera_rotation()


class MinkowskiMetric(Scene):
    def construct(self):

        s = MathTex(r" (\Delta s)^2 = -(c\Delta t)^2 + (\Delta x)^2 + (\Delta y)^2 + (\Delta z)^2 ")
        srect = SurroundingRectangle(s).set_color([TEAL_B, PINK, YELLOW])

        sf = VGroup(s, srect)

        self.play(Write(sf), run_time = 2)
        self.wait()
        self.play(sf.animate.move_to([0, 2, 0]))


        metric = MathTex(r" \eta_{\mu \nu} = \begin{pmatrix} -1 & 0 & 0 & 0 \\ \
                                            0 & 1 & 0 & 0 \\ \
                                            0 & 0 & 1 & 0 \\ \
                                            0 & 0 & 0 & 1 \
                                            \end{pmatrix} "
                ).move_to([0, -2, 0])

        xmu = MathTex(r" x^\mu : ").move_to([-0.8, 0, 0])
        x0ct = MathTex(r" x^0 = ct ").move_to([0.75, 0.9, 0])
        x1x = MathTex(r" x^1 = x ").move_to([0.7, 0.3, 0])
        x2y = MathTex(r" x^2 = y ").move_to([0.7, -0.3, 0])
        x3z = MathTex(r" x^3 = z ").move_to([0.7, -0.9, 0])

        greek_notation = VGroup(xmu, x0ct, x1x, x2y, x3z).move_to([0, -1, 0])

        x0 = MathTex(r" x^0 ").move_to([-0.4, -0.3, 0])
        x1 = MathTex(r" x^1 ").move_to([0.5, -0.3, 0])
        x2 = MathTex(r" x^2 ").move_to([1.3, -0.3, 0])
        x3 = MathTex(r" x^3 ").move_to([2.15, -0.3, 0])

        minkmetric = VGroup(metric, x0, x1, x2, x3).shift(UP*1)
        
        self.wait(2)

        self.play(Write(greek_notation), run_time = 2)

        self.wait(5)

        self.play(ReplacementTransform(greek_notation[1], x0), 
                  ReplacementTransform(greek_notation[2], x1),
                  ReplacementTransform(greek_notation[3], x2), 
                  ReplacementTransform(greek_notation[4], x3), 
                  FadeOut(greek_notation[0]),
                  run_time = 2
        )

        self.wait()

        self.play(Write(metric), run_time = 2)

        snew = MathTex(r" (\Delta s)^2", r"=", r"\eta_{\mu \nu}", r"\Delta x^\mu \Delta x^\nu ").move_to([0, 2, 0])
        snewrect = SurroundingRectangle(snew).set_color([TEAL_B, PINK, YELLOW]).move_to([0,2,0])

        minkowski_metric = Tex("Minkowski Metric").to_edge(DOWN).set_color([TEAL_B, MAROON_A]).scale(1.5)

        self.wait(3)

        self.play(DrawBorderThenFill(minkowski_metric), run_time = 2)

        self.wait(3)

        self.play(Unwrite(minkowski_metric), run_time = 1)

        self.wait(2)

        snewf = VGroup(snew, snewrect)

        self.play(ReplacementTransform(sf, snewf), run_time = 2)

        summation_notation = Tex(r" Einstein Summation Notation ").set_color([TEAL_B, MAROON_A])

        self.wait(3)
        self.play(FadeOut(VGroup(x0, x1, x2, x3)))
        self.play(snewf.animate.move_to([-2.8, 2, 0]), metric.animate.move_to([2.8, 2, 0]))
        self.play(snew[2].animate.set_color([TEAL_B]), snew[3].animate.set_color([MAROON_A]), run_time = 2)

        sdef = MathTex(r" (\Delta s)^2 =  ", r" -", r"\Delta x^0 \Delta x^0 ", r"+", r"\Delta x^1 \Delta x^1 ", r"+", r"\Delta x^2 \Delta x^2", r"+", r"\Delta x^3 \Delta x^3").move_to([0, -2, 0])

        sdef[1].set_color([TEAL_B])
        sdef[2].set_color([MAROON_A])
        sdef[4].set_color([MAROON_A])
        sdef[6].set_color([MAROON_A])
        sdef[8].set_color([MAROON_A])

        eta11 = MathTex(r"\eta_{00}")
        eta22 = MathTex(r"\eta_{11}")
        eta33 = MathTex(r"\eta_{22}")
        eta44 = MathTex(r"\eta_{33}")

        etas = VGroup(eta11, eta22, eta33, eta44).move_to([0, 0, 0])

        yellowsq = RoundedRectangle(height = 0.7, width = 0.7, fill_color = TEAL_B, fill_opacity = 0.3, corner_radius=0.1)
        tealsq = Square(1, color = TEAL_B, fill_opacity = 0.3)

        self.wait(3)

        self.play(Write(sdef[0]), run_time = 1)

        self.wait(4)

        self.play(DrawBorderThenFill(etas[0].set_color([TEAL_B])), FadeIn(yellowsq.move_to([2.35, 2.9, 0])), run_time = 2)

        self.wait()

        self.play(Write(sdef[1]), Write(sdef[2]), Write(sdef[3]), run_time = 2)

        self.wait(2)

        self.play(Transform(etas[0], etas[1].set_color([TEAL_B])), yellowsq.animate.move_to([3.25, 2.35, 0]), run_time = 2)
        self.wait()

        self.play(Write(sdef[4]), Write(sdef[5]), run_time = 2)

        self.wait()

        self.play(Transform(etas[0], etas[2].set_color([TEAL_B])), yellowsq.animate.move_to([4, 1.75, 0]), run_time = 2)
        self.wait()

        self.play(Write(sdef[6]), Write(sdef[7]), run_time = 2)

        self.wait()

        self.play(Transform(etas[0], etas[3].set_color([TEAL_B])), yellowsq.animate.move_to([4.8, 1.15, 0]), run_time =2)
        self.wait()

        self.play(Write(sdef[8]), run_time = 2)

        self.wait(3)

        self.play(Unwrite(etas[0]), run_time = 1)

        sdef2 = MathTex(r" (\Delta s)^2 =  ", r" -", r"\Delta ct \Delta ct ", r"+", r"\Delta x \Delta x ", r"+", r"\Delta y \Delta y", r"+", r"\Delta z \Delta z").move_to([0, -2, 0])

        sdef2[1].set_color([TEAL_B])
        sdef2[2].set_color([MAROON_B])
        sdef2[4].set_color([MAROON_B])
        sdef2[6].set_color([MAROON_B])
        sdef2[8].set_color([MAROON_B])

        sdef3 = MathTex(r" (\Delta s)^2 =  ", r" -", r"(c\Delta t)^2 ", r"+", r"(\Delta x)^2", r"+", r"(\Delta y)^2", r"+", r"(\Delta z)^2").move_to([0, -2, 0])

        self.wait(2)

        self.play(Transform(sdef, sdef2), run_time = 1)
        self.wait(3)
        self.play(Transform(sdef, sdef3), run_time = 1)

        self.wait(4)

        self.play(Unwrite(VGroup(sdef, metric, yellowsq)), run_time = 4)

        self.wait()

        self.play(snewf.animate.move_to([0, 1, 0]), run_time = 2)

        self.wait(2)

        notation = Tex(r" Einstein Summation Notation ").move_to([0, -1, 0]).set_color([TEAL_B, MAROON_A]).scale(1.5)

        self.play(DrawBorderThenFill(notation), run_time = 1)

        self.wait(4)

        self.play(Unwrite(snewf), Unwrite(notation), run_time = 1)

        self.wait()


class ProperLength(ThreeDScene):
    def construct(self): 

        self.set_camera_orientation(
            phi = 65*DEGREES,
            theta = 32*DEGREES, 
            distance = 5
        )   
        
        axes = ThreeDAxes(
            x_range = (-5, 5, 5), 
            y_range = (-5, 5, 5), 
            z_range = (0, 5, 5), 
            x_length = 7, 
            y_length = 7, 
            z_length = 3.5,
            axis_config={'tip_shape': StealthTip}
        )
        labels = axes.get_axis_labels(
                    Tex(r"SPACE").scale(0.7), Tex(r"SPACE").scale(0.7), Tex(r"$t$")
                )
        
        arr1 = Arrow3D(
            start = np.array([-2.5, -2.5, 0]),
            end = np.array([2, -1.5, 0.5]),
            resolution = 5, 
            color = WHITE, 
        )
        
        arr2 = Arrow3D(
            start = np.array([2.5, 2.5, 0]),
            end = np.array([-2, 1.5, 0.5]),
            resolution = 5, 
            color = WHITE, 
        )


        arr3 = Arrow3D(
            start = np.array([2, -1.5, 0.5]),
            end = np.array([-1, 0.5, 1]),
            resolution = 5, 
            color = WHITE, 
        )
        
        arr4 = Arrow3D(
            start = np.array([-2, 1.5, 0.5]),
            end = np.array([1, -0.5, 1]),
            resolution = 5, 
            color = WHITE, 
        ) 

        arr5 = Arrow3D(
            start = np.array([-1, 0.5, 1]),
            end = np.array([0, 0, 1.5]),
            resolution = 5, 
            color = WHITE, 
        ).set_color_by_gradient(TEAL_B, PINK, YELLOW)

        arr6 = Arrow3D(
            start = np.array([1, -0.5, 1]),
            end = np.array([0, 0, 1.5]),
            resolution = 5, 
            color = WHITE, 
        ).set_color([YELLOW, PINK, TEAL_B])

        self.begin_ambient_camera_rotation(rate = 0.1)

        self.play(Write(VGroup(axes, labels)), run_time = 2)

        self.wait()

        self.play(Write(arr1), run_time = 1)
        self.wait()

        self.play(Write(arr3), run_time = 2)
        self.wait()

        self.play(Write(arr5), run_time = 3)

        self.wait(3)

        self.play(Write(arr2), run_time = 1)
        self.wait()

        self.play(Write(arr4), run_time = 2)
        self.wait()

        self.play(Write(arr6), run_time = 3)
        self.wait(5) 


        v1 = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([1, 1, 1]),
            resolution = 5, 
            color = WHITE, 
        )

        v2 = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([-1, -1, 3]),
            resolution = 5, 
            color = WHITE, 
        )
        
        v12 = Arrow3D(
            start = np.array([1, 1, 1]),
            end = np.array([-1, -1, 3]),
            resolution = 8, 
            color = WHITE, 
        ).set_color([TEAL_B, PINK, YELLOW])

        self.play(ReplacementTransform(VGroup(arr1, arr2, arr3, arr4, arr5, arr6), VGroup(v1, v2)), run_time = 4)

        self.wait()

        self.play(Write(v12), run_time = 4)

        metrictensor = Tex(r" Metric Tensor ").set_color([TEAL_B, MAROON_A]).scale(1.5).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(metrictensor)
        self.remove(metrictensor)

        self.wait(3)

        self.play(DrawBorderThenFill(metrictensor), run_time = 2)

        self.wait(5)

        self.play(Unwrite(VGroup(v1, v2, v12, metrictensor, axes, labels)), run_time = 5)

        self.wait()

        self.stop_ambient_camera_rotation()

        
        



        


        
                    
        


        









        

    

         
        
     

