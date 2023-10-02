from manim import * 
import numpy as np
import math

class Complex_Intro(Scene):
    def construct(self):
        quote = Tex(r"`\textit{The words real and imaginary are picturesque relics of\
        an age when the nature of complex numbers was not properly understood}'").scale(0.7)
        author = Tex(r"H.S.M. Coxeter").scale(0.6).move_to([-5,-1,0])


        self.play(Write(quote))
        self.wait(2)
        self.play(DrawBorderThenFill(author))
        self.wait()
        self.play(FadeOut(quote, author), run_time = 1)

        
        quadratic = MathTex(r" ax^2 + bx + c = 0").move_to([0,1,0])
        equation = MathTex(r"x = \frac{-b \pm \sqrt{b^2- 4ac}}{2a}").move_to([0, -1, 0])

        self.play(Write(quadratic))
        self.wait(2)
        self.play(Write(equation))
        self.play(FadeOut(quadratic, equation), run_time = 3)

        equations = MathTex(r" x^2 + 1 = 0").move_to([0,1,0])
        equation2 = MathTex(r" x^2 = -1 ").move_to([0.65, 0.3, 0])
        x = MathTex(r" x  = \, ?").move_to([0,-1.3,0])

        self.play(Write(equations), run_time = 1)
        self.wait(2)
        self.play(Write(equation2), run_time = 1)
        self.wait()
        self.play(Create(x))
        self.wait()

        self.play(FadeOut(equations, equation2), run_time = 2)
        self.play(Uncreate(x))
        self.wait()

        i = Tex(r"$i$")
        imaginary = Tex(r"maginary").move_to([1.1, -0.05, 0])
        self.play(DrawBorderThenFill(i), run_time = 3)
        self.wait()
        self.play( DrawBorderThenFill(imaginary), run_time = 2)
        self.wait()
        self.play(FadeOut(i), FadeOut(imaginary))

        i_equation = MathTex(r"i = \sqrt{-1}").move_to([0,2,0]).set_color([TEAL_B, PINK, YELLOW])
        i_IMequations = MathTex(r"\sqrt{-16} &= 4i \\  \sqrt{-3} &= i\sqrt{3} \\ i^3 &= -i").move_to([0,0,0])
        i_Requations = MathTex(r"i^2 &= -1 \\ \sqrt{-2}\sqrt{-8} = i\sqrt{2} \cdot i\sqrt{8} &= -4 \\ i^{4n} &= 1").move_to([0,0,0])

        self.play(Write(i_equation))
        self.wait(2)
        self.play(Write(i_IMequations))
        self.wait(4)
        self.play(FadeOut(i_IMequations))
        self.play(Write(i_Requations))
        self.wait(4)
        self.play(FadeOut(i_Requations, i_equation), run_time = 3)


class Complex_Plane(VectorScene):
    def construct(self):

        reim = MathTex(r"z = ",r"\alpha", "+", r"\beta", "i").move_to([0,0,0])
        real = MathTex(r"\alpha, \beta \in \mathbb{R}").move_to([0, -1,0])

        reim[1].set_color(TEAL_B)
        reim[3].set_color(MAROON_A)

        self.play(Write(reim), run_time = 2)
        self.play(Write(real))
        self.wait(1)

        real_imaginary = Tex("z = ","Real ", "+ ", "Imaginary ", r"i").move_to([0,0,0])
        
        real_imaginary[1].set_color(TEAL_B)
        real_imaginary[3].set_color(MAROON_A)

        self.wait()

        self.play(ReplacementTransform(reim, real_imaginary),
                  ReplacementTransform(real, real_imaginary),
                  run_time = 2
        ) 
        
        self.wait(6)
        
        number = MathTex(r"z =", "2", "+", "3", "i")

        number[1].set_color(TEAL_B)
        number[3].set_color(MAROON_A)

        coord = MathTex(r"(", "2", r", \;", " 3", ")").move_to([-0.2,-1,0])
        coord[1].set_color(TEAL_B)
        coord[3].set_color(MAROON_A)

        self.play(Transform(real_imaginary, number), run_time = 2)
        self.wait(5) 
        self.play(Write(coord), run_time = 1)
        self.wait(3)
        self.play(FadeOut(real_imaginary, coord))

        ax = Axes( 
            x_range = (-7, 7, 7), 
            y_range = (-7, 7, 7),
            x_length = 7, 
            y_length = 7
        )

        self.play(DrawBorderThenFill(ax))
        
        labels = ax.get_axis_labels(
            Tex("x").scale(0.65), Text("y").scale(0.65)
        )

        labels2 = ax.get_axis_labels(Tex(r"real axis").scale(0.65).set_color([TEAL_B, PINK, YELLOW]),
                                     Tex(r"imaginary axis").scale(0.65).set_color([TEAL_B, PINK, YELLOW])
        )

        self.play(DrawBorderThenFill(labels), run_time = 2)
        self.wait()
        
        vector = Vector([2,3], color = RED_A)

        self.play( DrawBorderThenFill(vector), run_time = 2)
        self.vector_to_coords(vector)

        vec2 = Vector([5, -2], color = TEAL_A)
        vec3 = Vector([-4, 1], color = GREEN_A)
        vec4 = Vector([-2,-3]).set_color([TEAL_B, PINK, YELLOW])
        self.play( ReplacementTransform(vector, vec2), run_time = 1.5)
        self.play( ReplacementTransform(vec2, vec3), run_time = 1.5)
        self.play( ReplacementTransform(vec3, vec4), run_time = 1.5)

        self.play(FadeOut(vec4), run_time = 3)

        self.play(Transform(labels, labels2))
        self.wait(2)
        self.play(FadeOut(ax, labels))


class Polar_Plane(Scene):
    def construct(self):
        
        vector = Vector([3,3], color = MAROON_A)

        plane = NumberPlane()
        theta = MathTex(r"\theta").move_to([1,0.4,0])
        mag = MathTex(r"r").move_to([1.2,1.7,0])

        self.play(Create(plane), run_time = 3)
        self.wait(1)
        self.play(Create(vector), Write(theta), Write(mag), run_time = 3)

        vec2 = Vector([-3,-1], color = RED_A)
        theta2 = MathTex(r"\theta").move_to([-2,-0.3,0])
        mag2 = MathTex(r"r").move_to([-1.4,-0.8,0])
        x = MathTex(r"-3").set_color(TEAL_B).move_to([-1.5, 0.5, 0])
        y = MathTex(r"-1").set_color(MAROON_B).move_to([-4, -0.5, 0])
        xline = Line([0,0,0], [-3,0,0], color = TEAL_B)
        yline = Line([-3,0,0], [-3,-1,0], color = MAROON_A)

        
        r2 = MathTex(r" |z| = \sqrt{ {{ (-3)^2 }} + {{ (-1)^2 }} } = \sqrt{10.}").to_edge(DR)
        sqrt = MathTex(r"\sqrt{10}").to_edge(DR)
        sqrt2 = MathTex(r"\sqrt{10}").to_edge(DR)
        sqrt3 = MathTex(r"\sqrt{10}").move_to([-1.4, -0.8, 0]).set_color(YELLOW)


        r2[1].set_color(TEAL_B)
        r2[3].set_color(MAROON_A)

        backgroundRectangle1 = BackgroundRectangle(r2, color=WHITE,
                                                   fill_opacity=0.1)

        self.play(ReplacementTransform(vector, vec2),
                  ReplacementTransform(theta, theta2),
                  ReplacementTransform(mag, mag2),
                  run_time = 3
        )
        self.wait()

        self.play(Create(xline), Create(yline), DrawBorderThenFill(x), DrawBorderThenFill(y), run_time = 2)
        self.wait()

        self.play(ReplacementTransform(mag2, r2),
                  DrawBorderThenFill(backgroundRectangle1), run_time = 2)
        self.play(ReplacementTransform(x, r2[1]), 
                  ReplacementTransform(y, r2[3]), 
                  run_time = 2
        )

        self.wait()

        mag2 = MathTex(r"r").move_to([-1.4, -0.8, 0])

        self.play(FadeIn(mag2))

        rcos = MathTex(r"{{r}}\cos\theta").move_to([-1.5, 0.5, 0])
        magcos = MathTex(r"{{{\sqrt{10}}}}\cos\theta").move_to([-1.5, 0.5, 0])
        rsin = MathTex(r"{{r}}\sin\theta").move_to([-4, -0.5, 0])
        magsin = MathTex(r"{{{\sqrt{10}}}}\sin\theta").move_to([-4, -0.5, 0])

        magcos[0].set_color(YELLOW)
        magsin[0].set_color(YELLOW)

        self.play(DrawBorderThenFill(rcos), run_time = 2)
        self.play(DrawBorderThenFill(rsin), run_time = 2)
        self.wait()
        self.play(Write(sqrt), Write(sqrt2), ReplacementTransform(sqrt, magcos[0]), 
                  ReplacementTransform(rcos, magcos),
                  ReplacementTransform(sqrt2, magsin[0]),
                  ReplacementTransform(rsin, magsin),
                  ReplacementTransform(mag2, sqrt3),
                  run_time = 2
        )
        self.wait()

        self.play(FadeOut(plane, vec2, r2, sqrt, sqrt2, sqrt3, theta2, xline, yline, rcos,
                          mag2, rsin, magcos, magsin, x, y,
                          backgroundRectangle1), run_time = 2)

        equation = MathTex(r"&x = r\cos\theta \\ &y = r\sin\theta").scale(0.8).move_to([-4,2,0])
        therefore = Tex(r"Therefore,").scale(0.7).move_to([-4.5,0, 0])
        final = MathTex(r" x + iy &= r\cos\theta + ir\sin\theta \\ &= {{r (\cos\theta + i\sin\theta) }} ").move_to([0,-2,0])
        euler = MathTex(r"re^{i\theta}").move_to([-0.22,-2.25,0])

        self.play(Write(equation), run_time = 1)
        self.wait(1)
        self.play(Write(therefore))
        self.wait(1)
        self.play(Write(final), run_time = 3)
        self.wait(2)

        euler.set_color(YELLOW)
        self.play(ReplacementTransform(final[1], euler), run_time = 2)
       
        self.play(FadeOut(final, euler, therefore, equation), run_time = 2)

        polarplane_pi = PolarPlane(
            azimuth_units="PI radians",
            size=6,
            azimuth_label_font_size=33.6,
            radius_config={"font_size": 33.6},
            radius_step = 1,
            radius_max = 3
        ).add_coordinates()

        self.play(Write(polarplane_pi), run_time = 2)

        vec = Vector([3*np.cos(PI/5), 3*np.sin(PI/5)], color = RED_B)
        linex = Line([0,0,0], [3*np.cos(PI/5),0,0], color = GOLD_B)
        liney = Line([3*np.cos(PI/5),0,0], [3*np.cos(PI/5), 3*np.sin(PI/5),0], color = MAROON_A)

        self.play(DrawBorderThenFill(vec), run_time = 3)

        self.wait(5)

        self.play(Create(linex), Write(liney), run_time = 2)

        self.wait(2)

        mag3 = MathTex(r"3").move_to([1.1, 1.1, 0]).scale(0.7)
        x = MathTex(r"2.43").move_to([1.7, -0.5, 0]).scale(0.7)
        y = MathTex(r"1.76").move_to([3.2, 0.8, 0]).scale(0.7)

        equation = MathTex(r" &3e^{i\left(\frac{\pi}{5}\right)} \\ &=3\left(\cos\frac{\pi}{5} + i\sin\frac{\pi}{5}\right) \\ &\approx 2.43 + 1.76i").scale(0.7).to_edge(UR)

        self.play( DrawBorderThenFill(mag3))
        self.wait()
        self.play(Write(equation), run_time = 4)
        self.wait(2)
        self.wait(2)
        self.play(FadeOut(equation, polarplane_pi, linex, liney, vec, mag3), run_time = 3)


class Calculus(Scene):
    def construct(self):
        title = Tex(r"Physical Applications").to_edge(UL)

        particle = MathTex(r" z = x + iy = \frac{i + 2t}{t - i}").move_to([0, 1, 0])

        question = Tex(r" Find the particle's velocity and acceleration as a function of $t$").move_to([0, -1, 0]).scale(0.7)
        

        self.play(Write(title), run_time = 2)
        self.wait(2)
        self.play(Write(particle), run_time = 3)
        self.wait(2)
        self.play(Write(question), run_time = 1)
        self.wait(2)
        self.play(FadeOut(question), run_time = 2)

        method1 = MathTex(r"z = {{x}} + i{{y}}").move_to([0, 0, 0])
        method1[1].set_color(TEAL_B)
        method1[3].set_color(MAROON_A)
        method11 = Tex(r"Method 1:").move_to([-4.5, 1, 0]).scale(0.7)

        func = MathTex(r" (x(t), \; y(t))").move_to([0, -1, 0])
        diff = MathTex(r" \Rightarrow \left( \frac{dx}{dt}, \;  \frac{dy}{dt} \right) ").move_to([0, -2, 0]).set_color(YELLOW)

        particle2 = MathTex(r" z = x + iy = \frac{i + 2t}{t - i}").move_to([0, 2, 0])
        func2 = MathTex(r" (x(t), \; y(t))").move_to([0, 0, 0])


        self.play(ReplacementTransform(particle, particle2))
        self.wait()
        self.play(Write(method11), run_time = 1)
        self.wait()
        self.play(Write(method1), run_time = 1)
        self.wait()
        self.play(Write(func), run_time = 1)
        self.wait(2)
        self.play(FadeOut(method1))
        self.play(ReplacementTransform(func, func2))
        self.play(Write(diff), run_time = 2)
        self.wait(2)
        self.play(FadeOut(func2, particle2, diff, method11), run_time = 2)


        curve = ParametricFunction(
            lambda t: np.array([(2*t**2 -1)/(t**2 + 1), 3*t, 0]),
            color = YELLOW,
            t_range = [-5, 5]
        )

        ax = Axes(
            x_range = (-15, 15, 15),
            y_range = (-15, 15, 15),
            x_length = 7.5,
            y_length = 7.5,
        )

        self.play(Write(ax), run_time = 2)
        self.wait()
        self.play(Create(curve), run_time = 6)
        self.wait(3)
        self.play(FadeOut(ax, curve), run_time = 2)

        self.play(Write(particle2))

        method22 = Tex(r"Method 2:").move_to([-4, 1.2, 0]).scale(0.7)
        define = Tex(r"Define").move_to([-4, 1, 0]).scale(0.7)

        diffz = MathTex(r" \frac{dz}{dt} = \frac{dx}{dt} + i\frac{dy}{dt}").move_to([0, -1, 0])
        diff2z = MathTex(r" \frac{d^2 z}{dt^2} = \frac{d^2 x}{dt^2} + i \frac{d^2 y}{dt^2}").move_to([0, -2.5, 0])
        
        self.play(Write(define))
        self.wait()
        self.play(Write(diffz), Write(diff2z), run_time = 3)
        self.wait(5)
        self.play(FadeOut(define, diffz, diff2z), run_time = 2)
        self.wait(2)

        magv = MathTex(r" |\vec{v}| = \sqrt{ \left( \frac{dx}{dt} \right)^2 + \left(\frac{dy}{dt}\right)^2} = \Big|\frac{dz}{dt}\Big|").move_to([0, 0, 0])

        maga = MathTex(r" |\vec{a}| = \Big|\frac{d^2z}{dt^2}\Big|").move_to([-2.4, -2, 0])

        self.play(Write(method22))
        self.wait()
        self.play(Write(magv), run_time = 2)
        self.wait()
        self.play( DrawBorderThenFill(maga), run_time = 2)
        self.wait()

        self.play( FadeOut(maga, magv, method22), run_time = 1)

        deriv = MathTex(r" \frac{dz}{dt} &= \frac{2(t-i) - (i+2t)}{(t-i)^2} = \frac{-3i}{(t-i)^2} \\ v &= \Big|\frac{dz}{dt}\Big| = \sqrt{\frac{-3i}{(t-i)^2} \cdot \frac{+3i}{(t+i)^2}} = {{\frac{3}{t^2 + 1}}} \\ \frac{d^2 z}{dt^2} &= \frac{(-3i)(-2)}{(t-i)^3} = \frac{6i}{(t-i)^3}, \\ a &= \Big|\frac{d^2z}{dt^2}\Big| = {{\frac{6}{(t^2+1)^{3/2}}}}").scale(0.7).move_to([0, -1, 0])

        deriv[1].set_color(TEAL_B)
        deriv[3].set_color(MAROON_A)

        self.play(Write(deriv), run_time = 8)
        self.wait(3)
        self.play(FadeOut(particle2), run_time = 3)

        deriv2 = MathTex(r" \frac{dz}{dt} &= \frac{2(t-i) - (i+2t)}{(t-i)^2} = \frac{-3i}{(t-i)^2} \\ v &= \Big|\frac{dz}{dt}\Big| = \sqrt{\frac{-3i}{(t-i)^2} \cdot \frac{+3i}{(t+i)^2}} = {{\frac{3}{t^2 + 1}}} \\ \frac{d^2 z}{dt^2} &= \frac{(-3i)(-2)}{(t-i)^3} = \frac{6i}{(t-i)^3}, \\ a &= \Big|\frac{d^2z}{dt^2}\Big| = {{\frac{6}{(t^2+1)^{3/2}}}}").scale(0.7).to_edge(UR)

        deriv2[1].set_color([TEAL_B, PINK, YELLOW])
        deriv2[3].set_color(MAROON_A)

        line1 = Line([-0.5,-1,0], [-0.5,5,0])
        line2 = Line([-0.5,-1,0], [8,-1,0])

        self.play(Transform(deriv, deriv2), FadeOut(title), run_time = 2)
        self.play( DrawBorderThenFill(line1), DrawBorderThenFill(line2), run_time = 1)
        self.wait()

        deriv3 = MathTex(r" z &= \frac{i + 2t}{t - i} \\ &= \frac{i + 2t}{t - i}\left(\frac{t+i}{t+i}\right) = \frac{2t^2 + 3ti - 1}{t^2 + 1} \\ &= \frac{2t^2 - 1}{t^2 + 1} + \frac{3t}{t^2 + 1}i").scale(0.7).to_edge(UL)

        derivdiff = MathTex(r" \frac{dx}{dt} &= \frac{d}{dt} \left(\frac{2t^2 - 1}{t^2 + 1}\right) \\ \frac{dy}{dt} &= \frac{d}{dt} \left(\frac{3t}{t^2+1}\right)").scale(0.7).move_to([-5, -0.3, 0])

        derivdiff2 = MathTex(r" \left(\frac{dx}{dt}, \; \frac{dy}{dt}\right) &= \left(\frac{6t}{(t^2 +1)^2}, \; \frac{-3t^2 + 3}{(t^2 + 1)^2}\right) \\ |\vec{v}| &= \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} = {{\frac{3}{t^2 + 1}}}").scale(0.7).to_edge(DL)

        derivdiff2[1].set_color([TEAL_B, PINK, YELLOW])

        self.play(Write(deriv3), run_time = 3)
        self.play(Write(derivdiff), run_time = 3)
        self.play(Write(derivdiff2), run_time = 3)
        self.wait(3)


        self.play(FadeOut(deriv3, derivdiff, derivdiff2, deriv, line1, line2), run_time = 3)



    



        
        












        



