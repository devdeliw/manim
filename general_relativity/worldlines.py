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
        

        
        
     

