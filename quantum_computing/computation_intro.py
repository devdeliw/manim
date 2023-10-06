from manim import * 
import numpy as np
import math 

class Intro(Scene):
    def construct(self):
        ax = Axes( 
            x_range = (-5, 5), 
            y_range = (-5, 5),
            x_length = 5, 
            y_length = 5
        )


        ccircuit = Tex("Classical Circuit").move_to([-3, 1.5, 0]).set_color([TEAL_B, MAROON_A])
        cgates = Tex("Logic Gates").move_to([-3, 0, 0]).set_color([TEAL_B, MAROON_A])
        cwires = Tex("Wires").move_to([-3, -1, 0]).set_color([TEAL_B, MAROON_A])

        qcircuit = Tex("Quantum Circuit").set_color([PINK, YELLOW]).move_to([3, 1.5, 0])
        qgates = Tex("Quantum Gates").move_to([3, 0, 0]).set_color([PINK, YELLOW])
        qwires = Tex("Waveguides").move_to([3, -1, 0]).set_color([PINK, YELLOW])
        
        tablev = Line([0, -2, 0], [0, 2, 0]).set_color([PINK, YELLOW, TEAL_B, MAROON_A])
        tableh = Line([-5, 1, 0], [5, 1, 0]).set_color([PINK, YELLOW, TEAL_B, MAROON_A])

        self.play(FadeIn(tablev), FadeIn(tableh), run_time = 2)
        self.wait()
        self.play(Write(ccircuit), Write(qcircuit), run_time = 1)
        self.wait(4)
        self.play(Write(cgates), 
                  Write(cwires),
                  Write(qgates),
                  Write(qwires),
                  run_time = 2
        )
        self.wait(2.5)
        self.remove(ccircuit, 
                    cgates,
                    cwires,
                    qcircuit,
                    qgates, 
                     qwires, 
                     tablev, 
                     tableh
                    )

        logic_gates = Tex("Single Bit Logic Gates").to_edge(UL)
        NOT = Tex("NOT").to_edge(UR)

        operation = MathTex(r" 0 &\longrightarrow 1 \\ 1 &\longrightarrow 0").move_to([0, 0, 0])

        self.play(Write(logic_gates))
        self.wait(1)
        self.play(Write(NOT))
        self.wait()
        self.play(Write(operation))

        analog = Tex(r"can an analogous quantum \textit{NOT} gate for qubits be defined?").scale(0.7).move_to([0, -2, 0])
        self.wait(3)
        self.play(Write(analog))
        self.wait(2)
        self.play(FadeOut(operation, analog))

        qoperation = MathTex(r" |0\rangle &\longrightarrow |1\rangle \\ |1\rangle &\longrightarrow |0\rangle").move_to([0, 1, 0])

        logic_gates_q = Tex("Single Qubit Quantum Gates").to_edge(UL)
        QNOT = Tex("QNOT").to_edge(UR)
        
        self.play(Transform(logic_gates, logic_gates_q), Transform(NOT, QNOT))
        self.wait(2)
        self.play(Write(qoperation))
        self.wait(2)

        superpos = MathTex(r" &|\psi\rangle = \alpha {{|0\rangle}} + \beta {{|1\rangle}} \\ &|\psi\rangle = \alpha{{|1\rangle}} + \beta{{|0\rangle}}").move_to([0, -1.2, 0])
        linear = Tex(r"\textit{linear}").set_color([MAROON_A, TEAL_B]).move_to([0, -3, 0])
        
        superpos[1].set_color([TEAL_B])
        superpos[3].set_color([MAROON_A])
        superpos[5].set_color([MAROON_A])
        superpos[7].set_color([TEAL_B])

        self.play(Write(superpos), run_time = 2)
        self.wait(4)
        self.play(Write(linear))
        self.wait(5)
        self.play(FadeOut(qoperation, 
                          NOT, 
                          linear, 
                          superpos, 
                          logic_gates
                )
        )


class QNOT(Scene):
    def construct(self):
        
        title = Tex("Defining QNOT").to_edge(UL)

        X = MathTex(r" X \equiv \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}").move_to([0, 2, 0])
        X2 = MathTex(r" X \equiv {{ \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} }}").move_to([0, 2, 0])
        X2[1].set_color([TEAL_B, MAROON_A])

        VN = Tex(r"Vector Notation").move_to([-4, 0.5, 0]).scale(0.7)

        superpos = MathTex(r"|\psi\rangle = \alpha|0\rangle + \beta|1\rangle \equiv {{ \begin{bmatrix} \alpha \\ \beta \end{bmatrix} }} ").move_to([0, -0.5, 0])

        superpos[1].set_color([PINK, YELLOW])

        QNOT = MathTex(r"X \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} \beta \\ \alpha \end{bmatrix}").move_to([0, -2.5, 0])
        QNOT2 = MathTex(r"{{ \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} }} \begin{bmatrix} \alpha \\ \beta \end{bmatrix} = \begin{bmatrix} \beta \\ \alpha \end{bmatrix}").move_to([0, -2.5, 0])

        QNOTt = Tex("QNOT:").move_to([-3, -2.5, 0]).scale(0.7)

        QNOT2[0].set_color([TEAL_B, MAROON_A])

        self.play(Write(title))
        self.wait(1)
        self.play(Write(X))
        self.wait(4)
        self.play(Write(VN))
        self.play(Write(superpos), run_time = 3)
        self.wait(3)

        self.play(Write(QNOT), run_time = 3)
        self.wait()
        self.play(Transform(QNOT, QNOT2), Transform(X, X2), Write(QNOTt), run_time = 2)
        self.wait(4)

        self.play(FadeOut(title,
                          X, 
                          VN, 
                          superpos, 
                          QNOT,
                          QNOTt
                        ), run_time = 2
        )

class Unitary(Scene):
    def construct(self):
        
        twoxtwo = MathTex(r" \begin{bmatrix} a & b \\ c & d \end{bmatrix} ").move_to([0, 0, 0])

        constraints = Tex(r" are there any constraints on what $2$x$2$ matrices may be used as quantum gates? ").scale(0.7).move_to([0, -2, 0])

        self.play( DrawBorderThenFill(twoxtwo), run_time = 2)
        self.wait(3)
        self.play(Write(constraints))
        self.wait(2)

        self.play(FadeOut(twoxtwo, constraints), run_time = 2) 

        normalization = Tex(r" Recall the normalization condition:").to_edge(UL)

        normal = MathTex(r" |\alpha|^2 + |\beta|^2 = 1 ").set_color([YELLOW])

        final = Tex(r" The resultant transformed $|\psi'\rangle$ with coefficients $\alpha'$ and $\beta'$ where $|\psi'\rangle = \alpha'|0\rangle + \beta'|1\rangle$ must also satisfy the normalization condition").move_to([0, -2, 0]).scale(0.7)

        normal2 = MathTex(r" |\alpha|^2 + |\beta|^2 = 1 ").set_color([YELLOW]).move_to([0, 2, 0])

        unitary = Tex("unitary", " matrix")
        unitary[0].set_color([TEAL_B, PINK, YELLOW])

        U = MathTex(r"U:").move_to([-2, 0.05, 0]).set_color([TEAL_B, PINK, YELLOW])

        Udef = MathTex(r" U^\dagger U = I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}").move_to([2, 0, 0])
 
        where = Tex(r" where $U^\dagger$ is the \textit{adjoint} of $U$, obtained by transposing and complex conjugating $U$").move_to([0, -2, 0]).scale(0.7)

        self.play(Write(normalization), run_time = 2) 
        self.wait()
        self.play( DrawBorderThenFill(normal))
        self.wait()

        self.play(Write(final), run_time = 4)
        self.wait(4)
        self.play(FadeOut(normalization, final), Transform(normal, normal2))
        self.wait(2)

        self.play(Write(unitary))
        self.wait(2)
        self.play(Transform(unitary, U))
        self.wait(2)
        self.play(Write(Udef))
        self.wait(4)
        self.play(Write(where, run_time = 2))
        self.wait(3)

        self.play(FadeOut(normal, 
                          unitary,
                          Udef,
                          where
                ), run_time = 2
        )

class Gates(ThreeDScene):
    def construct(self): 
        
        Z = MathTex(r"Z", r"\equiv \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}").move_to([0, 1, 0])
        H = MathTex(r"H", r"\equiv \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}").move_to([0, -1, 0])
        Z[0].set_color([TEAL_B])
        H[0].set_color([MAROON_A])

        H2 = MathTex(r"H", r"\equiv \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}").move_to([0, 1.5, 0])
        H2[0].set_color([TEAL_B, PINK, YELLOW])

        operation = MathTex(r" &|0\rangle \longmapsto \frac{|0\rangle + |1\rangle}{\sqrt{2}} \\ &|1\rangle \longmapsto \frac{|0\rangle - |1\rangle}{\sqrt{2}}").move_to([0, -1.5, 0])

        self.play(Write(Z), Write(H))
        self.wait(5)
        self.play(FadeOut(Z), Transform(H, H2))
        self.wait(3)

        self.play(Write(operation), run_time = 2)
        self.wait(3)

        self.play(FadeOut(H, operation), run_time = 2)
        self.wait(2)

        self.set_camera_orientation(
            phi = 70*DEGREES,
            theta = 20*DEGREES, 
            distance = 4
        )

        title = Tex("Hadamard").to_edge(UR)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time = 2)

        bloch = Surface(
            lambda u, v: np.array([
            3 * np.cos(u) * np.cos(v),
            3 * np.cos(u) * np.sin(v),
            3 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[GRAY, GRAY], resolution=(32, 64), fill_opacity = 0.01
        ).set_color([TEAL_B, PINK, YELLOW])

        axes = ThreeDAxes(
            x_range = (-8, 8, 8), 
            y_range = (-8, 8, 8), 
            z_range = (-7, 7, 7), 
            x_length = 8, 
            y_length = 8, 
            z_length = 7
        )

        labels = axes.get_axis_labels(
            MathTex(r"x"), MathTex(r"y"), MathTex(r"z")
        )

        self.play(Write(axes), DrawBorderThenFill(labels))

        in_vec = MathTex(r" |+\rangle \equiv \frac{|0\rangle + |1\rangle}{\sqrt{2}} ").move_to([-9, -9, -9]).scale(0.7).set_color([TEAL_B])

        half_vec = MathTex(r" |1\rangle ").scale(0.7).move_to([-8, -8, -8]).set_color([MAROON_A])
        final_vec = MathTex(r" |0\rangle ").scale(0.7).move_to([-8, -8, -8]).set_color([YELLOW])

        zeroone = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([3, 0, 0]),
            resolution = 8,
            color = TEAL_B
        )

        one = MathTex(r"|1\rangle").move_to([1, 0, -3.5]).scale(0.7)
        zero = MathTex(r"|0\rangle").move_to([1, 0, 3.5]).scale(0.7)

        self.add_fixed_orientation_mobjects(one, zero)

        final = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([0, 0, 3]),
            resolution = 8, 
            color = YELLOW
        )
        
        H = Tex("Hadamard").to_edge(UR)

        self.wait(2)
        self.play(Create(bloch), run_time = 6)
        self.play(Create(zeroone))
        self.add_fixed_in_frame_mobjects(in_vec, half_vec, final_vec)
        self.play(Write(in_vec))

        self.add_fixed_orientation_mobjects(one, zero)
        self.wait(5)

        self.play(Rotate(
                    bloch, 
                    angle = 0.5*PI,
                    axis = np.array([0,1,0])
                ), Rotate(
                    zeroone,
                    angle = 0.5*PI, 
                    axis = np.array([0,1,0]),
                    about_point = ORIGIN),
                  Transform(in_vec, half_vec),
                run_time = 5
        )

        self.wait(4)

        self.play(Rotate(
                    bloch,
                    angle = PI,
                    axis = np.array([1,0,0])
                ), Rotate(
                    zeroone, 
                    angle = PI,
                    axis = np.array([1,0,0]), 
                    about_point = ORIGIN), 
                    Transform(in_vec, final_vec), 
                run_time = 5
        )

        self.play(Transform(zeroone, final))

        self.wait(4)
        self.play(FadeOut(bloch, labels, one, zero, in_vec, zeroone, title,
                          axes), run_time = 3)


class LogicGates(Scene):
    def construct(self):
        
        ax = Axes( 
            x_range = (-10, 10, 1), 
            y_range = (-10, 10, 1),
            x_length = 10, 
            y_length = 10
        )


        x = MathTex(r"x").move_to([-5, 0, 0])
        xbar = MathTex(r"\bar{x}").move_to([-2.8, 0, 0])

        ltriangle = Line(start =  [-4.7, 0, 0], end = [-4.4, 0, 0]).set_color([TEAL_B, MAROON_A])
        vtriangle = Line(start =  [-4.4, -0.7, 0], end = [-4.4, 0.7, 0])
        tdiag = Line(start =  [-4.4, 0.7, 0], end = [-3.5, 0, 0])
        bdiag = Line(start =  [-4.4, -0.7, 0], end = [-3.5, 0, 0])
        circ = Circle(radius = 0.1, color = WHITE).move_to([-3.4, 0, 0])
        rtriangle = Line(start =  [-3.3, 0, 0], end = [-3, 0, 0]).set_color([MAROON_A, TEAL_B])
        
        vline = Line(start =  [-2, -2, 0], end = [-2, 2, 0]).set_color([TEAL_B, MAROON_A])
        xl = MathTex(r" \alpha |0\rangle + \beta |1\rangle").move_to([0, 1.5, 0])
        xlinel = Line(start =  [1.5, 1.5, 0], end = [2, 1.5, 0])
        xvl = Line(start =  [2, 1.875, 0], end = [2, 1.125, 0])
        xtl = Line(start =  [2, 1.875, 0], end = [2.75, 1.875, 0])
        xbl = Line(start =  [2, 1.125, 0], end = [2.75, 1.125, 0])
        xvr = Line(start =  [2.75, 1.125, 0], end = [2.75, 1.875, 0])

        xsq = Square(side_length = 0.75).move_to([2.375, 1.5, 0]).set_color([TEAL_B])

        xliner = Line(start =  [2.75, 1.5, 0], end = [3.25, 1.5, 0])
        X = MathTex(r"X").move_to([2.375, 1.5, 0]).scale(0.9)
        xr = MathTex(r" \beta |0\rangle + \alpha |1\rangle").move_to([4.75, 1.5, 0])

        zl = MathTex(r" \alpha |0\rangle + \beta |1\rangle").move_to([0, 0, 0])
        zlinel = Line(start =  [1.5, 0, 0], end = [2, 0, 0])
        zvl = Line(start =  [2, 0.375, 0], end = [2, -0.375, 0])
        ztl = Line(start =  [2, 0.375, 0], end = [2.75, 0.375, 0])
        zbl = Line(start =  [2, -0.375, 0], end = [2.75, -0.375, 0])
        zvr = Line(start =  [2.75, -0.375, 0], end = [2.75, 0.375, 0])
        zliner = Line(start =  [2.75, 0, 0], end = [3.25, 0, 0])
        Z = MathTex(r"Z").move_to([2.375, 0, 0]).scale(0.9)
        zr = MathTex(r" \alpha |0\rangle - \beta |1\rangle").move_to([4.75, 0, 0])

        zsq = Square(side_length = 0.75).move_to([2.375, 0, 0]).set_color([MAROON_A])

        hl = MathTex(r" \alpha |0\rangle + \beta |1\rangle").move_to([0, -1.5, 0])
        hlinel = Line(start =  [1.5, -1.5, 0], end = [2, -1.5, 0])
        hvl = Line(start =  [2, -1.125, 0], end = [2, -1.875, 0])
        htl = Line(start =  [2, -1.125, 0], end = [2.75, -1.125, 0])
        hbl = Line(start =  [2, -1.875, 0], end = [2.75, -1.875, 0])
        hvr = Line(start =  [2.75, -1.875, 0], end = [2.75, -1.125, 0])
        hliner = Line(start =  [2.75, -1.5, 0], end = [3.25, -1.5, 0])
        H = MathTex(r"H").move_to([2.375, -1.5, 0]).scale(0.9)
        hr = MathTex(r" \alpha \frac{|0\rangle + |1\rangle}{\sqrt{2}}\
                     + \beta\frac{|0\rangle - |1\rangle}{\sqrt{2}").move_to([5.35, -1.5, 0]).scale(0.7)

        hsq = Square(side_length = 0.75).move_to([2.375, -1.5, 0]).set_color([TEAL_B, PINK, YELLOW])

        group = VGroup(x, xbar, ltriangle, vtriangle, tdiag, bdiag, circ, rtriangle, vline, 
                       xl, xlinel, xsq, xliner, X, xr, 
                       zl, zlinel, zsq, zliner, Z, zr,
                       hl, hlinel, hsq, hliner, H, hr
                ).shift(1 * LEFT)

        group1 = VGroup(xl, xlinel, xvl, xtl, xbl, xvr, xliner, X, xr).set_color([TEAL_B])
        group2 = VGroup(zl, zlinel, zvl, ztl, zbl, zvr, zliner, Z, zr).set_color([MAROON_A])
        group3 = VGroup(hl, hlinel, hvl, htl, hbl, hvr, hliner, H, hr).set_color([TEAL_B, PINK, YELLOW])

        self.play(Write(group), run_time = 8)
        self.wait(5)
        self.play(FadeOut(group), run_time = 3)
                
            
class Rotation(Scene):
    def construct(self): 

        title = Tex(r"Rotation Matrices").to_edge(UL)

        rotation_matrix = MathTex(r"U", r" = e^{i\alpha}", r"\begin{bmatrix} e^{-i\beta/2}\
        & 0 \\[2mm] 0 & e^{i\beta/2} \end{bmatrix}", r"\begin{bmatrix} \cos \frac{\gamma}{2}\
        & -\sin \frac{\gamma}{2} \\[2mm] \sin \frac{\gamma}{2} & \cos\
        \frac{\gamma}{2} \end{bmatrix}").move_to([0, -1.5, 0]).set_color([TEAL_B, MAROON_A])

        rotation_matrix[0].set_color([TEAL_B, PINK, YELLOW])

        rotating = Surface(
            lambda u, v: np.array([
            1 * np.cos(u) * np.cos(v),
            1 * np.cos(u) * np.sin(v),
            1 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[TEAL_B, MAROON_A], resolution=(4, 8),
            fill_opacity = 0.01
            ).move_to([0, 1.75, 0]).set_color([TEAL_B, MAROON_A])

        fine = Line(start =  [0, 1.75, -1.5], end = [0, 1.75, 1.5]).set_color([TEAL_B, MAROON_A])

        z = Brace(rotation_matrix[2], fill_opacity = 0.8,
                  background_stroke_color = TEAL_B
            ).set_color([TEAL_B, MAROON_A])

        xy = Brace(rotation_matrix[3], fill_opacity = 0.8,
                  background_stroke_color = MAROON_A
             ).set_color([MAROON_A, TEAL_B])

        Z = Tex(r" about $z$").move_to([-1, -3, 0]).scale(0.7)
        XY = Tex(r" about $xy$").move_to([2.9, -3, 0]).scale(0.7)

        self.play(Write(rotating), Write(fine), run_time = 3)

        self.play(Rotate(rotating, angle = PI, axis = np.array([1,1,1])),
                  Rotate(fine, angle = PI, axis = np.array([1,1,1])),
                  Write(rotation_matrix),
                  run_time = 3.5
        )

        self.play(Rotate(rotating, angle = PI, axis = np.array([-1,0,0])), 
                  Rotate(fine, angle = PI, axis = np.array([-1,0,0])),
                  run_time = 3.5
        )

        self.play(Rotate(rotating, angle = PI, axis = np.array([-1,1,1])), 
                  Rotate(fine, angle = PI, axis = np.array([-1,1,1])),
                  run_time = 3.5
        )

        self.play(Rotate(rotating, angle = PI, axis = np.array([0,1,-1])),
                  Rotate(fine, angle = PI, axis = np.array([0,1,-1])),
                  DrawBorderThenFill(z), DrawBorderThenFill(xy), Write(XY),
                  Write(Z),
                  run_time = 3.5
        )

        self.play(Rotate(rotating, angle = PI, axis = np.array([1,0,0])),
                  Rotate(fine, angle = PI, axis = np.array([1,0,0])),
                  run_time = 3.5
        )

        self.play(Rotate(rotating, angle = PI, axis = np.array([1,-1,-1])), 
                  Rotate(fine, angle = PI, axis = np.array([1,-1,-1])), 
                  FadeOut(rotating, fine, rotation_matrix, z, xy, XY, Z),
                  run_time = 3.5
        )


class MQubits(Scene):
    def construct(self):
        title = Tex(r"Multiple Qubits").to_edge(UL)

        gates = Tex(r" AND, OR, XOR, NAND, NOR ").scale(0.7)

        nand = Tex("NAND").set_color([TEAL_B, PINK, YELLOW])

        self.play(Write(title))

        self.wait()

        self.play(DrawBorderThenFill(gates))

        self.wait(7)
        
        self.play(ReplacementTransform(gates, nand), run_time = 2)
        self.wait(2)
        self.play(FadeOut(nand), run_time = 3)

        conot = Tex(r" \textit{controlled}-NOT")
        cnot = Tex(r"CNOT")

        gate = Tex("CNOT").to_edge(UR)

        ax = Axes( 
            x_range = (-5, 5), 
            y_range = (-5, 5),
            x_length = 5, 
            y_length = 5
        )
        
        Al = MathTex(r"|A\rangle").move_to([-1.5, 1.8, 0])
        tline = Line(start =  [-1, 1.8, 0], end = [1, 1.8, 0]).set_color([TEAL_B, MAROON_A])
        Ar = MathTex(r"|A\rangle").move_to([1.5, 1.8, 0])
        Adot = Dot(point = [0, 1.8, 0], radius = 0.08)

        vline = Line(start =  [0, 1.8, 0], end = [0, 0.8, 0]).set_color([TEAL_B, MAROON_A, TEAL_B])

        Bl = MathTex(r"|B\rangle").move_to([-1.5, 0.8, 0])
        bline = Line(start =  [-1, 0.8, 0], end = [1, 0.8, 0]).set_color([MAROON_A, TEAL_B])
        Br = MathTex(r"|B \oplus A \rangle ").move_to([2, 0.8, 0])
        bdot = Dot(point = [0, 0.8, 0], radius = 0.08)

        group1 = VGroup(Al, tline, Ar, vline, Adot, Bl, bline, Br, bdot)

        UCN = MathTex(r"U_{CN}",  r" = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}").move_to([0, -2, 0])

        UCN[0].set_color([TEAL_B, MAROON_A])

        self.wait(2)
        self.play(Write(conot))
        self.wait()
        self.play(ReplacementTransform(conot, cnot))
        self.wait(2)
        self.play(ReplacementTransform(cnot, gate))

        self.wait(1)

        self.play(Write(group1), run_time = 5)

        self.wait(6)

        self.play(Write(UCN))

        self.wait(5)

        self.play(FadeOut(UCN, group1, title, gate), run_time = 3)


        xornand = Tex(r" can other classical gates like NAND / XOR be understood as unitary quantum gates similar to how CNOT represents NOT?").scale(0.75)

        A2l = MathTex(r"|A\rangle").move_to([1.5, 1.8, 0])
        t2line = Line(start =  [-1, 1.8, 0], end = [1, 1.8, 0]).set_color([TEAL_B, MAROON_A])
        A2r = MathTex(r"|A\rangle").move_to([-1.5, 1.8, 0])
        A2dot = Dot(point = [0, 1.8, 0], radius = 0.08)

        v5line = Line(start =  [0, 1.8, 0], end = [0, 0.8, 0]).set_color([TEAL_B, MAROON_A, TEAL_B])

        B2l = MathTex(r"|B\rangle").move_to([1.5, 0.8, 0])
        b2line = Line(start =  [-1, 0.8, 0], end = [1, 0.8, 0]).set_color([MAROON_A, TEAL_B])
        B2r = MathTex(r"|B \oplus A \rangle ").move_to([-2, 0.8, 0])
        b2dot = Dot(point = [0, 0.8, 0], radius = 0.08)

        group2 = VGroup(A2l, t2line, A2r, v5line, A2dot, B2l, bline, B2r, b2dot)

        ltriangle = Line(start =  [-1.9, -1, 0], end = [-0.9, -1, 0])
        vtriangle = Line(start =  [-0.9, -1.7, 0], end = [-0.9, -0.3, 0])
        tdiag = Line(start =  [-0.9, -0.3, 0], end = [0, -1, 0])
        bdiag = Line(start =  [-0.9, -1.7, 0], end = [0, -1, 0])
        circ = Circle(radius = 0.1, color = WHITE, fill_opacity = 1).move_to([0, -1, 0])
        rtriangle = Line(start =  [0.1, -1, 0], end = [1.2, -1, 0])

        x = MathTex(r"x").move_to([-2.4, -1, 0]).set_color([TEAL_B])
        xbar = MathTex(r"\bar{x}").move_to([1.7, -1, 0]).set_color([MAROON_A])

        right = MathTex(r"\longrightarrow").move_to([-1.75, -1, 0])
        right2 = MathTex(r"\longrightarrow").move_to([0.5, -1, 0])

        groupx = VGroup(ltriangle, vtriangle, tdiag, bdiag, right, right2, circ, rtriangle, x, xbar).scale(1.25)



        however = Tex(r" however, gates like NAND and XOR are \textit{irreversible}").scale(0.8).move_to([0, 1.5, 0])


        inverse = MathTex(r"U", r"\Longleftrightarrow", r" U'").move_to([0, -1.5, 0])
        inverse[0].set_color([TEAL_B])
        inverse[2].set_color([MAROON_A])

        cool_thing = Tex(r" \textit{Any multiple qubit logic gate can be composed from} CNOT \textit{and single qubit gates}").move_to([0, 0, 0]).scale(0.75)

        parallel = Tex("CNOT ", "is the quantum-parallel of the universality of", " NAND").move_to([0, 2, 0]).scale(0.75)
        parallel[0].set_color([TEAL_B])
        parallel[2].set_color([MAROON_A])

        arrow = MathTex(r"\Longleftrightarrow").move_to([0, -1.5, 0])

        A3l = MathTex(r"|A\rangle").move_to([-5, -2, 0])
        t3line = Line(start =  [-4.5, -2, 0], end = [-2.5, -2, 0]).set_color([TEAL_B, MAROON_A])
        A3r = MathTex(r"|A\rangle").move_to([-2, -2, 0])
        A3dot = Dot(point = [-3.5, -2, 0], radius = 0.08)

        v3line = Line(start =  [-3.5, -2, 0], end = [-3.5, -3, 0]).set_color([TEAL_B, MAROON_A, TEAL_B])

        B3l = MathTex(r"|B\rangle").move_to([-5, -3, 0])
        b3line = Line(start =  [-4.5, -3, 0], end = [-2.5, -3, 0]).set_color([MAROON_A, TEAL_B])
        B3r = MathTex(r"|B \oplus A \rangle ").move_to([-1.5, -3, 0])
        b3dot = Dot(point = [-3.5, -3, 0], radius = 0.08)

        group3 = VGroup(A3l, t3line, A3r, A3dot, v3line, B3l, b3line, B3r, b3dot).shift(UP*1)

        A4l = MathTex(r"|A\rangle").move_to([2.2, -2, 0])
        t4line = Line(start =  [2.7, -2, 0], end = [4.7, -2, 0]).set_color([TEAL_B, MAROON_A])
        A4r = MathTex(r"|A\rangle").move_to([5.2, -2, 0])
        A4dot = Dot(point = [3.7, -2, 0], radius = 0.08)

        v4line = Line(start =  [3.7, -2, 0], end = [3.7, -3, 0]).set_color([TEAL_B, MAROON_A, TEAL_B])

        B4l = MathTex(r"|B\rangle").move_to([5.2, -3, 0])
        b4line = Line(start =  [2.7, -3, 0], end = [4.7, -3, 0]).set_color([MAROON_A, TEAL_B])
        B4r = MathTex(r"|B \oplus A \rangle ").move_to([1.7, -3, 0])
        b4dot = Dot(point = [3.7, -3, 0], radius = 0.08)

        group4 = VGroup(A4l, t4line, A4r, A4dot, v4line, B4l, b4line, B4r, b4dot).shift(UP*1)

        groupfull = VGroup(group3, group4, arrow).shift(LEFT*0.1)

        self.wait(1)

        self.play(Write(xornand))
        self.wait(5)

        self.play(FadeOut(xornand))

        self.wait()
        self.play(Write(group2), run_time = 3) 
        self.wait()
        self.play(Write(inverse))
        self.wait(4)
        self.play(FadeOut(group2, inverse))
        self.wait(2)
        self.play(Write(however))
        self.wait(2)
        self.play(Write(groupx), run_time = 2)
        self.wait(4)
        self.play(FadeOut(however, groupx))
        self.wait()
        self.play(Write(cool_thing))
        self.wait(4)
        self.play(FadeOut(cool_thing))
        self.play(DrawBorderThenFill(parallel), Write(groupfull))
        self.wait(7)
        self.play(FadeOut(parallel, groupfull, arrow), run_time = 3)

class Wait(Scene):
    def construct(self):
        
        # literally just a black screen for 0.5seconds
        self.wait(0.5)

class Basis(Scene):
    def construct(self):
        title = Tex(r"Previously").to_edge(UL)

        psi = MathTex(r" \alpha |0\rangle + \beta |1\rangle").move_to([0, 1, 0])
        prob = Tex(" 0:",  r"$\; |\alpha|^2 \quad \Big| \quad$", "1:", r"$\; |\beta|^2$").move_to([0, -0.5, 0])
        prob[0].set_color([PINK, YELLOW])
        prob[2].set_color([YELLOW, PINK])

        compbasis = Tex(r" the states $|0\rangle$ and $|1\rangle$ represent just one of many possible choices of basis states for a qubit").scale(0.7).move_to([0, -2, 0])

        plus = MathTex(r" |+\rangle").move_to([-1, 0, 0]).set_color([TEAL_B, MAROON_A])
        minus = MathTex(r" |-\rangle").move_to([1, 0, 0]).set_color([PINK, YELLOW])

        plusminus2 = MathTex(r" |+\rangle", r" \equiv \frac{|0\rangle + |1\rangle}{\sqrt{2}} ").move_to([-2, 1.5, 0])
        plusminus3 = MathTex(r" |-\rangle", r" \equiv \frac{|0\rangle - |1\rangle}{\sqrt{2}} ").move_to([2, 1.5, 0])
        plusminus2[0].set_color([TEAL_B, MAROON_A])
        plusminus3[0].set_color([PINK, YELLOW])

        self.play(Write(title))
        self.wait()
        self.play(Write(psi))
        self.wait(2)

        self.play(DrawBorderThenFill(prob), run_time = 2)
        self.wait(2)
        self.play(Write(compbasis))
        self.wait(3)


        self.play(FadeOut(compbasis, psi, title, prob))
        self.wait()
        self.play(DrawBorderThenFill(plus), DrawBorderThenFill(minus))
        self.wait(2)
        self.play(ReplacementTransform(plus, plusminus2), ReplacementTransform(minus, plusminus3), run_time = 2)

        basis_change = MathTex(r"|\psi\rangle = \alpha|0\rangle + \beta|1\rangle = \frac{\alpha + \beta}{\sqrt{2}}", r"|+\rangle", r"+ \frac{\alpha - \beta}{\sqrt{2}}", r"|-\rangle").move_to([0, -1.5, 0])
        basis_change[1].set_color([TEAL_B, MAROON_A])
        basis_change[3].set_color([PINK, YELLOW])

        basis_change2 = MathTex(r"|\psi\rangle = \frac{\alpha + \beta}{\sqrt{2}}", r"|+\rangle", r"+ \frac{\alpha - \beta}{\sqrt{2}}", r"|-\rangle").move_to([0, 1, 0])
        basis_change2[1].set_color([TEAL_B, MAROON_A])
        basis_change2[3].set_color([PINK, YELLOW])


        self.wait(5)
        self.play(Write(basis_change))

        prob2 = Tex(r" yields $|+\rangle$ with probability $|\alpha + \beta|^2 / 2$, and $|-\rangle$ with probability $|\alpha - \beta|^2 / 2$").move_to([0, -1, 0]).scale(0.8)
        
        
        self.wait(2)
        self.play(FadeOut(plusminus2, plusminus3), ReplacementTransform(basis_change, basis_change2), run_time = 2)
        self.wait(2)
        self.play(Write(prob2), run_time = 4)
        self.wait(3)
        self.play(FadeOut(prob2, basis_change2), run_time = 2)


class Generally(Scene):
    def construct(self):
        title = Tex(r" More Generally,").to_edge(UL)

        basis = Tex(r" given any basis states ",  r"$|a\rangle$", r" and ", r"$|b\rangle$", ", ", r"$|\psi\rangle$", " can be represented as ", r"$|\psi\rangle$", r" = ", r"$\alpha$", r"$|a\rangle$", " + ", r"$\beta$", r"$|b\rangle$").move_to([0, 1, 0]).scale(0.8)
        basis[1].set_color([TEAL_B, MAROON_A])
        basis[3].set_color([PINK, YELLOW])
        basis[10].set_color([TEAL_B, MAROON_A])
        basis[13].set_color([PINK, YELLOW])

        ortho = Tex(r" provided the states are orthonormal, it gives $a$ with probability $|\alpha|^2$ and $b$ with probability $|\beta|^2$ such that").move_to([0, -0.5, 0]).scale(0.7)

        norm = MathTex(r"|\alpha|^2 + |\beta|^2 = 1").set_color([TEAL_B, PINK, YELLOW]).move_to([0, -2, 0])


        self.play(Write(title))
        self.wait(1)
        self.play(Write(basis), run_time = 3)
        self.wait(2)
        self.play(Write(ortho), run_time = 3)
        self.wait()
        self.play(Write(norm))
        self.wait(3)
        self.play(FadeOut(title, basis, ortho, norm), run_time = 5)


class Thumbnail(Scene):
    def construct(self):

        ax = Axes(
            x_range = (-10, 10, 1),
            y_range = (-10, 10, 1),
            x_length = 10,
            y_length = 10
        )


        x = MathTex(r"x").move_to([-5, 0, 0])
        xbar = MathTex(r"\bar{x}").move_to([-2.8, 0, 0])

        ltriangle = Line(start =  [-4.7, 0, 0], end = [-4.4, 0, 0]).set_color([TEAL_B, MAROON_A])
        vtriangle = Line(start =  [-4.4, -0.7, 0], end = [-4.4, 0.7, 0])
        tdiag = Line(start =  [-4.4, 0.7, 0], end = [-3.5, 0, 0])
        bdiag = Line(start =  [-4.4, -0.7, 0], end = [-3.5, 0, 0])
        circ = Circle(radius = 0.1, color = WHITE).move_to([-3.4, 0, 0])
        rtriangle = Line(start =  [-3.3, 0, 0], end = [-3, 0, 0]).set_color([MAROON_A, TEAL_B])

        vline = Line(start =  [-2, -2, 0], end = [-2, 2, 0]).set_color([TEAL_B, MAROON_A])
        xl = MathTex(r" \alpha |0\rangle + \beta |1\rangle").move_to([0, 1.5, 0])
        xlinel = Line(start =  [1.5, 1.5, 0], end = [2, 1.5, 0])
        xvl = Line(start =  [2, 1.875, 0], end = [2, 1.125, 0])
        xtl = Line(start =  [2, 1.875, 0], end = [2.75, 1.875, 0])
        xbl = Line(start =  [2, 1.125, 0], end = [2.75, 1.125, 0])
        xvr = Line(start =  [2.75, 1.125, 0], end = [2.75, 1.875, 0])

        xsq = Square(side_length = 0.75).move_to([2.375, 1.5, 0]).set_color([TEAL_B])

        xliner = Line(start =  [2.75, 1.5, 0], end = [3.25, 1.5, 0])
        X = MathTex(r"X").move_to([2.375, 1.5, 0]).scale(0.9)
        xr = MathTex(r" \beta |0\rangle + \alpha |1\rangle").move_to([4.75, 1.5, 0])

        zl = MathTex(r" \alpha |0\rangle + \beta |1\rangle").move_to([0, 0, 0])
        zlinel = Line(start =  [1.5, 0, 0], end = [2, 0, 0])
        zvl = Line(start =  [2, 0.375, 0], end = [2, -0.375, 0])
        ztl = Line(start =  [2, 0.375, 0], end = [2.75, 0.375, 0])
        zbl = Line(start =  [2, -0.375, 0], end = [2.75, -0.375, 0])
        zvr = Line(start =  [2.75, -0.375, 0], end = [2.75, 0.375, 0])
        zliner = Line(start =  [2.75, 0, 0], end = [3.25, 0, 0])
        Z = MathTex(r"Z").move_to([2.375, 0, 0]).scale(0.9)
        zr = MathTex(r" \alpha |0\rangle - \beta |1\rangle").move_to([4.75, 0, 0])

        zsq = Square(side_length = 0.75).move_to([2.375, 0, 0]).set_color([MAROON_A])

        hl = MathTex(r" \alpha |0\rangle + \beta |1\rangle").move_to([0, -1.5, 0])
        hlinel = Line(start =  [1.5, -1.5, 0], end = [2, -1.5, 0])
        hvl = Line(start =  [2, -1.125, 0], end = [2, -1.875, 0])
        htl = Line(start =  [2, -1.125, 0], end = [2.75, -1.125, 0])
        hbl = Line(start =  [2, -1.875, 0], end = [2.75, -1.875, 0])
        hvr = Line(start =  [2.75, -1.875, 0], end = [2.75, -1.125, 0])
        hliner = Line(start =  [2.75, -1.5, 0], end = [3.25, -1.5, 0])
        H = MathTex(r"H").move_to([2.375, -1.5, 0]).scale(0.9)
        hr = MathTex(r" \alpha \frac{|0\rangle + |1\rangle}{\sqrt{2}}\
                     + \beta\frac{|0\rangle - |1\rangle}{\sqrt{2}").move_to([5.35, -1.5, 0]).scale(0.7)

        hsq = Square(side_length = 0.75).move_to([2.375, -1.5, 0]).set_color([TEAL_B, PINK, YELLOW])

        group = VGroup(x, xbar, ltriangle, vtriangle, tdiag, bdiag, circ, rtriangle, vline,
                       xl, xlinel, xsq, xliner, X, xr,
                       zl, zlinel, zsq, zliner, Z, zr,
                       hl, hlinel, hsq, hliner, H, hr
                ).shift(1 * LEFT)

        group1 = VGroup(xl, xlinel, xvl, xtl, xbl, xvr, xliner, X, xr).set_color([TEAL_B])
        group2 = VGroup(zl, zlinel, zvl, ztl, zbl, zvr, zliner, Z, zr).set_color([MAROON_A])
        group3 = VGroup(hl, hlinel, hvl, htl, hbl, hvr, hliner, H, hr).set_color([TEAL_B, PINK, YELLOW])

        group.shift(DOWN*0.7)

        Quantum_Computation = Tex(r"Quantum Computation").move_to([0, 2.5, 0]).scale(1.5)

   
        self.add(group, Quantum_Computation)


