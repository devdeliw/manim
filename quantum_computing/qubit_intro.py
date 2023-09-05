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

        ax = Axes()
        labels = ax.get_axis_labels(

                MathTex(r"| 0 \rangle").scale(0.75), MathTex(r"| 1 \rangle").scale(0.75)
        )

        self.play(Write(ax), Write(labels))

        vector1 = self.add_vector([2, 3], color = BLUE_B)
        self.vector_to_coords(vector1)

        vector2 = self.add_vector([-2, -1], color = BLUE_B)
        self.vector_to_coords(vector2)

        self.play(FadeOut(vector1))

        superposition = MathTex(r" | \psi \rangle = -2 | 0 \rangle - | 1 \rangle").to_edge(DL)
        self.play(Write(superposition), run_time = 2)

        self.play(FadeOut(VGroup(vector2, ax, superposition, labels)), run_time = 3)


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

        self.play(FadeOut(vec1, sphere), run_time = 4)

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
        deriv = MathTex(r"|\psi\rangle &= \alpha |0\rangle + \beta |1\rangle \\ &=e^{i\gamma} \left(\cos{\frac{\theta}{2}} |0\rangle + e^{i\varphi}\sin{\frac{\theta}{2}}|1\rangle\right)").move_to([0,0,0])
        final = MathTex(r"|\psi\rangle & \approx \cos{\frac{\theta}{2} |0\rangle + e^{i\varphi}\sin{\frac{\theta}{2}} |1\rangle").move_to([0, -3, 0])


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
            z_length = 10
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

        phix = MathTex(r"\varphi").move_to([-8,-8,-8])
        thetax = MathTex(r"\theta").move_to([-8,-8,-8])

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()

        sphere = Surface(
            lambda u, v: np.array([
            2 * np.cos(u) * np.cos(v),
            2 * np.cos(u) * np.sin(v),
            2 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[RED_A, PURPLE_A], resolution=(32, 64), fill_opacity = 0.1
        )

        self.play(Create(axes), run_time = 1)

        self.play(GrowFromPoint(arrow1, ORIGIN), Create(sphere), run_time = 4)

        self.add_fixed_orientation_mobjects(thetax)

        self.play(ReplacementTransform(arrow1, arrow2), theta.animate.set_value(35*DEGREES), phi.animate.set_value(80*DEGREES), run_time = 3)
        self.wait()

        self.play(ReplacementTransform(arrow2, arrow3), phi.animate.set_value(70*DEGREES), Transform(thetax, phix), run_time = 3)
        self.wait(3)



        




         
        
        









                
        







                



