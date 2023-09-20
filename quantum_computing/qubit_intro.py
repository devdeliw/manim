from manim import * 
import numpy as np
import math 

class TwistedCurve(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)  # Set Camera Orientation
        axes = ThreeDAxes(x_length = 6, y_length = 6, z_length = 6)   

        state_0 = axes.get_z_axis_label(Tex(r"$|0\rangle$"))

        resolution_sphere = 10  

        sphere = Surface(
            lambda u, v: np.array([
                3 * np.cos(u) * np.cos(v),
                3 * np.cos(u) * np.sin(v),
                3 * np.sin(u)
            ]), v_range = [0,TAU], u_range = [-PI/2, PI/2], fill_opacity = 0.2, 
            checkerboard_colors=[BLUE_D, BLUE_A],
            resolution=(resolution_sphere, resolution_sphere)
        )                                                                                    

        initial_state = Vector([3, 0, 0], color = BLUE_B)
        hadamard_1 = Vector([0, 0, -3], color = BLUE_B)
        hadamard_2 = Vector([0, 0, 3], color = BLUE_B)

        self.play(Create(axes))
        self.play(Write(state_0))


        self.play(Write(sphere), run_time = 5)
        self.wait()

        self.begin_ambient_camera_rotation(rate = 0.3)

        initial_state_label = Tex(r"$\frac{|0 \rangle + |1 \rangle}{\sqrt(2)}$")

        hadamard_1_label = Tex(r"$| 1 \rangle$")
        hadamard_2_label = Tex(r"$| 0 \rangle$")
        
        initial_state_label.to_edge(LEFT)
        hadamard_1_label.to_edge(DOWN)
        hadamard_2_label.to_edge(UP)

        hadamard_matrix = Matrix([[ "1 / \sqrt{2} ", " 1/ \sqrt{2}"], ["-1 / \sqrt{2} ", " 1 / \sqrt{2}"]])
        hadamard_matrix.to_edge(DOWN + RIGHT)
        
        self.play(Write(hadamard_matrix))
        self.play(Write(initial_state))
        self.play(Write(initial_state_label))
        self.play(ReplacementTransform(initial_state, hadamard_1), run_time = 2)
        self.play(Write(hadamard_1_label))
        self.play(Transform(hadamard_1, hadamard_2), FadeOut(hadamard_1_label), run_time = 3)
        self.play(Write(hadamard_2_label))
        self.wait()
        self.play(FadeOut(hadamard_2))
        self.wait()

        self.stop_ambient_camera_rotation()

class Intro(VectorScene):
    def construct(self):
        computational_basis = Text("for a two level quantum system:").scale(0.5).move_to([0,2,0])
        qubit_0 = MathTex(r"| 0 \rangle = \begin{bmatrix} 1 \\ 0 \end{bmatrix}").move_to([-1.5,0.5,0])
        qubit_1 = MathTex(r"| 1 \rangle = \begin{bmatrix} 0 \\ 1 \end{bmatrix}").move_to([1.5,0.5,0])


        self.play(Write(computational_basis), run_time = 2)
        self.play(Write(qubit_0), Write(qubit_1))
        self.wait(2)
        group = VGroup(computational_basis, qubit_0, qubit_1)
        self.play(FadeOut(group), run_time = 2)

        ax = Axes( 
            x_range = (-5, 5, 7), 
            y_range = (-5, 5, 7),
            x_length = 7, 
            y_length = 7
        )
        
        labels = ax.get_axis_labels(

                MathTex(r"| 0 \rangle").scale(0.75), MathTex(r"| 1 \rangle").scale(0.75)
        )

        self.play(Write(ax), Write(labels))

        vector1 = self.add_vector([2, 3], color = BLUE_B)
        self.vector_to_coords(vector1)

        self.play(FadeOut(vector1))

        vector2 = self.add_vector([-2, -1], color = BLUE_B)
        self.vector_to_coords(vector2)

        vector22 = Vector([-2,-1]).set_color([TEAL_B, PINK, YELLOW])

        self.play(ReplacementTransform(vector2, vector22), run_time = 1)
        self.wait()
        superposition = MathTex(r" | \psi \rangle = -2 | 0 \rangle - | 1 \rangle").to_edge(DL)
        self.play(Write(superposition), run_time = 2)

        self.play(FadeOut(VGroup(vector22, ax, superposition, labels)), run_time = 3)


class Superposition(VectorScene): 
    def construct(self): 

        superposition = MathTex(r"&| \psi \rangle = \alpha | 0 \rangle + \beta | 1 \rangle \\ & (\alpha, \beta) \in \mathbb{C}").move_to([0,2,0])


        self.play(Write(superposition), run_time = 4)

        self.play(FadeOut(superposition), run_time = 2) 

        numberplane = NumberPlane()
        self.play(Write(numberplane))

        vector1 = self.add_vector([-2, 3], color = BLUE_B)
        label1 = self.write_vector_coordinates(vector1)
        self.wait()
        self.play(FadeOut(label1))

        vector2 = Vector([4, -3], color = BLUE_B)
        self.play(ReplacementTransform(vector1, vector2), run_time = 2)
        label2 = self.write_vector_coordinates(vector2)
        self.wait()
        self.play(FadeOut(label2))

        vector1 = self.add_vector([-2, 3], color = BLUE_B)
        vector3 = Vector([3, -4], color = PURPLE_B)
        vector4 = Vector([-3, -1], color = PURPLE_B)
        vector5 = Vector([3, 1], color = MAROON_B)
        vector6 = Vector([-4, -2], color = MAROON_B)
        vector7 = Vector([3, 1], color = RED_B)
        vector8 = Vector([1, -3], color = RED_B)
        vector9 = Vector([-3, 4], color = GREEN_B)
        vector10 = Vector([4, -3], color = GREEN_B)
        vector11 = Vector([1, 1], color = YELLOW_B)
        vector12 = Vector([-1, -2], color = YELLOW_B)


        self.play(ReplacementTransform(vector2, vector3), 
                  ReplacementTransform(vector1, vector4), 
                  run_time = 1
        )
        self.play(ReplacementTransform(vector3, vector5), 
                  ReplacementTransform(vector4, vector6), 
                  run_time = 1
        )
        self.play(ReplacementTransform(vector5, vector7),
                  ReplacementTransform(vector6, vector8),
                  run_time = 1
        )
        self.play(ReplacementTransform(vector7, vector9),
                  ReplacementTransform(vector8, vector10),
                  run_time = 1
        )
        self.play(ReplacementTransform(vector9, vector11),
                  ReplacementTransform(vector10, vector12),
                  run_time = 1
        )
    
        self.play(FadeOut(numberplane), FadeOut(vector11), FadeOut(vector12), run_time = 2)

class LinearCombQNOT(LinearTransformationScene): 
    def __init__(self): 
        LinearTransformationScene.__init__(
                self, 
                show_coordinates = True, 
                leave_ghost_vectors = True,
                show_basis_vectors = True
        )
    def construct(self):

        matrix = [[0, 1], [1, 0]]

        matrix_tex = Tex(r" QNOT $= \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$").to_edge(UL)

      
        vect1 = self.get_vector([1, -2], color = PURPLE_B)
        vect2 = self.get_vector([-4, 3], color = BLUE_B)

        self.add_transformable_mobject(vect1, vect2)
        self.add_background_mobject(matrix_tex) 
        self.apply_matrix(matrix, run_time = 5)

        self.play(FadeOut(matrix_tex))

class ComputationalBasis(Scene):
    def construct(self):
        vector_space = Tex(r"$ | \psi \rangle$ forms a vector space spanned by $| 0 \rangle$, $ | 1 \rangle $")
        basis = Tex(r"$|0\rangle$, $|1\rangle$ form the \textit{computational basis}").shift(1*DOWN)

        self.play(Write(vector_space))
        self.play(Write(basis))
        self.wait()
        self.play(FadeOut(vector_space, basis))


class LinearCombZ(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
                self,
                show_coordinates = True,
                leave_ghost_vectors = True,
                show_basis_vectors = True
        )
    def construct(self):

        matrix = [[1, 0], [0, -1]]

        matrix_tex = Tex(r" Z $= \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$").to_edge(UL)
        vect1 = self.get_vector([-2, 1], color = PURPLE_B)
        vect2 = self.get_vector([3, -4], color = BLUE_B)

        self.add_transformable_mobject(vect1, vect2)
        self.add_background_mobject(matrix_tex)
        self.apply_matrix(matrix, run_time = 5)

        self.play(FadeOut(matrix_tex))

class BasicQM(Scene):
    def construct(self):
        title = Tex(r"Fundamentals of $\psi$").to_edge(UL) 
        self.play(Write(title)) 

        psi = Tex(r" Qubits allow for linear combinations of 0, 1 states, known as superpositions $$ | \psi \rangle = \alpha | 0 \rangle + \beta | 1 \rangle$$").scale(0.7).move_to([0,2,0])

        qubit_collapse = Tex(r" Examining Qubits yields $ | 0 \rangle $ w/ probability $ | \alpha |^2 $, or $ |1 \rangle$  w/ probability $ | \beta |^2 $.").scale(0.7).move_to([0,0.5,0])

        therefore = Tex(r"Therefore,").scale(0.7).move_to([-5,-0.5,0])

        probability = MathTex(r"|\alpha|^2 + |\beta|^2 = 1").scale(0.7).move_to([0,-1,0])

        collapse = Tex(r"Once a qubit does collapse into $| 0 \rangle$ or $| 1 \rangle$, the post-measurement state of the qubit will be the same.").scale(0.7).move_to([0,-2,0])

        uncertain = Tex(r"No one knows why this collapse occurs, this behavior is simply one of the \textit{fundamental postulates of quantum mechanics.}").scale(0.7).move_to([0,-3,0]) 

        self.play(Write(psi))
        self.wait(2)
        self.play(Write(qubit_collapse))
        self.wait()
        self.play(Write(therefore))
        self.play(Write(probability))
        self.wait(3)
        self.play(Write(collapse))
        self.play(Write(uncertain))
        self.wait()
        self.play(FadeOut(VGroup(title, psi, qubit_collapse, therefore, probability, collapse, uncertain)), run_time = 3)
        self.wait(1)

class Probability(ThreeDScene):
    def construct(self): 
        
        axes = ThreeDAxes(
            x_range = (-5, 5, 1), 
            y_range = (-5, 5, 1), 
            z_range = (-5, 5, 1), 
            x_length = 5, 
            y_length = 5, 
            z_length = 5,

        )

        self.renderer.camera.light_source.move_to(3*IN)

        self.set_camera_orientation(
            phi = 90*DEGREES,
            theta = 0*DEGREES, 
            distance = 4
        )

        labels = axes.get_axis_labels(
            Tex(""), Text(""), MathTex(r"| 0 \rangle").scale(0.45)
        )

        arrow1 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([-2, 3, -1]),
            resolution=8,
            color = BLUE_B)
        arrow2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([-2, -2, 3]),
            resolution=8,
            color = BLUE_B)
        arrow3 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 2, -1]),
            resolution=8,
            color = BLUE_B)
        arrow4 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 1, 2]),
            resolution=8,
            color = BLUE_B)
        arrow5 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([-3, -1, 3]),
            resolution=8,
            color = BLUE_B)
        arrow6 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([3, -1, -3]),
            resolution=8,
            color = BLUE_B)

        self.begin_ambient_camera_rotation(rate = 0.4)

        self.play(GrowFromPoint(arrow1, ORIGIN), 
                  GrowFromPoint(arrow2, ORIGIN),
                  GrowFromPoint(arrow3, ORIGIN),
                  GrowFromPoint(arrow4, ORIGIN),
                  GrowFromPoint(arrow5, ORIGIN),
                  GrowFromPoint(arrow6, ORIGIN),
                  run_time = 4)

        self.wait(5)

        arr1 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([3, 1, 1]),
            resolution=8, 
            color = PURPLE_B)
        arr2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, -1, 3]),
            resolution=8,
            color = PURPLE_B)
        arr3 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([-3, 1, -2]),
            resolution=8,
            color = PURPLE_B)
        arr4 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([-2, -4, 3]),
            resolution=8,
            color = PURPLE_B)
        arr5 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([-3, -1, -2]),
            resolution=8,
            color = PURPLE_B)
        arr6 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 0, 0]),
            resolution=8,
            color = PURPLE_B)

        self.play(ReplacementTransform(arrow1, arr1),
                  ReplacementTransform(arrow2, arr2), 
                  ReplacementTransform(arrow3, arr3), 
                  ReplacementTransform(arrow4, arr4),
                  ReplacementTransform(arrow5, arr5), 
                  ReplacementTransform(arrow6, arr6), 
                  run_time = 6
        )

        self.play(FadeOut(arr1, arr2, arr3, arr4, arr5), run_time = 2)
        one = MathTex(r"|1\rangle").move_to([0.2, 0, -2.5]).scale(0.6)

        self.add_fixed_orientation_mobjects(one)

        self.play(Create(axes), Write(labels), Write(one))

        self.stop_ambient_camera_rotation()

        self.move_camera(
            phi = 90*DEGREES, 
            theta = -90*DEGREES,
            distance = 2,
            zoom = 1.3,
            run_time = 3
        )

        self.begin_3dillusion_camera_rotation(rate = 0.1)

        coords = MathTex(r"{{\frac{1}{\sqrt{2}}}} | 0 \rangle + {{\frac{1}{\sqrt{2}}}} | 1 \rangle").move_to([-2,-2,-2])

        coords[0].set_color(TEAL_D)
        coords[2].set_color(PURPLE_B)

        qubit_0 = Arrow3D(
                start = np.array([0,0,0]),
                end = np.array([0,0,1]),
                resolution = 8, 
                color = PURPLE_B
        )

        qubit_1 = Arrow3D(
                start = np.array([0,0,0]),
                end = np.array([0,0,-1]),
                resolution = 8,
                color = BLUE_D
        )

        coords_transform = MathTex(r"{{\frac{1}{2}}} | 0 \rangle + {{\frac{1}{2}}} | 1 \rangle").move_to([-2,-2,-2])
        coords_transform[0].set_color(BLUE_B)
        coords_transform[2].set_color(MAROON_B)

        self.add_fixed_orientation_mobjects(coords)

        self.play(Write(coords))

        self.wait(5)

        sphere = Surface(
            lambda u, v: np.array([
                2 * np.cos(u) * np.cos(v),
                2 * np.cos(u) * np.sin(v),
                2 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[TEAL_D, PURPLE_A], resolution=(32, 64), fill_opacity = 0.1
        )

        self.play(Create(sphere), FadeOut(axes), run_time = 4)
        self.wait(4)

        self.stop_3dillusion_camera_rotation()

        vec1 = Arrow3D(
                start = np.array([0,0,0]),
                end = np.array([0,0,-2]),
                resolution = 8, 
                color = MAROON_B
        )

        vec0 = Arrow3D(
                start = np.array([0,0,0]),
                end = np.array([0,0,2]), 
                resolution = 8,
                color = BLUE_B
        )

        arr7= Arrow3D(
            start=np.array([0, 0, 0]),
            end=np.array([2, 0, 0]),
            resolution=8,
            color = TEAL_B)

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers() 

        self.play(Transform(coords, coords_transform), run_time = 1.5)
        self.wait()

        self.play(ReplacementTransform(arr6, vec0), phi.animate.set_value(0*DEGREES), run_time = 4)
        self.wait(2)
        self.play(ReplacementTransform(vec0, arr7), phi.animate.set_value(90*DEGREES), theta.animate.set_value(90*DEGREES), run_time = 3)
        self.wait(1)
        self.play(ReplacementTransform(arr7, vec1), phi.animate.set_value(-90*DEGREES), run_time = 4)
        self.wait(5) 

        self.play(FadeOut(vec1, sphere, labels, one, coords), run_time = 4)

class Determination(Scene):
    def construct(self):
        title = Tex(r"Methods of realizing Qubits").to_edge(UL)


        bullet1 = Tex(r"different polarizations of a photon").move_to([0,2,0])
        bullet2 = Tex(r"adjustment of nuclear spin in a magnetic field").move_to([0,1,0])
        bullet3 = Tex(r"two different states of an electron orbiting an electron").move_to([0,0,0])


        self.play(Write(bullet1))
        self.wait()
        self.play(Write(bullet2))
        self.wait()
        self.play(Write(bullet3))

        self.wait()
        self.play(FadeOut(bullet1, bullet2, bullet3), run_time = 1)


class BlochSphereDeriv(ThreeDScene):
    def construct(self):
        
        prob = Tex(r"Because $|\alpha|^2 + |\beta|^2 = 1$,").to_edge(UL)
        deriv = MathTex(r"|\psi\rangle &= \alpha |0\rangle + \beta |1\rangle \\ &=e^{i\gamma} \left(\cos{\frac{\theta}{2}} |0\rangle + e^{i\varphi}\sin{\frac{\theta}{2}}|1\rangle\right)").move_to([0,1,0])
        final = MathTex(r"|\psi\rangle & \approx \cos{\frac{\theta}{2} |0\rangle + e^{i\varphi}\sin{\frac{\theta}{2}} |1\rangle").move_to([0, -2.5, 0])


        self.play(Write(prob))
        self.wait(3)
        self.play(Write(deriv), run_time = 5)
        self.wait(3)
        self.play(Write(final))
        self.wait(2)
        self.play(FadeOut(prob, deriv), run_time = 2)

        axes = ThreeDAxes(
            x_range = (-1, 1, 1), 
            y_range = (-1, 1, 1), 
            z_range = (-1, 1, 1), 
            x_length = 10, 
            y_length = 10, 
            z_length = 7
        )

        self.move_camera(
            phi = 90*DEGREES, 
            theta = -90*DEGREES,
            distance = 1
        )  

        self.play(FadeOut(final))

        arrow1 = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([2, 0, 0]),
            resolution = 8, 
            color = TEAL_B, 
        )

        arrow2 = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([2, 2, 0]),
            resolution = 8, 
            color = BLUE_B, 
        )

        arrow3 = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([2, 2, 2]),
            resolution = 8, 
            color = TEAL_B, 
        )

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()

        sphere = Surface(
            lambda u, v: np.array([
            2 * np.cos(u) * np.cos(v),
            2 * np.cos(u) * np.sin(v),
            2 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_A, PURPLE_A], resolution=(32, 64), fill_opacity = 0.1
        )

        one = MathTex(r"|1\rangle").move_to([0.3, 0, -3]).scale(0.6)
        zero = MathTex(r"|0\rangle").move_to([0.3, 0, 3]).scale(0.6)

        self.add_fixed_orientation_mobjects(one)
        self.add_fixed_orientation_mobjects(zero)

        self.play(Create(axes), Write(one), Write(zero), run_time = 2)

        self.play(GrowFromPoint(arrow1, ORIGIN), Create(sphere), run_time = 4)

        thetax = MathTex(r"\theta").move_to([-3,-3, 0])
        self.play(Write(thetax))
        self.add_fixed_in_frame_mobjects(thetax)

        self.play(ReplacementTransform(arrow1, arrow2), theta.animate.set_value(35*DEGREES), phi.animate.set_value(80*DEGREES), run_time = 3)
        self.wait()

        self.play(ReplacementTransform(arrow2, arrow3), phi.animate.set_value(70*DEGREES), Transform(thetax, MathTex(r"\varphi").move_to([-3, -3, 0])), run_time = 3)
        self.wait(3)

        blochsphere = Tex(r"Bloch Sphere").to_edge(DR).set_color(TEAL_B)
        self.add_fixed_in_frame_mobjects(blochsphere)

        self.play( DrawBorderThenFill(blochsphere), run_time = 1)
        self.wait(2)

        self.play(FadeOut(blochsphere, arrow3, thetax, sphere, one, zero, axes), run_time = 2)



class MultipleQubits(Scene):
    def construct(self):
        title = Tex(r"Suppose we have two qubits").to_edge(UL)

        classical = Tex(r"If these were classical bits, there would be four combinations: ").scale(0.7).move_to([0,2,0])
        classical_bits = Tex(r" 00, 01, 10, 11 ").scale(0.8).move_to([0,0.5,0])
        quantum = Tex(r"A two qubit system has four \textit{computational basis states} denoted: ").scale(0.7).move_to([0,2,0])
        qubits = MathTex(r" |00\rangle, |01\rangle, |10\rangle, |11\rangle").scale(0.8).scale(0.9).move_to([0,0.5,0])
        basis = Tex(r"A pair of qubits can exist in any superposition of these\
                four states such that the state vector describing the two qubits is ").scale(0.7).move_to([0,-1,0])
        
        superposition = MathTex(r" |\psi\rangle = {{\alpha_{00}}} |00\rangle\
                                + {{\alpha_{01}}}|01\rangle\
                                + {{\alpha_{10}}}|10\rangle\
                                + {{\alpha_{11}}}|11\rangle").scale(0.8).move_to([0,-2,0])

        superposition[1].set_color(TEAL_B)
        superposition[3].set_color(TEAL_B)
        superposition[5].set_color(MAROON_A)
        superposition[7].set_color(MAROON_A)


        self.play(Write(title))
        self.wait(2)
        self.play(Write(classical))
        self.play(Write(classical_bits))
        self.wait(1)
        self.play(FadeOut(classical_bits, classical))

        self.wait(2)

        self.play(Write(quantum))
        self.wait()
        self.play(Write(qubits))
        self.wait(3)
        self.play(Write(basis))
        self.wait()
        self.play(Write(superposition))
        self.wait(3)
        self.play(FadeOut(quantum, qubits, basis, title), run_time = 2)

        superposition2 = MathTex(r" |\psi\rangle = {{\alpha_{00}}} |00\rangle\
                                + {{\alpha_{01}}}|01\rangle\
                                + {{\alpha_{10}}}|10\rangle\
                                + {{\alpha_{11}}}|11\rangle").scale(0.8).move_to([0,2,0])

        superposition2[1].set_color(TEAL_B)
        superposition2[3].set_color(TEAL_B)
        superposition2[5].set_color(MAROON_A)
        superposition2[7].set_color(MAROON_A)

        self.play(ReplacementTransform(superposition, superposition2), run_time = 1)

        alpha_00 = MathTex(r"\alpha_{00}").move_to([-2.5, 2, 0])
        alpha_01 = MathTex(r"\alpha_{01}").move_to([-1.0, 2, 0])
        alpha_10 = MathTex(r"\alpha_{10}").move_to([1.5, 2, 0])
        alpha_11 = MathTex(r"\alpha_{11}").move_to([3.5, 2, 0])

        normalization = MathTex(r"|{{\alpha_{00}}}|^2 + |{{\alpha_{01}}}|^2 + |{{\alpha_{10}}}|^2 + |{{\alpha_{11}}}|^2 \cdots {{\sum_{n} |\alpha_i|^2 = 1}}").move_to([0, 0, 0])
        condition = Tex(r"normalization condition").move_to([0, -2, 0])

        normalization[9].set_color(YELLOW)
        normalization[1].set_color(TEAL_B)
        normalization[3].set_color(TEAL_B)
        normalization[5].set_color(MAROON_A)
        normalization[7].set_color(MAROON_A)


        self.play(Write(normalization), DrawBorderThenFill(condition), run_time = 5)
        self.wait(2)
        self.play(ReplacementTransform(alpha_00, normalization[1]),
                  ReplacementTransform(alpha_01, normalization[3]),
                  ReplacementTransform(alpha_10, normalization[5]),
                  ReplacementTransform(alpha_11, normalization[7]),
                  run_time = 2
        )
        self.wait(2)

        
        self.play(FadeOut(normalization, condition, superposition2), run_time = 2)

        title = Tex(r"2 Qubits").to_edge(UL)

        norm = MathTex(r"\sum_{x \in \{0,1\}^2} |\alpha_x|^2 = 1").move_to([0, 1, 0])
        
        post = Tex(r"Measuring the first qubit yields a chance of $|0\rangle$ with probability $|\alpha_{00}|^2 + |\alpha_{01}|^2$").scale(0.7).move_to([0, -0.5, 0])

        text = Tex(r"The post-measurement state is then, accounting for renormalization,").scale(0.7).move_to([-0.7, -1.4, 0])


        post_measurement = MathTex(r" |\psi'\rangle = \frac{\alpha_{00} |00\rangle + \alpha_{01}|01\rangle}{\sqrt{|\alpha_{00}|^2 + |\alpha_{01}|^2}}").move_to([0, -2.7, 0]).scale(0.8)

        norm2 = MathTex(r"\sum_{x \in \{0,1\}^2} |\alpha_x|^2 = 1").move_to([0, 1, 0]).set_color(YELLOW)

        self.play(Write(title), run_time = 1)
        self.wait(1)
        self.play(Write(norm), run_time = 2)
        self.wait(2)
        self.play(Write(post), run_time = 3)
        self.wait(2)
        self.play( Write(text), run_time = 2)
        self.play(Write(post_measurement), run_time = 2)
        self.wait(3)
        self.play(ReplacementTransform(norm, norm2))
        self.wait(2)
        self.play( FadeOut(title, norm2, post, post_measurement, text), run_time = 2)



class LinearTransformation3D(ThreeDScene):

    CONFIG = {
        "x_axis_label": "$|\alpha_{00}\rangle$",
        "y_axis_label": "$|\alpha_{01}\rangle$",
        "basis_i_color": GREEN,
        "basis_j_color": RED,
        "basis_k_color": GOLD
    }

    def create_matrix(self, np_matrix):


        m = Matrix(np_matrix)

        m.scale(0.5)
        m.set_column_colors(TEAL_B, MAROON_A, GOLD_A)

        m.to_corner(UP + LEFT)

        return m

    def construct(self):

        M = np.array([
            [-4, 6, 0],
            [3, 5, 0],
            [0, 0, 0]
        ])

        i_color = PINK
        j_color = TEAL_A
        k_color = RED_A

        axes = ThreeDAxes(
            x_range = (-10, 10, 10), 
            y_range = (-10, 10, 10), 
            z_range = (-10, 10, 7), 
            x_length = 10, 
            y_length = 10, 
            z_length = 7
        )
        
        
        axes.set_color(GRAY)

        labels = axes.get_axis_labels(
            MathTex(r"|00\rangle").scale(0.65), MathTex(r"|01\rangle").scale(0.65), MathTex(r"|10\rangle").scale(0.65)
        )

        self.set_camera_orientation(
            phi = 75*DEGREES,
            theta = -45*DEGREES, 
        )

        self.begin_ambient_camera_rotation(rate=0.1)

        self.play(Create(axes), Write(labels), run_time = 2)

        # basis vectors i,j,k
        basis_vector_helper = Tex(r"$i$", ",", r"$j$", ",", r"$k$")
        basis_vector_helper[0].set_color([PINK,YELLOW])
        basis_vector_helper[2].set_color([TEAL_B,MAROON_A])
        basis_vector_helper[4].set_color([GREEN_A,PURPLE_A])

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # matrix
        matrix = self.create_matrix(M)

        self.add_fixed_in_frame_mobjects(matrix)

        # axes & camera
        self.add(axes)

        cube = Cube(side_length=1, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([1, 0, 0]),
            resolution = 2,
            color = [PINK, YELLOW]
        ).scale(0.9)

        j_vec = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([0, 1, 0]),
            resolution = 2,
            color = [TEAL_A, MAROON_A]
        ).scale(0.9)

        k_vec = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([0, 0, 1]),
            color = [RED_A, PURPLE_A],
            resolution = 2
        ).scale(0.9)

        i_vec_new = Arrow3D(
            start = np.array([0, 0, 0]),
            end = M @ np.array([1, 0, 0]),
            color = [PINK, YELLOW],
            resolution = 2
        ).scale(0.9)

        j_vec_new = Arrow3D(
            start = np.array([0, 0, 0]),
            end = M @ np.array([0, 1, 0]),
            color = [TEAL_B, MAROON_A],
            resolution = 2
        ).scale(0.9)

        k_vec_new = Arrow3D(
            start = np.array([0, 0, 0]),
            end = M @ np.array([0, -1, 0]),
            resolution = 2,
            color = [RED_A, PURPLE_A]
        ).scale(0.7)

        i_vec_new_new = Arrow3D(
            start = np.array([0, 0, 0]),
            end = M @ np.array([0.5, 0, 0]),
            resolution = 2,
            color = [PINK, YELLOW]
        )
        


        self.play(
            Create(cube),
            GrowFromPoint(i_vec, ORIGIN),
            GrowFromPoint(j_vec, ORIGIN),
            GrowFromPoint(k_vec, ORIGIN),
            Write(basis_vector_helper)
        )

        self.wait(5)

        matrix_anim = ApplyMatrix(M, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait(1)

        self.play(Transform(i_vec, i_vec_new_new), run_time = 4)

        self.wait(7)

        self.play(FadeOut(i_vec, j_vec, k_vec, axes, basis_vector_helper, matrix, cube, labels), run_time = 4)


class EPR(ThreeDScene):
    def construct(self):
        
        
        title = Tex(r"EPR Paradox").to_edge(UL)

        suppose = Tex(r" Suppose we were given the following 2 qubit system:").move_to([-2, 2, 0]).scale(0.7)

        epr = MathTex(r"|\psi\rangle = \frac{ |00 \rangle + |11 \rangle}{\sqrt{2}}").move_to([0, 0.5, 0]).scale(0.8)

        alpha = MathTex(r"\alpha_{00}", r"= \frac{1}{\sqrt{2}}, \;\;\;", r"\alpha_{11}", r"= \frac{1}{\sqrt{2}").move_to([0, -2, 0]).scale(0.8)

        alpha[0].set_color(TEAL_B)
        alpha[2].set_color(MAROON_A)

        alpha_T = MathTex(r"|00\rangle}}", r": \; \frac{1}{2}, \;\;\;", r"|11\rangle", r": \; \frac{1}{2}").move_to([0, -1, 0]).scale(0.8)

        alpha_T[0].set_color(TEAL_B)
        alpha_T[2].set_color(MAROON_A)

        self.play(Write(title), run_time = 1)
        self.wait(3)
        self.play(Write(suppose), run_time = 2)
        self.wait(1)
        self.play( DrawBorderThenFill(epr), run_time = 1)
        self.wait(4)
        self.play(Write(alpha), run_time = 1)
        self.wait(5)
        self.play(ReplacementTransform(alpha, alpha_T), run_time = 2)
        self.wait(2)

        epr2 = MathTex(r" |\psi '\rangle =", r"|00\rangle").move_to([0, -0.5, 0]).scale(0.8)
        epr2[1].set_color(TEAL_B)
        epr3 = MathTex(r" |\psi '\rangle =", r"|11\rangle").move_to([0, -0.5, 0]).scale(0.8)
        epr3[1].set_color(MAROON_A)

        alpha_T2 = MathTex(r"|00\rangle", r": \; \frac{1}{2}, \;\;\;", r"|11\rangle", r": \; \frac{1}{2}").move_to([0, 2, 0]).scale(0.8)

        alpha_T2[0].set_color(TEAL_B)
        alpha_T2[2].set_color(MAROON_A)

        self.play(FadeOut(title, suppose), run_time = 1)
        self.play( ReplacementTransform(alpha_T, alpha_T2), run_time = 1)
        self.wait(2)
        self.play( ReplacementTransform(epr, epr2), run_time = 2)
        self.wait(2)
        self.play( ReplacementTransform(epr2, epr3), run_time = 2)
        self.wait(4)
        self.play( FadeOut(epr3, alpha_T2), run_time = 3)



        entanglement = Tex("entanglement").set_color([TEAL_B,PINK,YELLOW]).scale(0.8).move_to([0, 0, 0])
        self.wait()
        self.play( DrawBorderThenFill(entanglement), run_time = 2)

        self.add_fixed_orientation_mobjects(entanglement)

        axes = ThreeDAxes(
            x_range = (-3, 3, 3),
            y_range = (-3, 3, 3),
            z_range = (-3, 3, 3),
            x_length = 3,
            y_length = 3,
            z_length = 3
        ).move_to([3, 0, 0])


        self.set_camera_orientation(
            phi = 90*DEGREES,
            theta = -90*DEGREES,
        )

        q1 = Surface(
            lambda u, v: np.array([
            1 * np.cos(u) * np.cos(v),
            1 * np.cos(u) * np.sin(v),
            1 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[TEAL_B, MAROON_A], resolution=(16, 32), fill_opacity = 0.1
        ).move_to([3, 0, 0]).set_opacity(0.05)

        q2 = Surface(
            lambda u, v: np.array([
            1 * np.cos(u) * np.cos(v),
            1 * np.cos(u) * np.sin(v),
            1 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_A, PURPLE_A], resolution=(16, 32), fill_opacity = 0.1
        ).move_to([-3, 0, 0]).set_opacity(0.05)

        line1 = Line([3,0,-2], [3,0,2]).set_color([TEAL_B, MAROON_A]).set_opacity(0.3)
        line2 = Line([-3,0,-2], [-3,0,2]).set_color([PINK, YELLOW]).set_opacity(0.3)

        self.play(Create(q1), Create(q2),
                  DrawBorderThenFill(line1), DrawBorderThenFill(line2),
                  run_time = 4
        )
        self.wait(5)
        self.play(FadeOut(entanglement), run_time = 2)

class Entanglement(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(
            phi = 90*DEGREES,
            theta = -90*DEGREES, 
        )
        

        q1 = Surface(
            lambda u, v: np.array([
            1 * np.cos(u) * np.cos(v),
            1 * np.cos(u) * np.sin(v),
            1 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[TEAL_B, MAROON_A], resolution=(16, 32), fill_opacity = 0.1
        ).move_to([3, 0, 0])

        q2 = Surface(
            lambda u, v: np.array([
            1 * np.cos(u) * np.cos(v),
            1 * np.cos(u) * np.sin(v),
            1 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_A, PURPLE_A], resolution=(16, 32), fill_opacity = 0.1
        ).move_to([-3, 0, 0])

        vec1 = Arrow3D(
            start = np.array([3, 0, 0]),
            end = np.array([4, 0, 0]),
            resolution = 8, 
            color = WHITE, 
        )

        vec2 = Arrow3D(
            start = np.array([3, 0, 0]),
            end = np.array([3, 0, 1]),
            resolution = 8, 
            color = WHITE, 
        )

        vec11 = Arrow3D(
            start = np.array([-3, 0, 0]),
            end = np.array([-2, 0, 0]),
            resolution = 8, 
            color = WHITE, 
        )
        
        vec12 = Arrow3D(
            start = np.array([-3, 0, 0]),
            end = np.array([-3, 0, 1]),
            resolution = 8, 
            color = WHITE, 
        )


        self.play(Create(q1), Create(q2), run_time = 4)
        self.play(Write(vec1), Write(vec11), run_time = 1)
        self.wait(2)

        self.play( ReplacementTransform(vec1, vec2), run_time = 1)
        self.wait()

        self.play( ReplacementTransform(vec11, vec12), run_time = 1)
        self.wait(4)

        self.play( FadeOut(vec2, vec12, q1, q2), run_time = 4)

class Entanglement2(ThreeDScene):
    def construct(self): 
       
        axes = ThreeDAxes(
            x_range = (-3, 3, 3), 
            y_range = (-3, 3, 3), 
            z_range = (-3, 3, 3), 
            x_length = 3, 
            y_length = 3, 
            z_length = 3
        ).move_to([3, 0, 0])
        

        self.set_camera_orientation(
            phi = 90*DEGREES,
            theta = -90*DEGREES, 
        )

        q1 = Surface(
            lambda u, v: np.array([
            1 * np.cos(u) * np.cos(v),
            1 * np.cos(u) * np.sin(v),
            1 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[TEAL_B, MAROON_A], resolution=(16, 32), fill_opacity = 0.1
        ).move_to([3, 0, 0])

        q2 = Surface(
            lambda u, v: np.array([
            1 * np.cos(u) * np.cos(v),
            1 * np.cos(u) * np.sin(v),
            1 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_A, PURPLE_A], resolution=(16, 32), fill_opacity = 0.1
        ).move_to([-3, 0, 0])

        line1 = Line([3,0,-2], [3,0,2]).set_color([TEAL_B, MAROON_A])
        line2 = Line([-3,0,-2], [-3,0,2]).set_color([PINK, YELLOW])
    
        self.play(FadeIn(q1, q2, line1, line2))

        self.play(Rotate(q1, 2*PI, axis = [0,0,1]),
                  Rotate(q1, PI/4, axis = [2,1,1]), 
                  Rotate(line1, PI/4, axis = [2,1,1]), 
                  run_time = 1
        )

        axes2 = ThreeDAxes(
            x_range = (-3, 3, 3), 
            y_range = (-3, 3, 3), 
            z_range = (-3, 3, 3), 
            x_length = 3, 
            y_length = 3, 
            z_length = 3
        ).move_to([-3, 0, 0])

        self.play(Rotate(q2, 2*PI, axis = [0,0,1]),
                  Rotate(q2, PI/4, axis = [2,-1,-1]),
                  Rotate(line2, PI/4, axis = [2,-1,-1]),
                  run_time = 1
        )

        self.play(Rotate(q1, 20*PI, axis = [0,0,1]),
                  Rotate(line1, 20*PI, axis = [0,0,1]), 
                  Rotate(q2, -20*PI, axis = [0,0,1]),
                  Rotate(line2, -20*PI, axis = [0,0,1]),
                  rate_func = rate_functions.ease_in_sine, 
                  run_time = 10
        )

        self.play(Rotate(q1, 2*PI, axis = [0,0,1], rate_func = rate_functions.ease_out_cubic),
                  Rotate(line1, 2*PI, axis = [0,0,1], rate_func = rate_functions.ease_out_cubic), 
                  Rotate(q2, -4*PI, axis = [0,0,1], rate_func = linear), 
                  Rotate(line2, -4*PI, axis = [0,0,1], rate_func = linear),
                  run_time = 2
        )

        self.play(Rotate(q2, -4*PI, axis = [0,0,1], rate_func = linear),
                  Rotate(line2, -4*PI, axis = [0,0,1], rate_func = linear), 
                  run_time = 2
        )

        self.play(Rotate(q2, -2*PI, axis = [0,0,1], rate_func = rate_functions.ease_out_cubic), 
                  Rotate(line2, -2*PI, axis = [0,0,1], rate_func = rate_functions.ease_out_cubic), 
                  run_time = 4
        )

        self.play(FadeOut(q1, q2, line1, line2), run_time = 4)


        
        








                




                




                 
                
                









                        
                







                        



