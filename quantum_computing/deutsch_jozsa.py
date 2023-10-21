from manim import * 
from manim_ml.neural_network import Convolutional2DLayer, FeedForwardLayer, NeuralNetwork
from manim_ml.neural_network.animations.dropout import make_neural_network_dropout_animation
import numpy as np
import math


class Intro(ThreeDScene):
    def construct(self):
        nn = NeuralNetwork([
                Convolutional2DLayer(1, 7, 3, filter_spacing=0.32),
                Convolutional2DLayer(3, 5, 3, filter_spacing=0.32),
                Convolutional2DLayer(5, 3, 3, filter_spacing=0.18),
                Convolutional2DLayer(12, 2, 3, filter_spacing = 0.16)
            ],
            layer_spacing=0.25,
        )
        nn.move_to(ORIGIN).scale(2)

        self.play(FadeIn(nn), run_time = 2)

        forward_pass = nn.make_forward_pass_animation()

        self.play(forward_pass, run_time = 9)
        self.remove(nn)
        self.wait(1)

class Neural(ThreeDScene):
    def construct(self):
        
        nn = NeuralNetwork([
        FeedForwardLayer(3),
        FeedForwardLayer(5),
        FeedForwardLayer(3),
        FeedForwardLayer(5),
        FeedForwardLayer(4),
            ],
            layer_spacing=0.4,
        )
        nn.move_to([0,1.5,0]).scale(1.5)

        nn2 = NeuralNetwork([
        FeedForwardLayer(3),
        FeedForwardLayer(4),
        FeedForwardLayer(5),
        FeedForwardLayer(2),
        FeedForwardLayer(4),
            ],
            layer_spacing=0.4,
        )
        nn2.move_to([0,-1.5,0]).scale(1.5)

        self.play(FadeIn(nn), FadeIn(nn2), run_time = 2)

        self.play(
            make_neural_network_dropout_animation(
                nn, dropout_rate=0.25, do_forward_pass=True
            ), 
            make_neural_network_dropout_animation(
                nn2, dropout_rate=0.25, do_forward_pass=True
            ) 
        )
        self.wait(1)

class Time(ThreeDScene):
    def construct(self):

        nn = NeuralNetwork([
        FeedForwardLayer(1),
        FeedForwardLayer(2),
        FeedForwardLayer(4),
        FeedForwardLayer(7),
        FeedForwardLayer(12),
        FeedForwardLayer(18),
        FeedForwardLayer(8), 
        FeedForwardLayer(3)
            ],
            layer_spacing=1,
        )
        nn.move_to(ORIGIN)
        self.add(nn)
        self.play(
            make_neural_network_dropout_animation(
                nn, dropout_rate=0.25, do_forward_pass=True
            )
        )
        self.wait(1)

        time = Tex(r"time").move_to([-2.5, -2.5, 0]).set_color([TEAL_B, PINK, YELLOW]).scale(1.5)

        self.play(DrawBorderThenFill(time), run_time = 1)

        self.wait()

        self.play(FadeOut(time, nn))

        self.wait(4)


class Efficient(ThreeDScene):
    def construct(self): 
        
        axes = ThreeDAxes(
            x_range = (-7, 7, 1), 
            y_range = (-7, 7, 1), 
            z_range = (-7, 7, 1), 
            x_length = 7, 
            y_length = 7, 
            z_length = 7
        )
    
        init = Line(start =  [-3, 0, 0], end = [-2.5, 0, 0])
        ldiag = Line(start =  [-2.5, 0, 0], end = [-2, -0.5, 0])
        lline = Line(start =  [-2, -0.5, 0], end = [-1.5, -0.5, 0])
        mdiag = Line(start =  [-1.5, -0.5, 0], end = [-1, -1, 0])
        rline = Line(start =  [-1, -1, 0], end = [-0.5, -1, 0])
        rdiag = Line(start =  [-0.5, -1, 0], end = [0, -1.5, 0])
        fine = Line(start =  [0, -1.5, 0], end = [0.5, -1.5, 0])
    
        group = VGroup(init, ldiag, lline, mdiag, rline, rdiag, fine).set_color([YELLOW])

        vg = VGroup()

        vg.add(*[Line(start = [-4, i, 0], end = [-3.5, i, 0]) for i in np.arange(-5, 6)])
        vg.add(*[Line(start = [-3.5, i+0.5, 0], end = [-3, i, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vg.add(*[Line(start = [-3, i, 0], end = [-2, i, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vg.add(*[Line(start = [-2, i+0.5, 0], end = [-1.5, i, 0]) for i in np.arange(-6, 5, 1)])
        vg.add(*[Line(start = [-1.5, i, 0], end = [-0.5, i, 0]) for i in np.arange(-6, 5, 1)])
        vg.add(*[Line(start = [-0.5, i+0.5, 0], end = [0, i, 0]) for i in np.arange(-6.5, 4.5, 1)])
        vg.add(*[Line(start = [0, i, 0], end = [0.5, i, 0]) for i in np.arange(-6.5, 4.5, 1)])

        vg.add(*[Line(start = [-4, i, 0], end = [-3.5, i, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vg.add(*[Line(start = [-3.5, i, 0], end = [-3, i+0.5, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vg.add(*[Line(start = [-3, i, 0], end = [-2, i, 0]) for i in np.arange(-5, 6, 1)])
        vg.add(*[Line(start = [-2, i, 0], end = [-1.5, i+0.5, 0]) for i in np.arange(-5, 6, 1)])
        vg.add(*[Line(start = [-1.5, i, 0], end = [-0.5, i, 0]) for i in np.arange(-4.5, 6.5, 1)])
        vg.add(*[Line(start = [-0.5, i, 0], end = [0, i+0.5, 0]) for i in np.arange(-4.5, 6.5, 1)])
        vg.add(*[Line(start = [0, i, 0], end = [0.5, i, 0]) for i in np.arange(-4, 7, 1)])

        
        vg2 = vg.copy()
        vg2.move_to([0, 0, 1])
        vg3 = vg.copy()
        vg3.move_to([0, 0, 2])
        vg4 = vg.copy()
        vg4.move_to([0, 0, 3])
        vg5 = vg.copy()
        vg5.move_to([0, 0, 4])
        vg6 = vg.copy()
        vg6.move_to([0, 0, 5])
        vg7 = vg.copy()
        vg7.move_to([0, 0, 6])

        vgf = VGroup(vg2, vg3, vg4, vg5, vg6, vg7)

        self.play(Create(vgf.shift(3.5*LEFT).scale(0.7).set_color([GRAY_D, GRAY_C])))

        self.play(Rotate(vgf, PI/3, [0, 1, 0]),
        )

        self.remove(vgf)
        
        i = 0
        while i < 5:
            if i % 2 == 0:
                self.play(Write(vgf.set_color([TEAL_B, MAROON_A])), run_time = 2)
                self.remove(vgf)
                i += 1
            else:
                self.play(Write(vgf.set_color([MAROON_A, TEAL_B])), run_time = 2)
                self.remove(vgf)
                i += 1

        self.play(Uncreate(vgf))

        self.wait(2)


class Efficiency(Scene):
    def construct(self):

        vgs1 = VGroup()
        vgld1 = VGroup()
        vgll1 = VGroup()
        vgmd1 = VGroup()
        vgrl1 = VGroup()
        vgrd1 = VGroup()
        vge1 = VGroup()
        vgs2 = VGroup()
        vgld2 = VGroup()
        vgll2 = VGroup()
        vgmd2 = VGroup()
        vgrl2 = VGroup()
        vgrd2 = VGroup()
        vge2 = VGroup()

        vgs1.add(*[Line(start = [-4, i, 0], end = [-3.5, i, 0]) for i in np.arange(-5, 6)])
        vgld1.add(*[Line(start = [-3.5, i+0.5, 0], end = [-3, i, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vgll1.add(*[Line(start = [-3, i, 0], end = [-2, i, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vgmd1.add(*[Line(start = [-2, i+0.5, 0], end = [-1.5, i, 0]) for i in np.arange(-6, 5, 1)])
        vgrl1.add(*[Line(start = [-1.5, i, 0], end = [-0.5, i, 0]) for i in np.arange(-6, 5, 1)])
        vgrd1.add(*[Line(start = [-0.5, i+0.5, 0], end = [0, i, 0]) for i in np.arange(-6.5, 4.5, 1)])
        vge1.add(*[Line(start = [0, i, 0], end = [0.5, i, 0]) for i in np.arange(-6.5, 4.5, 1)])

        vgs2.add(*[Line(start = [-4, i, 0], end = [-3.5, i, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vgld2.add(*[Line(start = [-3.5, i, 0], end = [-3, i+0.5, 0]) for i in np.arange(-5.5, 5.5, 1)])
        vgll2.add(*[Line(start = [-3, i, 0], end = [-2, i, 0]) for i in np.arange(-5, 6, 1)])
        vgmd2.add(*[Line(start = [-2, i, 0], end = [-1.5, i+0.5, 0]) for i in np.arange(-5, 6, 1)])
        vgrl2.add(*[Line(start = [-1.5, i, 0], end = [-0.5, i, 0]) for i in np.arange(-4.5, 6.5, 1)])
        vgrd2.add(*[Line(start = [-0.5, i, 0], end = [0, i+0.5, 0]) for i in np.arange(-4.5, 6.5, 1)])
        vge2.add(*[Line(start = [0, i, 0], end = [0.5, i, 0]) for i in np.arange(-4, 7, 1)])

        vg = VGroup(vgs1, vgld1, vgll1, vgmd1, vgrl1, vgrd1, vge1,
                    vgs2, vgld2, vgll2, vgmd2, vgrl2, vgrd2, vge2
            )

        vdt = VGroup()
        vdb = VGroup()

        vdt.add(*[Dot([-4, i, 0], radius = 0.08, color = TEAL_B) for i in np.arange(-5, 6, 1)])
        vdb.add(*[Dot([-4, i, 0], radius = 0.08, color = MAROON_A) for i in np.arange(-5.5, 5.5, 1)])

        j = 0 
        while j < 5:

            vdt = VGroup()
            vdb = VGroup()

            vdt.add(*[Dot([-4, k, 0], radius = 0.08, color = TEAL_B) for k in np.arange(-5, 6, 1)])
            vdb.add(*[Dot([-4, k, 0], radius = 0.08, color = MAROON_A) for k in np.arange(-5.5, 5.5, 1)])

            vtracedpath = VGroup()
            vtracedpath.add(*[TracedPath(vdt[m].get_center, dissipating_time = 0.05, stroke_opacity = [0, 1]) for m in range(0, 10)])
            vtracedpath.add(*[TracedPath(vdb[m].get_center, dissipating_time = 0.05, stroke_opacity = [0, 1]) for m in range(0, 10)])
            self.add(vtracedpath)

            group = VGroup(vdt.shift(3*LEFT), vdb.shift(3*LEFT))

            for i in range(1, 10): 

                self.play(
                        MoveAlongPath(vdt[i], vgs1[i]), 
                        MoveAlongPath(vdb[i], vgs2[i]),
                        run_time = 0.05, rate_func = rate_functions.ease_in_cubic) 
                self.play(
                        MoveAlongPath(vdt[i], vgld1[i]), 
                        MoveAlongPath(vdb[i], vgld2[i]), 
                        run_time = 0.05, rate_func = rate_functions.ease_in_cubic)
                self.play(
                        MoveAlongPath(vdt[i], vgll1[i]),
                        MoveAlongPath(vdb[i], vgll2[i]),
                        run_time = 0.05, rate_func = rate_functions.ease_in_cubic)
                self.play(
                        MoveAlongPath(vdt[i], vgmd1[i]),
                        MoveAlongPath(vdb[i], vgmd2[i]),
                        run_time = 0.05, rate_func = rate_functions.ease_in_cubic)
                self.play(
                        MoveAlongPath(vdt[i], vgrl1[i]),
                        MoveAlongPath(vdb[i], vgrl2[i]),
                        run_time = 0.05, rate_func = rate_functions.ease_in_cubic)
                self.play(
                        MoveAlongPath(vdt[i], vgrd1[i]),
                        MoveAlongPath(vdb[i], vgrd2[i]),
                        run_time = 0.05, rate_func = rate_functions.ease_in_cubic)
                self.play(
                        MoveAlongPath(vdt[i], vge1[i]),
                        MoveAlongPath(vdb[i], vge2[i]),
                        run_time = 0.05, rate_func = rate_functions.ease_in_cubic)

                self.remove(vdt[i], vdb[i])

            j += 1

        self.play(Write(vg.scale(1.5).shift(LEFT*3).set_color([GRAY_D, GRAY_C])), run_time = 2)
        self.wait(2)
        self.play(FadeOut(vg))

class CubeAlgo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES, theta=-55*DEGREES)

        axes = ThreeDAxes(
            x_range = (-5, 5, 1), 
            y_range = (-5, 5, 1), 
            z_range = (-5, 5, 1), 
            x_length = 5, 
            y_length = 5, 
            z_length = 5
        )

        labels = axes.get_axis_labels(
                Tex("x"), Tex("y"), Tex("z")
                )
        
        cube = Cube(side_length=3, fill_opacity=0.15, stroke_width = 3).set_color([TEAL_B, MAROON_A]).shift(LEFT*4).scale(1.2)
        self.add(cube)
        
        vgs = Line(start =  [-1.5, 0.5, 0], end = [-1.1, 0.5, 0])
        vgld = Line(start =  [-1.1, 0.5, 0], end = [-0.7, 0.25, 0])
        vgll = Line(start =  [-0.7, 0.25, 0], end = [-0.3, 0.25, 0])
        vgmd = Line(start =  [-0.3, 0.25, 0], end = [0.3, -0.25, 0])
        vgrl = Line(start =  [0.3, -0.25, 0], end = [0.7, -0.25, 0])
        vgrd = Line(start =  [0.7, -0.25, 0], end = [1.1, -0.5, 0])
        vge = Line(start =  [1.1, -0.5, 0], end = [1.5, -0.5, 0])

        group = VGroup(vgs, vgld, vgll, vgmd, vgrl, vgrd, vge)

        vgs1 = VGroup()
        vgld1 = VGroup()
        vgll1 = VGroup()
        vgmd1 = VGroup()
        vgrl1 = VGroup()
        vgrd1 = VGroup()
        vge1 = VGroup()

        vgs2 = VGroup()
        vgld2 = VGroup()
        vgll2 = VGroup()
        vgmd2 = VGroup()
        vgrl2 = VGroup()
        vgrd2 = VGroup()
        vge2 = VGroup()
    
        vgs1.add(*[Line([-1.5, i, 0], [-1.1, i, 0]) for i in np.arange(-0.5, 2, 0.5)])
        vgld1.add(*[Line([-1.1, i, 0], [-0.7, i-0.25, 0]) for i in np.arange(-0.5, 2, 0.5)])
        vgll1.add(*[Line([-0.7, i-0.25, 0], [-0.3, i-0.25, 0]) for i in np.arange(-0.5, 2, 0.5)])
        vgmd1.add(*[Line([-0.3, i-0.25, 0], [0.3, i-0.75, 0]) for i in np.arange(-0.5, 2, 0.5)])
        vgrl1.add(*[Line([0.3, i-0.75, 0], [0.7, i-0.75, 0]) for i in np.arange(-0.5, 2, 0.5)])
        vgrd1.add(*[Line([0.7, i-0.75, 0], [1.1, i-1, 0]) for i in np.arange(-0.5, 2, 0.5)])
        vge1.add(*[Line([1.1, i-1, 0], [1.5, i-1, 0]) for i in np.arange(-0.5, 2, 0.5)])

        group1 = VGroup(vgs1, vgld1, vgll1, vgmd1, vgrl1, vgrd1, vge1)

        vgs2.add(*[Line([-1.5, i, 0], [-1.1, i, 0]) for i in np.arange(-1.5, 1, 0.5)])
        vgld2.add(*[Line([-1.1, i, 0], [-0.7, i+0.25, 0]) for i in np.arange(-1.5, 1, 0.5)])
        vgll2.add(*[Line([-0.7, i+0.25, 0], [-0.3, i+0.25, 0]) for i in np.arange(-1.5, 1, 0.5)])
        vgmd2.add(*[Line([-0.3, i+0.25, 0], [0.3, i+0.75, 0]) for i in np.arange(-1.5, 1, 0.5)])
        vgrl2.add(*[Line([0.3, i+0.75, 0], [0.7, i+0.75, 0]) for i in np.arange(-1.5, 1, 0.5)])
        vgrd2.add(*[Line([0.7, i+0.75, 0], [1.1, i+1, 0]) for i in np.arange(-1.5, 1, 0.5)])
        vge2.add(*[Line([1.1, i+1, 0], [1.5, i+1, 0]) for i in np.arange(-1.5, 1, 0.5)])

        group2 = VGroup(vgs2, vgld2, vgll2, vgmd2, vgrl2, vgrd2, vge2)
        """
        
        arr = VGroup()

        arr.add(*[Line([-1.5, i, 0], [-1.1, i, 0]) for i in np.arange(-0.5, 2, 0.5)])
        arr.add(*[Line([-1.1, i, 0], [-0.7, i-0.25, 0]) for i in np.arange(-0.5, 2, 0.5)])
        arr.add(*[Line([-0.7, i-0.25, 0], [-0.3, i-0.25, 0]) for i in np.arange(-0.5, 2, 0.5)])
        arr.add(*[Line([-0.3, i-0.25, 0], [0.3, i-0.75, 0]) for i in np.arange(-0.5, 2, 0.5)])
        arr.add(*[Line([0.3, i-0.75, 0], [0.7, i-0.75, 0]) for i in np.arange(-0.5, 2, 0.5)])
        arr.add(*[Line([0.7, i-0.75, 0], [1.1, i-1, 0]) for i in np.arange(-0.5, 2, 0.5)])
        arr.add(*[Line([1.1, i-1, 0], [1.5, i-1, 0]) for i in np.arange(-0.5, 2, 0.5)])

        arr.add(*[Line([-1.5, i, 0], [-1.1, i, 0]) for i in np.arange(-1.5, 1, 0.5)])
        arr.add(*[Line([-1.1, i, 0], [-0.7, i+0.25, 0]) for i in np.arange(-1.5, 1, 0.5)])
        arr.add(*[Line([-0.7, i+0.25, 0], [-0.3, i+0.25, 0]) for i in np.arange(-1.5, 1, 0.5)])
        arr.add(*[Line([-0.3, i+0.25, 0], [0.3, i+0.75, 0]) for i in np.arange(-1.5, 1, 0.5)])
        arr.add(*[Line([0.3, i+0.75, 0], [0.7, i+0.75, 0]) for i in np.arange(-1.5, 1, 0.5)])
        arr.add(*[Line([0.7, i+0.75, 0], [1.1, i+1, 0]) for i in np.arange(-1.5, 1, 0.5)])
        arr.add(*[Line([1.1, i+1, 0], [1.5, i+1, 0]) for i in np.arange(-1.5, 1, 0.5)])

        arr2 = arr.copy()
        arr2.move_to([0, 0, -1.5])
        arr3 = arr.copy()
        arr3.move_to([0, 0, -1])
        arr4 = arr.copy()
        arr4.move_to([0, 0, -0.5])
        arr5 = arr.copy()
        arr5.move_to([0, 0, 0.5])
        arr6 = arr.copy()
        arr6.move_to([0, 0, 1])
        arr7 = arr.copy()
        arr7.move_to([0, 0, 1.5])

        arrf = VGroup(arr, arr2, arr3, arr4, arr5, arr6, arr7).shift(LEFT*4).scale(1.2)

        """
        groupf11 = group1.copy()
        groupf11.move_to([0, 0, -1.5])
        groupf12 = group1.copy()
        groupf12.move_to([0, 0, -1])
        groupf13 = group1.copy()
        groupf13.move_to([0, 0, -0.5])
        groupf14 = group1.copy()
        groupf14.move_to([0, 0, 0.5])
        groupf15 = group1.copy()
        groupf15.move_to([0, 0, 1])
        groupf16 = group1.copy()
        groupf16.move_to([0, 0, 1.5])

        groupf21 = group2.copy()
        groupf21.move_to([0, 0, -1.5])
        groupf22 = group2.copy()
        groupf22.move_to([0, 0, -1])
        groupf23 = group2.copy()
        groupf23.move_to([0, 0, -0.5])
        groupf24 = group2.copy()
        groupf24.move_to([0, 0, 0.5])
        groupf25 = group2.copy()
        groupf25.move_to([0, 0, 1])
        groupf26 = group2.copy()
        groupf26.move_to([0, 0, 1.5])

        group_final = VGroup(group1, groupf11, groupf12, groupf13, groupf14, groupf15, groupf16, 
                             group2, groupf21, groupf22, groupf23, groupf24, groupf25, groupf26).shift(LEFT*4).scale(1.2)
        
        self.play(Write(cube))
        self.wait()
        self.play(Write(group_final.set_color([GRAY_D, GRAY_C])))

        self.play(Rotate(cube, PI/2, [0,1 ,0]), 
                  Rotate(group_final, PI/2, [0,1,0])
        )
        self.play(Rotate(group_final, PI/2, [1,0,0]), 
                  Rotate(cube, PI/2, [1,0,0])
        )
        
        self.wait(1)
        """
        i = 0
        while i < 5:
            if i % 2 == 0:
                self.play(Write(arrf.set_color([TEAL_B, MAROON_A])), run_time = 2)
                self.remove(arrf)
                i += 1
            else:
                self.play(Write(arrf.set_color([MAROON_A, TEAL_B])), run_time = 2)
                self.remove(arrf)
                i += 1
        """

    
        i = 0
        while i < 20:
            
            self.remove(group_final)

            if i % 2 == 0: 

                VGroup(groupf11, groupf13, groupf14, groupf16, 
                       groupf21, groupf23, groupf24, groupf26
                ).set_color([TEAL_B])

                VGroup(groupf12, group1, groupf15, 
                       groupf22, group2, groupf25
                ).set_color([MAROON_A])

            else: 
                VGroup(groupf11, groupf13, groupf14, groupf16,
                       groupf21, groupf23, groupf24, groupf26
                ).set_color([MAROON_A])

                VGroup(groupf12, group1, groupf15,
                       groupf22, group2, groupf25
                ).set_color([TEAL_B])


                """
                for j in np.arange(0, 6, 2):

                    group_t = VGroup(group1[j],
                                     group2[j],
                                     groupf11[j],
                                     groupf21[j],
                                     groupf12[j],
                                     groupf22[j],
                                     groupf13[j],
                                     groupf23[j],
                                     groupf14[j],
                                     groupf24[j],
                                     groupf15[j],
                                     groupf25[j],
                                     groupf16[j],
                                     groupf26[j]
                                ).set_color([MAROON_B])
                    group_m = VGroup(group1[j+1],
                                     group2[j+1],
                                     groupf11[j+1],
                                     groupf21[j+1],
                                     groupf12[j+1],
                                     groupf22[j+1],
                                     groupf13[j+1],
                                     groupf23[j+1],
                                     groupf14[j+1],
                                     groupf24[j+1],
                                     groupf15[j+1],
                                     groupf25[j+1],
                                     groupf16[j+1],
                                     groupf26[j+1]
                                ).set_color([TEAL_B])
                    group6 = VGroup(group1[6],
                                     group2[6],
                                     groupf11[6],
                                     groupf21[6],
                                     groupf12[6],
                                     groupf22[6],
                                     groupf13[6],
                                     groupf23[6],
                                     groupf14[6],
                                     groupf24[6],
                                     groupf15[6],
                                     groupf25[6],
                                     groupf16[6],
                                     groupf26[6]
                                ).set_color([MAROON_B])
                    """

            self.play(FadeIn(group1[0]), 
                      FadeIn(group2[0]),
                      FadeIn(groupf11[0]),
                      FadeIn(groupf21[0]),
                      FadeIn(groupf12[0]),
                      FadeIn(groupf22[0]),
                      FadeIn(groupf13[0]),
                      FadeIn(groupf23[0]),
                      FadeIn(groupf14[0]),
                      FadeIn(groupf24[0]),
                      FadeIn(groupf15[0]),
                      FadeIn(groupf25[0]),
                      FadeIn(groupf16[0]),
                      FadeIn(groupf26[0]),
                      run_time = 0.1)
            self.play(
                      Write(group1[1]), 
                      Write(group2[1]), 
                      Write(groupf11[1]),
                      Write(groupf21[1]),
                      Write(groupf12[1]),
                      Write(groupf22[1]),
                      Write(groupf13[1]),
                      Write(groupf23[1]),
                      Write(groupf14[1]),
                      Write(groupf24[1]),
                      Write(groupf15[1]),
                      Write(groupf25[1]),
                      Write(groupf16[1]),
                      Write(groupf26[1]),
                      run_time = 0.1)
            self.play(
                      Write(group1[2]),
                      Write(group2[2]),
                      Write(groupf11[2]),
                      Write(groupf21[2]),
                      Write(groupf12[2]),
                      Write(groupf22[2]),
                      Write(groupf13[2]),
                      Write(groupf23[2]),
                      Write(groupf14[2]),
                      Write(groupf24[2]),
                      Write(groupf15[2]),
                      Write(groupf25[2]),
                      Write(groupf16[2]),
                      Write(groupf26[2]),
                      run_time = 0.1)
            self.play(
                      Write(group1[3]),
                      Write(group2[3]),
                      Write(groupf11[3]),
                      Write(groupf21[3]),
                      Write(groupf12[3]),
                      Write(groupf22[3]),
                      Write(groupf13[3]),
                      Write(groupf23[3]),
                      Write(groupf14[3]),
                      Write(groupf24[3]),
                      Write(groupf15[3]),
                      Write(groupf25[3]),
                      Write(groupf16[3]),
                      Write(groupf26[3]),
                      run_time = 0.1),
            self.play(
                      Write(group1[4]),
                      Write(group2[4]),
                      Write(groupf11[4]),
                      Write(groupf21[4]),
                      Write(groupf12[4]),
                      Write(groupf22[4]),
                      Write(groupf13[4]),
                      Write(groupf23[4]),
                      Write(groupf14[4]),
                      Write(groupf24[4]),
                      Write(groupf15[4]),
                      Write(groupf25[4]),
                      Write(groupf16[4]),
                      Write(groupf26[4]),
                      run_time = 0.1)
            self.play(
                      Write(group1[5]),
                      Write(group2[5]),
                      Write(groupf11[5]),
                      Write(groupf21[5]),
                      Write(groupf12[5]),
                      Write(groupf22[5]),
                      Write(groupf13[5]),
                      Write(groupf23[5]),
                      Write(groupf14[5]),
                      Write(groupf24[5]),
                      Write(groupf15[5]),
                      Write(groupf25[5]),
                      Write(groupf16[5]),
                      Write(groupf26[5]),
                      run_time = 0.1)
            self.play(
                      Write(group1[6]),
                      Write(group2[6]),
                      Write(groupf11[6]),
                      Write(groupf21[6]),
                      Write(groupf12[6]),
                      Write(groupf22[6]),
                      Write(groupf13[6]),
                      Write(groupf23[6]),
                      Write(groupf14[6]),
                      Write(groupf24[6]),
                      Write(groupf15[6]),
                      Write(groupf25[6]),
                      Write(groupf16[6]),
                      Write(groupf26[6]),
                      run_time = 0.1
            )
            i += 1
        
        self.play(Unwrite(cube), Unwrite(group_final))
        self.wait()

class QueryModel(Scene):
    def construct(self):
        
        inp = Tex(r" input ").move_to([0, 1.5, 0]).scale(0.7)
        larrow = MathTex(r" \downharpoonleft ").move_to([0, 1, 0])
        rect = Rectangle(height = 1, width = 2.3).set_color([TEAL_B, MAROON_A])
        rarrow = MathTex(r" \downharpoonleft ").move_to([0, -1, 0])
        out = Tex(r" output ").move_to([0, -1.5, 0]).scale(0.7)
        comp = Tex(r" computation ").move_to([0, 0, 0]).scale(0.7)

        trect = Rectangle(height = 1, width = 2.3).set_color([TEAL_B, MAROON_A]).move_to([-1, 1, 0])
        inp2 = Tex(r" input ").move_to([-1, 1, 0]).scale(0.7)
        brect = Rectangle(height = 1, width = 2.3).set_color([TEAL_B, MAROON_A]).move_to([-1, -1, 0])
        comp2 = Tex(r" computation ").move_to([-1, -1, 0]).scale(0.7)

        arr1 = MathTex(r"\upharpoonright").move_to([-2, 0, 0])
        arr2 = MathTex(r"\upharpoonright").move_to([-1.5, 0, 0])
        arr3 = MathTex(r"\upharpoonright").move_to([-0.25, 0, 0])

        cdot = MathTex(r" \cdots").move_to([-0.75, 0, 0]).scale(0.8)

        arr4 = MathTex(r"\downharpoonleft").move_to([-1.75, 0, 0])
        arr5 = MathTex(r"\downharpoonleft").move_to([-1.25, 0, 0])
        arr6 = MathTex(r"\downharpoonleft").move_to([0, 0, 0])

        rarr = MathTex(r"\longrightarrow").move_to([0.5, -1, 0])
        out2 = Tex(r" output ").move_to([1.5, -1, 0]).scale(0.7).set_color([TEAL_B, PINK, YELLOW])

        query = Tex(r" Query Model").move_to([0, 2, 0]).scale(0.7) 

        group1 = VGroup(inp, larrow, rect, rarrow, out, comp).scale(1.25)
        group2 = VGroup(trect, inp2, brect, comp2, arr1, arr2, arr3, cdot, arr4, arr5, arr6, rarr, out2, query).scale(1.25)

        self.play(Write(group1))
        self.wait(5)
        self.play(Unwrite(group1))
        self.wait()

        self.wait()

        self.play(Write(group2))
        self.wait(5)
        self.play(FadeOut(group2))

class QSupreme(ThreeDScene):
    def construct(self):

        nn = NeuralNetwork([
        FeedForwardLayer(1),
        FeedForwardLayer(8)
            ],
            layer_spacing=3,
        )

        nn2 = NeuralNetwork([
            FeedForwardLayer(4), 
            FeedForwardLayer(8)
            ],
            layer_spacing = 3, 
        )

        nn.move_to([0,-1.5, 0])
        nn2.move_to([0, 1.5, 0])
        self.add(nn, nn2)
        self.play(
            make_neural_network_dropout_animation(
                nn, dropout_rate=0.25, do_forward_pass=True
            ),
            make_neural_network_dropout_animation(
                nn2, dropout_rate = 0.25, do_forward_pass = True
            )
        )
        self.wait(1)

        query = Tex(r"Single Query").move_to([0, 0, 0]).set_color([TEAL_B, PINK, YELLOW]).scale(0.9)

        self.play(DrawBorderThenFill(query), run_time = 1)

        self.wait(2)

        self.play(Unwrite(query))

        self.wait(1)


class Binary(Scene):
    def construct(self):

        binary = MathTex(r" \Sigma", r" = \{ 0, \; 1 \}").move_to([0, 1, 0])
        binary[0].set_color([TEAL_B, PINK, YELLOW]).scale(1.1).shift(DOWN*0.05)
        func = MathTex(r" f \, : \, \Sigma^n \rightarrow \Sigma^m")

        self.play(Write(binary)) 
        self.wait(4)
        self.play(Write(func))
        self.wait(2)

        self.play(FadeOut(binary), func.animate.shift(UP*2))

        def_n = Tex(r" if $n = 2$ and $m = 1$,").move_to([-2, 0, 0]).scale(0.8)
        func2 = MathTex(r" f \, : \, \Sigma^2 \rightarrow \Sigma").move_to([0, 2, 0])

        b1 = MathTex(r"01").move_to([-1, -1, 0])
        b1r = SurroundingRectangle(b1).set_color([TEAL_B, MAROON_A])
        b2 = MathTex(r"10").move_to([-1, -1.7, 0])
        b2r = SurroundingRectangle(b2).set_color([TEAL_B, MAROON_A])

        a1 = Line(start =  [-0.6, -1, 0], end = [1.2, -1.4, 0])
        a2 = Line(start =  [-0.6, -1.7, 0], end = [1.2, -1.4, 0])

        fb1 = MathTex(r"0").move_to([1.5, -1.4, 0]).set_color([TEAL_B, PINK, YELLOW])
        fb1r = SurroundingRectangle(fb1).set_color([TEAL_B, PINK, YELLOW])
        fb2 = MathTex(r"1").move_to([1.5, -1.4, 0]).set_color([TEAL_B, PINK, YELLOW])
        fb3 = MathTex(r"0").move_to([1.5, -1.4, 0]).set_color([TEAL_B, PINK, YELLOW])



        self.wait()

        self.play(Write(def_n))
        self.wait(1)
        self.play(Transform(func, func2))
        self.wait(2)
        self.play(Write(b1), Write(b1r), Write(b2), Write(b2r))
        self.wait()
        self.play(Write(a1), Write(a2), Write(fb1), Write(fb1r))
        self.wait()
        self.play(Transform(fb1, fb2))
        self.wait()
        self.play(Transform(fb1, fb3))

        self.wait()

        def_n2 = Tex(r" if $n = 3$ and $m = 1$,").move_to([-2, 0, 0]).scale(0.8)
        func3 = MathTex(r" f \, : \, \Sigma^3 \rightarrow \Sigma").move_to([0, 2, 0])

        b12 = MathTex(r"000").move_to([-1.5, -1, 0])
        b1r2 = SurroundingRectangle(b12).set_color([MAROON_A, TEAL_B])
        b22 = MathTex(r"001").move_to([-1.5, -1.7, 0])
        b2r2 = SurroundingRectangle(b22).set_color([MAROON_A, TEAL_B])

        vdots = MathTex(r"\vdots").move_to([-1.5, -2.5, 0]) 

        a12 = Line(start =  [-0.9, -1, 0], end = [1.1, -1.7, 0])
        a22 = Line(start =  [-0.9, -1.7, 0], end = [1.1, -1.7, 0])
        a32 = Line(start = [-0.9, -2.5, 0], end = [1.1, -1.7, 0 ])

        fb12 = MathTex(r"0").move_to([1.5, -1.7, 0]).set_color([TEAL_B, PINK, YELLOW])
        fb12r = SurroundingRectangle(fb12).set_color([TEAL_B, PINK, YELLOW])
        fb22 = MathTex(r"1").move_to([1.5, -1.7, 0]).set_color([TEAL_B, PINK, YELLOW])
        fb32 = MathTex(r"0").move_to([1.5, -1.7, 0]).set_color([TEAL_B, PINK, YELLOW])

        self.play(Unwrite(b1), 
                  Unwrite(b1r), 
                  Unwrite(b2), 
                  Unwrite(b2r),
                  Unwrite(a1),
                  Unwrite(a2), 
                  Unwrite(fb1), 
                  Unwrite(fb1r)
        )

        self.wait(1)

        self.play(Transform(func, func3), 
                  Transform(def_n, def_n2),
        )

        self.play(Write(b12), 
                  Write(b1r2), 
                  Write(b22), 
                  Write(b2r2), 
                  Write(vdots)
        )

        self.wait()

        self.play(Write(a12), 
                  Write(a22), 
                  Write(a32), 
                  Write(fb12), 
                  Write(fb12r)
        )

        self.wait()

        self.play(Transform(fb12, fb22))
        self.wait()
        self.play(Transform(fb12, fb32))

        self.wait()

        self.play(Unwrite(VGroup(func, def_n, b12, b1r2, b22, b2r2, vdots, a12, a22, a32, fb12, fb12r)))

        self.wait()

class Examples(Scene):
    def construct(self):
        
        title = Tex(r"OR").to_edge(UL).set_color([TEAL_B, MAROON_A])

        func = MathTex(r" f \, : \, \Sigma^n \rightarrow \Sigma").move_to([0, 2, 0])

        if1 = MathTex(r" \text{If } \exists \, x \in \Sigma^n \, : \,", r"f(x) = 1,").move_to([-2, 0.5, 0])
        if1[1].set_color([YELLOW])
        if2 = MathTex(r" \text{If }", r"\nexists", r"\, x \in \Sigma^n \, : \,", r"f(x) = 1,").move_to([-2, 0.5, 0])
        if2[3].set_color([YELLOW])
        if2[1].set_color([TEAL_B, MAROON_A])


        sigma_n = MathTex(r" \Sigma^n ").move_to([-1.5, -1, 0])
        sigma_nrect = SurroundingRectangle(sigma_n).set_color([WHITE])

        f = MathTex(r"f").set_color([TEAL_B, MAROON_A]).move_to([0, -1, 0])
        frect = SurroundingRectangle(f).set_color([MAROON_A, TEAL_B])

        arr1 = MathTex(r" \rightarrow ").move_to([-0.75, -1, 0])
        arr2 = MathTex(r" \rightarrow ").move_to([0.9, -1, 0])

        out1 = MathTex(r"1").set_color([TEAL_B, PINK, YELLOW]).move_to([1.5, -1, 0])
        out1rect = SurroundingRectangle(out1).set_color([TEAL_B, PINK, YELLOW])

        out2 = MathTex(r"0").set_color([TEAL_B, PINK, YELLOW]).move_to([1.5, -1, 0])

        VGroup(sigma_n, f, out1, out2, sigma_nrect, frect, out1rect).scale(1.2)

        self.play(Write(title))
        self.wait(1)

        self.play(Write(func), run_time = 2)

        self.wait(2)

        self.play(Write(if1))

        self.wait(1)

        self.play(Write(sigma_n), Write(sigma_nrect), Write(f), Write(frect), 
                  Write(arr1), Write(arr2), Write(out1), Write(out1rect), run_time = 2
        )

        self.wait(4)

        self.play(ReplacementTransform(if1, if2)
        ) 
        self.wait()
        self.play(Transform(out1, out2)
        )

        self.wait(4)

        self.play(FadeOut(VGroup(sigma_n, sigma_nrect, f, frect,
                                 arr1, arr2, out1, out1rect, 
                                 if2, func, title))
        )
        self.wait()

        title = Tex(r"XOR / Parity").to_edge(UL).set_color([TEAL_B, MAROON_A])

        func = MathTex(r" f \, : \, \Sigma^n \rightarrow \Sigma").move_to([0, 2, 0])

        if1 = MathTex(r" \text{If } \# \, x \in \Sigma^n \, : \, f(x) = 1 ", r"\text{ is even,}").move_to([-2, 0.5, 0])
        if1[1].set_color([YELLOW])
        if2 = MathTex(r" \text{If } \# \, x \in \Sigma^n \, : \, f(x) = 1 ", r"\text{ is odd,}").move_to([-2, 0.5, 0])
        if2[1].set_color([YELLOW])


        sigma_n = MathTex(r" \Sigma^n ").move_to([-1.5, -1, 0])
        sigma_nrect = SurroundingRectangle(sigma_n).set_color([WHITE])

        f = MathTex(r"f").set_color([TEAL_B, MAROON_A]).move_to([0, -1, 0])
        frect = SurroundingRectangle(f).set_color([MAROON_A, TEAL_B])

        arr1 = MathTex(r" \rightarrow ").move_to([-0.75, -1, 0])
        arr2 = MathTex(r" \rightarrow ").move_to([0.9, -1, 0])

        out1 = MathTex(r"0").set_color([TEAL_B, PINK, YELLOW]).move_to([1.5, -1, 0])
        out1rect = SurroundingRectangle(out1).set_color([TEAL_B, PINK, YELLOW])

        out2 = MathTex(r"1").set_color([TEAL_B, PINK, YELLOW]).move_to([1.5, -1, 0])

        VGroup(sigma_n, f, out1, out2, sigma_nrect, frect, out1rect).scale(1.2)

        self.wait()
        self.play(Write(title))
        self.wait(1)

        self.play(Write(func), run_time = 2)

        self.wait(2)

        self.play(Write(if1))

        self.wait(1)

        self.play(Write(sigma_n), Write(sigma_nrect), Write(f), Write(frect),
                  Write(arr1), Write(arr2), Write(out1), Write(out1rect), run_time = 2
        )

        self.wait(4)

        self.play(ReplacementTransform(if1, if2)
        )
        self.wait()
        self.play(Transform(out1, out2)
        )

        self.wait(4)

        self.play(Unwrite(VGroup(sigma_n, sigma_nrect, f, frect,
                                 arr1, arr2, out1, out1rect,
                                 if2, func, title))
        )
        self.wait()


class Queries(ThreeDScene):
    def construct(self): 

        axes = ThreeDAxes(
            x_range = (-10, 10, 1), 
            y_range = (-10, 10, 1), 
            z_range = (-10, 10, 1), 
            x_length = 10, 
            y_length = 10, 
            z_length = 10
        )

        labels = axes.get_axis_labels(Tex("x"), Tex("y"), Tex("z"))
        
        self.set_camera_orientation(
            phi = 75*DEGREES,
            theta = 45*DEGREES, 
            distance = 3
        )
    
        dots = VGroup()
        dots1 = VGroup()
        dots2 = VGroup()
        dots3 = VGroup()
        dots4 = VGroup()
        dots5 = VGroup()
        dots6 = VGroup()
        dots7 = VGroup()


        dots.add(*[Dot3D([5, i, -3], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots.set_color([TEAL_B, MAROON_A])
        dots1.add(*[Dot3D([5, i, -2], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots1.set_color([TEAL_B, MAROON_A])
        dots2.add(*[Dot3D([5, i, -1], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots2.set_color([TEAL_B, MAROON_A])
        dots3.add(*[Dot3D([5, i, 0], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots3.set_color([TEAL_B, MAROON_A])
        dots4.add(*[Dot3D([5, i, 1], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots4.set_color([TEAL_B, MAROON_A])
        dots5.add(*[Dot3D([5, i, 2], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots5.set_color([TEAL_B, MAROON_A])
        dots6.add(*[Dot3D([5, i, 3], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots6.set_color([TEAL_B, MAROON_A])
        dots7.add(*[Dot3D([5, i, 4], radius = 0.15, resolution = (3,3), fill_opacity = 0.02) for i in range(5, -5, -1)])
        dots7.set_color([TEAL_B, MAROON_A])


        self.begin_ambient_camera_rotation(rate = 0.2)

        self.play(Write((VGroup(dots, dots1, dots2, dots3, dots4, dots5, dots6, dots7))), run_time = 2)
        self.wait(4)
    
        cube = Cube(side_length = 2, fill_opacity = 0.15, stroke_width = 3).set_color([TEAL_B, MAROON_A])
        cube2 = Cube(side_length = 2, fill_opacity = 0.15, stroke_width = 3).set_color([TEAL_B, MAROON_A])

        self.play(Write(cube))
        
        self.wait(4)

        
        middot = Surface(
            lambda u, v: np.array([
            0.5 * np.cos(u) * np.cos(v),
            0.5 * np.cos(u) * np.sin(v),
            0.5 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[TEAL_B, MAROON_A], resolution=(3, 6), fill_opacity = 0.01
        ).move_to([0, 0, 0])
        
    
    
        for i in dots: 
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)
        for i in dots1:
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)
        for i in dots2:
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)
        for i in dots3:
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)
        for i in dots4:
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)
        for i in dots5:
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)
        for i in dots6:
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)
        for i in dots7:
            self.play(Transform(i, middot), run_time = 0.1)
            self.wait(0.1)

        cubef = Cube(side_length = 1, fill_opacity = 0.15, 
                     stroke_width = 3).set_color([PINK, YELLOW]).move_to([-5, 0, 0])

        enddot = Surface(
            lambda u, v: np.array([
            0.25 * np.cos(u) * np.cos(v),
            0.25 * np.cos(u) * np.sin(v),
            0.25 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[PINK, YELLOW], resolution=(3, 6), fill_opacity = 0.01
        ).move_to([-5, 0, 0])

        line1 = Line3D([-1,1,1], [-4.5, 0.5, 0.5]).set_color([TEAL_B, MAROON_A])
        line2 = Line3D([-1,-1,1], [-4.5, -0.5, 0.5]).set_color([TEAL_B, MAROON_A])
        line3 = Line3D([-1, 1, -1], [-4.5, 0.5, -0.5]).set_color([TEAL_B, MAROON_A])
        line4 = Line3D([-1, -1, -1], [-4.5, -0.5, -0.5]).set_color([TEAL_B, MAROON_A])

        self.wait(2)

        self.play(Write(VGroup(line1, line2, line3, line4)), Transform(middot, enddot), ReplacementTransform(cube2, cubef), run_time = 3)

        self.wait(8)

        self.play(Unwrite(VGroup(line1, line2, line3, line4, middot, enddot, cubef, cube)), run_time =  2)

        self.wait()

        self.stop_ambient_camera_rotation()
        

class UnitaryGates(Scene):
    def construct(self):
        
        x = MathTex(r"|x\rangle").move_to([-3.5, 1.5, 0]).scale(1.2)
        x2 = MathTex(r"|x\rangle").move_to([3.65, 1.5, 0]).scale(1.2)
        y = MathTex(r"|y\rangle").move_to([-3.5, -1.5, 0]).scale(1.2) 
        y2 = MathTex(r"|y \oplus f(x) \rangle").move_to([4.55, -1.5, 0]).scale(1.2)
        Uf = MathTex(r"U_f").scale(1.2)
        rect = Rectangle(height = 5, width = 3, fill_opacity = 0.4, stroke_width = 3).set_color([TEAL_B, MAROON_A])

        line1 = Line([-3, 1.6, 0], [-1.5, 1.6, 0])
        line2 = Line([-3, 1.4, 0], [-1.5, 1.4, 0])
        line3 = Line([-3, -1.6, 0], [-1.5, -1.6, 0])
        line4 = Line([-3, -1.4, 0], [-1.5, -1.4, 0])

        lines1 = VGroup(line1, line2, line3, line4)

        line11 = Line([1.5, 1.6, 0], [3.1, 1.6, 0])
        line22 = Line([1.5, 1.4, 0], [3.1, 1.4, 0])
        line33 = Line([1.5, -1.6, 0], [3.1, -1.6, 0])
        line44 = Line([1.5, -1.4, 0], [3.1, -1.4, 0])

        lines2 = VGroup(line11, line22, line33, line44)

        groupf = VGroup(x, x2, y, y2, Uf, rect, lines1, lines2)
        gate = groupf.copy().move_to([0, 1, 0]).scale(0.8)

        self.play(Write(VGroup(x, y, rect, x2, y2, lines1, lines2)), run_time = 2)

        xyin = MathTex(r" x \in \Sigma^n \quad \Big| \quad y \in \Sigma^m").move_to([0, -2, 0])
        xor = MathTex(r" \text{XOR : } y \oplus f(x)").move_to([0, -3, 0])
        xorex = MathTex(r" 001 \oplus 101 = 100").move_to([0, -3, 0])

        self.wait(4)
        self.play(Write(Uf))

        srect = SurroundingRectangle(gate).set_color([TEAL_B, MAROON_A])

        self.wait(6)
        self.play(ReplacementTransform(groupf, gate), Write(srect))

        self.wait(1)

        self.play(Write(xyin))
        self.wait()
        self.play(Write(xor))
        self.wait(3)
        self.play(Transform(xor, xorex))
        self.wait(4) 

        self.play(Unwrite(VGroup(gate, xyin, xor, xorex, srect)))
        self.wait()


class Deutsch(Scene):
    def construct(self):

        func = MathTex(r" f \, : \, \Sigma^n \rightarrow \Sigma^ ").move_to([0, 2, 0])
        func2 = MathTex(r" f \, : \, \Sigma \rightarrow \Sigma").move_to([0, 2, 0])
        one2one = Tex(r" $f \, : \,$ 1 bit $\rightarrow$ 1 bit ").move_to([0, 2, 0])

        self.play(Write(func))
        self.wait(2)
        self.play(Transform(func, func2))
        self.wait(2)
        self.play(Transform(func, one2one))

        self.wait(3)

        a2 = MathTex(r"a").scale(0.8).move_to([-1.2, 1, 0])
        
        a3 = a2.copy().move_to([0.8, 1, 0])
        a4 = a2.copy().move_to([2.8, 1, 0])
        a1 = a2.copy().move_to([-3.2, 1, 0])

        f2 = MathTex(r"f_2(a)").scale(0.8).move_to([-0.3, 1, 0])
        f3 = MathTex(r"f_3(a)").scale(0.8).move_to([1.7, 1, 0])
        f4 = MathTex(r"f_4(a)").scale(0.8).move_to([3.7, 1, 0])
        f1 = MathTex(r"f_1(a)").scale(0.8).move_to([-2.3, 1, 0])

        zero = MathTex(r"0").scale(0.8).move_to([-3.2, 0.25, 0])
        one = MathTex(r"1").scale(0.8).move_to([-3.2, -0.25, 0])

        zero2 = zero.copy().shift(RIGHT*2)
        zero3 = zero.copy().shift(RIGHT*4)
        zero4 = zero.copy().shift(RIGHT*6)

        one2 = one.copy().shift(RIGHT*2)
        one3 = one.copy().shift(RIGHT*4)
        one4 = one.copy().shift(RIGHT*6)

        num = VGroup(one, one2, one3, one4, zero, zero2, zero3, zero4)

        lineh1 = Line([-3.5, 0.7, 0], [-1.7, 0.7, 0]).set_color([TEAL_B, MAROON_A])
        lineh2 = lineh1.copy().shift(RIGHT*2)
        lineh3 = lineh1.copy().shift(RIGHT*4)
        lineh4 = lineh1.copy().shift(RIGHT*6)

        linev1 = Line([-2.9, 1.3, 0], [-2.9, -0.7, 0]).set_color([MAROON_A, TEAL_B])
        linev2 = linev1.copy().shift(RIGHT*2)
        linev3 = linev1.copy().shift(RIGHT*4)
        linev4 = linev1.copy().shift(RIGHT*6)

        af = VGroup(a1, a2, a3, a4, f1, f2, f3, f4)

        lineh = VGroup(lineh1, lineh2, lineh3, lineh4)
        linev = VGroup(linev1, linev2, linev3, linev4)

        zer1 = zero.copy().move_to([-2.3, 0.25, 0])
        zer2 = zer1.copy().shift(RIGHT*2)
        zer3 = zer1.copy().shift(DOWN*0.5)
        zer4 = zer3.copy().shift(RIGHT*4)

        on1 = one.copy().move_to([-0.3, -0.25, 0])
        on2 = on1.copy().shift(RIGHT*4)
        on3 = one.copy().move_to([1.7, 0.25, 0])
        on4 = on3.copy().shift(RIGHT*2)

        onzer = VGroup(zer1, zer2, zer3, zer4, on1, on2, on3, on4)

        group = VGroup(af, lineh, linev, num, onzer)

        p1 = VGroup(zer1, zer3)
        p2 = VGroup(zer2, on1)
        p3 = VGroup(on3, zer4)
        p4 = VGroup(on4, on2)

        p1r = SurroundingRectangle(p1).set_color([TEAL_B, MAROON_A])
        p2r = SurroundingRectangle(p2).set_color([TEAL_B, MAROON_A])
        p3r = SurroundingRectangle(p3).set_color([TEAL_B, MAROON_A])
        p4r = SurroundingRectangle(p4).set_color([TEAL_B, MAROON_A])

        rects = VGroup(p1r, p2r, p3r, p4r) 
        groupf = VGroup(group, rects).move_to([0, -0.5, 0]).scale(1.2)

        self.play(Write(groupf), run_time = 2)

        g1 = VGroup(a1, f1)
        g2 = VGroup(a2, f2) 
        g3 = VGroup(a3, f3)
        g4 = VGroup(a4, f4)

        b1 = Brace(g1)
        b23 = Brace(VGroup(g2, g3))
        b4 = Brace(g4)

        self.wait(5)

        self.play(Write(VGroup(b1, b23, b4).shift(DOWN*1.7)))

        constant = MathTex(r"\textit{constant}").move_to([-3.55, -1.8, 0]).scale(0.9)
        constant2 = constant.copy().shift(RIGHT*7.2)
        balanced = MathTex(r"\textit{balanced}").move_to([0, -1.8, 0]).scale(0.9)

        conbal = VGroup(constant, constant2, balanced).shift(DOWN*0.5)


        self.play(Write(constant), Write(constant2), Write(balanced))

        self.wait(5)

        self.play(Unwrite(VGroup(groupf, b1, b23, b4, constant, constant2, balanced, func)))

        self.wait()


class DeutschProb(Scene):
    def construct(self):

        vline = Line(start =  [-1, -1, 0], end = [-1, 1, 0]).set_color([TEAL_B, MAROON_A])

        problem = Tex(r"\textbf{Deutsch's Problem}").move_to([1.05, 0.6, 0]).scale(0.8)
        inp = Tex(r" Input: a function $f \, : \, \{0, 1\} \rightarrow \{0, 1\}$").move_to([2.4, 0, 0]).scale(0.8)
        out = Tex(r" Output: 0 if $f$ is constant, 1 if $f$ is balanced").move_to([3.05, -0.6, 0]).scale(0.8)

        prob = VGroup(vline, problem, inp, out).move_to([0, 0, 0])

        self.play(Write(vline))
        self.wait()
        self.play(Write(problem))
        self.wait(1)
        self.play(Write(inp))
        self.wait(2)
        self.play(Write(out))

        self.wait(4)

        self.play(prob.animate.shift(UL*2))

        rect = SurroundingRectangle(prob).set_color([TEAL_B, MAROON_A])

        self.play(Write(rect))

        self.wait()

        func = Tex("function").scale(0.7).move_to([-1.5, 0.3, 0])
        inp = Tex(r"`$f(0)f(1)$'").scale(0.7).move_to([0.5, 0.3, 0])
        out = Tex("output").scale(0.7).move_to([2.5, 0.3, 0])
        hline = Line([-2.5, 0, 0], [3.6, 0, 0]).set_color([TEAL_B, MAROON_A])
        f1 = MathTex(r"f_1").move_to([-1.5, -0.5, 0])
        f2 = MathTex(r"f_2").move_to([-1.5, -1.1, 0])
        f3 = MathTex(r"f_3").move_to([-1.5, -1.7, 0])
        f4 = MathTex(r"f_4").move_to([-1.5, -2.3, 0])

        f = VGroup(f1, f2, f3, f4)

        str1 = Tex(r"`$00$'").move_to([0.5, -0.5, 0])
        str2 = Tex(r"`$01$'").move_to([0.5, -1.1, 0])
        str3 = Tex(r"`$10$'").move_to([0.5, -1.7, 0])
        str4 = Tex(r"`$11$'").move_to([0.5, -2.3, 0])

        string = VGroup(str1, str2, str3, str4)

        out0 = MathTex(r"0").move_to([2.5, -0.5, 0])
        out01 = out0.copy().move_to([2.5, -2.3, 0])
        out1 = MathTex(r"1").move_to([2.5, -1.1, 0])
        out11 = out1.copy().move_to([2.5, -1.7, 0])

        ans = VGroup(out0, out01, out1, out11).set_color([TEAL_B, MAROON_A]) 



        VGroup(func, inp, out, hline, f, string, ans).move_to([0, -1.5, 0])

        self.play(Write(VGroup(func, inp, out, hline)))
        self.wait(2)

        self.play(Write(f), Write(string))
        self.wait(2)

        self.play(Write(ans))

        self.wait(3)

        funcdef = VGroup(f, string, ans, func, inp, out, hline)

        self.play(funcdef.animate.shift(LEFT*2.9))
        rect2 = SurroundingRectangle(funcdef).set_color([TEAL_B, MAROON_A])
        self.play(Write(rect2))

        xor = MathTex(r" f(0) \oplus f(1)").move_to([3.9, -1.5, 0])
        xor2 = Tex(r" XOR ").move_to([3.93, -0.8, 0])

        xors = VGroup(xor, xor2)
        xorrect = SurroundingRectangle(xors).set_color([TEAL_B, MAROON_A])

        xorsf = VGroup(xors, xorrect).shift(LEFT*0.5)
        xorsf.shift(DOWN*0.3)

        self.wait(2)

        self.play(Write(xors), Write(xorrect))

        self.wait(5)

        self.play(Unwrite(VGroup(xors, xorrect, rect2, funcdef, func, inp, out, hline, prob, rect)))
        self.wait()


class DeutschAlgo(Scene):
    def construct(self):

        zero = MathTex(r" | 0 \rangle ").move_to([-5, 2, 0])
        one = MathTex(r" | 1 \rangle ").move_to([-5, -2, 0])

        Hi1 = MathTex(r" H ").move_to([-3, 2, 0])
        Hi1sq = Square(side_length = 1, fill_opacity = 0.2).set_color([TEAL_B, MAROON_A]).move_to([-3, 2, 0])
        Hi2 = Hi1.copy().shift(DOWN*4)
        Hi2sq = Hi1sq.copy().shift(DOWN*4)
        Hio = Hi1.copy().shift(RIGHT*6)
        Hiosq = Hi1sq.copy().shift(RIGHT*6)
        Uf = MathTex(r" U_f ")
        Ufrect = Rectangle(width = 3, height = 5.5, fill_opacity = 0.2).set_color([TEAL_B, PINK, YELLOW])


        semicirc = Arc(fill_opacity=0, angle=PI, stroke_width = 3).move_to([5, 2, 0]).scale(0.3)
        semicircsq = Hi1sq.copy().shift(RIGHT*8).set_color([PINK, YELLOW])
        dot = Dot([5,1.84,0], radius = 0.05)
        line = Line([5, 1.84, 0], [5.3, 2.14, 0])

        group = VGroup(zero, one, Hi1, Hi1sq, 
                       Hi2, Hi2sq, Hio, Hiosq, Uf, Ufrect, semicirc,
                       semicircsq, dot, line
        )

        hi1uf = Line(start =  [-2.5, 2, 0], end = [-1.5, 2, 0])
        ufhio = hi1uf.copy().shift(RIGHT*4)
        hi2uf = hi1uf.copy().shift(DOWN*4)
        hiom = hi1uf.copy().shift(RIGHT*6)
        zeroh = Line(start =  [-4.5, 2, 0], end = [-3.5, 2, 0])
        oneh = zeroh.copy().shift(DOWN*4)
        ufend = Line(start =  [1.5, -2, 0], end = [6.2, -2, 0])
        mend1 = Line(start = [5.5, 2.1, 0], end = [6.2, 2.1, 0])
        mend2 = mend1.copy().shift(DOWN*0.2)

        lines = VGroup(hi1uf, ufhio, hi2uf, hiom, zeroh, oneh, ufend, mend1, mend2)

        zer = MathTex(r"0").move_to([6.6, 2.3, 0])
        on = MathTex(r"1").move_to([6.6, 1.8, 0])

        pi1line = DashedLine([-2, 2.75, 0], [-2, -2.75, 0])
        pi1 = MathTex(r" | \pi_1 \rangle").move_to([-2, -3.2, 0])
        pi2line = DashedLine([2, 2.75, 0], [2, -2.75, 0])
        pi2 = MathTex(r" | \pi_2 \rangle").move_to([2, -3.2, 0])
        pi3line = DashedLine([4, 2.75, 0], [4, -2.75, 0])
        pi3 = MathTex(r" | \pi_3 \rangle").move_to([4, -3.2, 0])

        pis = VGroup(pi1line, pi1, pi2line, pi2, pi3line, pi3)

        rectangle = SurroundingRectangle(VGroup(zer, on)).set_color([TEAL_B, MAROON_A])

        groupf = VGroup(lines, group, zer, on, rectangle).move_to([0, 0, 0])
        groupff = VGroup(lines, group, zer, on, rectangle, pis).move_to([0, 0, 0])

        self.play(Write(group), run_time = 5)
        self.play(Write(lines), Write(zer), Write(on), Write(rectangle))
        self.wait(4)

        self.play(Write(pis.shift(LEFT*0.8)))
        self.wait(4)
        self.play(Unwrite(VGroup(pi2line, pi2, pi3line, pi3, Uf, Ufrect, Hio,
                                 Hiosq, semicirc, semicircsq, dot, line, zer,
                                 on, rectangle, mend1, mend2, ufend, ufhio, hiom)), run_time = 2)

        self.wait(2)
        
        hmatrixt = MathTex(r" \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \
                          \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{pmatrix} ").move_to([-0.5, 2.3, 0])

        hmatrixb = hmatrixt.copy().shift(DOWN*4)

        matrix0 = MathTex(r" \begin{pmatrix} 1 \\[6px] 0 \end{pmatrix} ").move_to([-6, 2.3, 0])
        matrix1 = MathTex(r" \begin{pmatrix} 0 \\[6px] 1 \end{pmatrix} ").move_to([-6, -1.7, 0])

        line1copy = VGroup(zeroh.copy(), oneh.copy(), hi1uf.copy(), hi2uf.copy())

        self.play(Write(line1copy))

        matrix01 = matrix0.copy().shift(RIGHT*7.5)
        matrix11 = matrix1.copy().shift(RIGHT*7.5)
        
        self.wait()

        self.play(Transform(zero, matrix0), Transform(one, matrix1))

        self.wait()
        self.play(Write(VGroup(hmatrixt, hmatrixb, matrix01, matrix11)))
        self.wait()

        h0out = MathTex(r" \begin{pmatrix} \frac{1}{\sqrt{2}} \\[6px] \frac{1}{\sqrt{2}} \end{pmatrix} ").move_to([-1.1, 2.3, 0])
        h1out = MathTex(r" \begin{pmatrix} \frac{1}{\sqrt{2}} \\[6px] -\frac{1}{\sqrt{2}} \end{pmatrix} ").move_to([-1.1, -1.7, 0])

        h0out1 = MathTex(r" \frac{ |0\rangle + |1\rangle }{\sqrt{2}} ").move_to([-1.1, 2.3, 0]).set_color([TEAL_B, PINK, YELLOW])
        h1out1 = MathTex(r" \frac{ |0\rangle - |1\rangle }{\sqrt{2}} ").move_to([-1.1, -1.7, 0]).set_color([TEAL_B, PINK, YELLOW])

        self.wait(2)
        self.play(ReplacementTransform(VGroup(hmatrixt, matrix01), h0out), ReplacementTransform(VGroup(hmatrixb, matrix11), h1out))

        self.wait(2)

        inzero = MathTex(r" |0 \rangle ").move_to([-5.9, 2.35, 0])
        inone = MathTex(r" |1 \rangle ").move_to([-5.9, -1.65, 0])

        self.play(Transform(h0out, h0out1), Transform(h1out, h1out1),
                  run_time = 1
        )

        self.wait()
        
        self.play(Transform(zero, inzero), Transform(one, inone))

        self.wait(2)

        grouph1 = VGroup(zero, one, h0out, h1out, zeroh, oneh, hi1uf, hi2uf, line1copy, pi1, pi1line, Hi1, Hi1sq, Hi2, Hi2sq)

        self.play(grouph1.animate.scale(0.8).to_edge(LEFT))

        vline = Line(start =  [-1, 10, 0], end = [-1, -10, 0])
        self.play(Write(vline))


        self.wait(70)

        self.play(vline.animate.shift(RIGHT*0.3), grouph1.animate.scale(1.2).to_edge(LEFT))


        pi1form = MathTex(r" | - \rangle | + \rangle").move_to([-3.4, -2.8, 0]).scale(0.8)

        h1outminus = MathTex(r" | -\rangle").set_color([MAROON_A]).move_to([-2.3, -1.57, 0])
        h0outplus  = MathTex(r" | + \rangle").set_color([TEAL_B]).move_to([-2.3, 2.25, 0])

        self.wait(2)
 
        self.play(ReplacementTransform(h1out, h1outminus), ReplacementTransform(h0out, h0outplus))
        self.wait()
        
        self.play(Transform(pi1, pi1form))

        pi1form1 = MathTex(r" \frac{1}{2} (", r"|0\rangle", r"-", r"|1\rangle", r") |0\rangle + \frac{1}{2}(", r"|0\rangle", r"-", r"|1\rangle", r")|1\rangle").move_to([-3.7, -3, 0]).scale(0.8)


        pi2form1 = MathTex(r" |\pi_2\rangle = \frac{1}{2} (", r"|0 \oplus f(0) \rangle", r"-", r"|1 \oplus f(0) \rangle", r") |0\rangle \\ + \frac{1}{2}(", r"|0\oplus f(1) \rangle", r"-", r"|1 \oplus f(1) \rangle", r")|1\rangle")

        pi2form1[1].set_color([TEAL_B])
        pi2form1[3].set_color([MAROON_A])
        pi2form1[5].set_color([TEAL_B])
        pi2form1[7].set_color([MAROON_A])

        self.wait(3)

        self.play(ReplacementTransform(pi1, pi1form1))

        self.wait(2)

        pi1corner = MathTex(r" |\pi_1 \rangle = \frac{1}{2} (", r"|0\rangle", r"-", r"|1\rangle", r") |0\rangle \\ + \frac{1}{2}(", r"|0\rangle", r"-", r"|1\rangle", r")|1\rangle").scale(0.8).move_to([1.27, 2.3, 0])

        pi1corner[1].set_color([TEAL_B])
        pi1corner[3].set_color([MAROON_A])
        pi1corner[5].set_color([TEAL_B])
        pi1corner[7].set_color([MAROON_A])
        
        self.play(ReplacementTransform(pi1form1, pi1corner))

        self.wait(2)

        self.play(Unwrite(VGroup(zero, one, zeroh, oneh, hi1uf, hi2uf, line1copy, pi1line, Hi1, Hi1sq, Hi2, Hi2sq)), 
                  h1outminus.animate.shift(LEFT*3.5), h0outplus.animate.shift(LEFT*3.5))

        self.wait(2)
        
        Uf = MathTex(r" U_f").move_to([-3.5, 0, 0])
        Ufrect = Rectangle(height = 5.5, width = 2.3, fill_opacity = 0.2).set_color([TEAL_B, PINK, YELLOW]).move_to([-3.5, 0, 0])

        puf = Line(start =  [-5.3, 2.25, 0], end = [-4.65, 2.25, 0])
        muf = Line(start =  [-5.3, -1.57, 0], end = [-4.65, -1.57, 0])

        ufpi2t = Line(start =  [-2.35, 2.25, 0], end = [-1.15, 2.25, 0])
        ufpi2b = Line(start = [-2.35, -1.57, 0], end = [-1.15, -1.57, 0])

        pi2line = DashedLine([-1.75, 2.75, 0], [-1.75, -2.75, 0])
        pi2 = MathTex(r" | \pi_2 \rangle").move_to([-1.75, -3.2, 0])

        self.play(Write(VGroup(Uf, Ufrect, puf, muf, ufpi2t, ufpi2b, pi2line, pi2)), run_time = 3)

        self.wait(5)

        self.play(Write(pi2form1.move_to([2.6, 0, 0]).scale(0.8)))

        pi2form2 = MathTex(r" |\pi_2\rangle = |-\rangle \left( \frac{(-1)^{f(0)} |0\rangle + (-1)^{f(1)}|1\rangle}{\sqrt{2}} \right) ").move_to([2.82, 0, 0]).scale(0.8)

        self.wait(5)

        self.play(ReplacementTransform(pi2form1, pi2form2))

        phase = Tex(r" \textit{phase kickback} ").move_to([3, -2, 0]).set_color([TEAL_B, MAROON_A])

        self.wait(8)

        self.play(Write(phase))

        pi2form3 = MathTex(r" |\pi_2\rangle &= (-1)^{f(0)}|-\rangle \left( \frac{|0\rangle + (-1)^{f(0)\oplus f(1)} |1\rangle}{\sqrt{2}}\right) ").move_to([3.17, 0, 0]).scale(0.8)


        pi2form4 = MathTex(r" |\pi_2\rangle &= (-1)^{f(0)}|-\rangle \left( \frac{|0\rangle + (-1)^{f(0)\oplus f(1)} |1\rangle}{\sqrt{2}}\right) \\ &=  \left\{ \begin{array}{ll} \hspace{-2mm} (-1)^{f(0)} |-\rangle |+\rangle \; \text{ if } f(0) \oplus f(1) = 0 \\ \hspace{-2mm} (-1)^{f(0)} |-\rangle|-\rangle \; \text{ if } f(0) \oplus f(1) = 1 \end{array} \right. ").move_to([3.19, 0, 0]).scale(0.8)
        """
        pi2form4[1].set_color([TEAL_B])
        pi2form4[2].set_color([MAROON_A])
        pi2form4[4].set_color([TEAL_B])
        pi2form4[5].set_color([MAROON_A])
        """

        pi2form5 = MathTex(r" |\pi_2\rangle = \left\{ \begin{array}{ll} \hspace{-2mm} (-1)^{f(0)} |-\rangle |+\rangle \; \text{ if } f(0) \oplus f(1) = 0 \\ \hspace{-2mm} (-1)^{f(0)} |-\rangle|-\rangle \; \text{ if } f(0) \oplus f(1) = 1 \end{array} \right. ").move_to([3.15, 0.3, 0]).scale(0.8)

        self.wait(2)
        self.play(Unwrite(phase))

        self.wait(2)

        self.play(ReplacementTransform(pi2form2, pi2form3)) 

        self.wait(4)

        self.play(ReplacementTransform(pi2form3, pi2form4))

        self.wait(2)

        self.play(ReplacementTransform(pi2form4, pi2form5))

        self.wait(4)

        pi3line = DashedLine([-4, 2.75, 0], [-4, -2.75, 0])
        pi3 = MathTex(r" | \pi_3 \rangle").move_to([-4, -3.2, 0])

        H = MathTex(r"H").move_to([-4.85, 2.25, 0])
        Hsq = Square(side_length = 1, fill_opacity = 0.2).set_color([TEAL_B, MAROON_A]).move_to([-4.85, 2.25, 0])

        semicirc = Arc(fill_opacity=0, angle=PI, stroke_width = 3).move_to([-3.05, 2.25, 0]).scale(0.3)
        semicircsq = Square(side_length = 1, fill_opacity = 0.2).set_color([PINK, YELLOW]).move_to([-3.05, 2.25, 0])
        dot = Dot([-3.05, 2.15,0], radius = 0.05)
        line = Line([-3.05, 2.15, 0], [-2.75, 2.45, 0])

        pi2H = Line(start =  [-6.2, 2.25, 0], end = [-5.35, 2.25, 0])
        Hm = Line(start =  [-4.35, 2.25, 0], end = [-3.55, 2.25, 0])
        me = Line(start =  [-2.55, 2.3, 0], end = [-2, 2.3, 0])
        me2 = me.copy().shift(DOWN*0.2)

        pi2e = Line(start =  [-6.2, -1.57, 0], end = [-2, -1.57, 0])

        pi3form1 = MathTex(r" |\pi_3\rangle = \left\{ \begin{array}{ll} \hspace{-2mm} (-1)^{f(0)} |-\rangle |0\rangle \; \text{ if } f(0) \oplus f(1) = 0 \\ \hspace{-2mm} (-1)^{f(0)} |-\rangle|1\rangle \; \text{ if } f(0) \oplus f(1) = 1 \end{array} \right. ").move_to([3.15, -1.7, 0]).scale(0.8)

        pi3form2 = MathTex(r"  = \left\{ \begin{array}{ll} \hspace{-2mm} (-1)^{f(0)} |0\rangle \; \text{ if } f(0) \oplus f(1) = 0 \\ \hspace{-2mm} (-1)^{f(0)} |1\rangle \; \text{ if } f(0) \oplus f(1) = 1 \end{array} \right. ").move_to([3.15, -1.7, 0]).scale(0.8)




        #-------------------------------------------------#

        self.play(VGroup(pi2line, pi2).animate.shift(LEFT*4), Unwrite(VGroup(Uf, Ufrect, puf, muf, ufpi2t, ufpi2b, h1outminus, h0outplus)), run_time = 2)

        self.wait(2)

        self.play(Write(VGroup(pi3line, pi3, H, Hsq, semicirc, semicircsq, dot, line, 
                               pi2H, Hm, me, me2, pi2e)),
                  run_time = 2
        )

        self.wait(7)

        self.play(Write(pi3form1))

        self.wait(5)

        self.play(Transform(pi3form1, pi3form2))

        self.wait(5)

        self.play(Unwrite(VGroup(pi2line, pi2, Uf, Ufrect, puf, muf, ufpi2t, ufpi2b, h1outminus, h0outplus, pi3line, pi3, H, Hsq, semicirc, semicircsq, dot, line, pi2H, Hm, me, me2, pi2e, pi3form1, pi1corner, pi2form5, vline)), run_time = 3)

        
        zero = MathTex(r" | 0 \rangle ").move_to([-5, 2, 0])
        one = MathTex(r" | 1 \rangle ").move_to([-5, -2, 0])

        Hi1 = MathTex(r" H ").move_to([-3, 2, 0])
        Hi1sq = Square(side_length = 1, fill_opacity = 0.2).set_color([TEAL_B, MAROON_A]).move_to([-3, 2, 0])
        Hi2 = Hi1.copy().shift(DOWN*4)
        Hi2sq = Hi1sq.copy().shift(DOWN*4)
        Hio = Hi1.copy().shift(RIGHT*6)
        Hiosq = Hi1sq.copy().shift(RIGHT*6)
        Uf = MathTex(r" U_f ")
        Ufrect = Rectangle(width = 3, height = 5.5, fill_opacity = 0.2).set_color([TEAL_B, PINK, YELLOW])


        semicirc = Arc(fill_opacity=0, angle=PI, stroke_width = 3).move_to([5, 2, 0]).scale(0.3)
        semicircsq = Hi1sq.copy().shift(RIGHT*8).set_color([PINK, YELLOW])
        dot = Dot([5,1.84,0], radius = 0.05)
        line = Line([5, 1.84, 0], [5.3, 2.14, 0])

        group = VGroup(zero, one, Hi1, Hi1sq,
                       Hi2, Hi2sq, Hio, Hiosq, Uf, Ufrect, semicirc,
                       semicircsq, dot, line
        )

        hi1uf = Line(start =  [-2.5, 2, 0], end = [-1.5, 2, 0])
        ufhio = hi1uf.copy().shift(RIGHT*4)
        hi2uf = hi1uf.copy().shift(DOWN*4)
        hiom = hi1uf.copy().shift(RIGHT*6)
        zeroh = Line(start =  [-4.5, 2, 0], end = [-3.5, 2, 0])
        oneh = zeroh.copy().shift(DOWN*4)
        ufend = Line(start =  [1.5, -2, 0], end = [6.2, -2, 0])
        mend1 = Line(start = [5.5, 2.1, 0], end = [6.2, 2.1, 0])
        mend2 = mend1.copy().shift(DOWN*0.2)

        lines = VGroup(hi1uf, ufhio, hi2uf, hiom, zeroh, oneh, ufend, mend1, mend2)

        zer = MathTex(r"0").move_to([6.6, 2.3, 0])
        on = MathTex(r"1").move_to([6.6, 1.8, 0])

        pi1line = DashedLine([-2, 2.75, 0], [-2, -2.75, 0])
        pi1 = MathTex(r" | \pi_1 \rangle").move_to([-2, -3.2, 0])
        pi2line = DashedLine([2, 2.75, 0], [2, -2.75, 0])
        pi2 = MathTex(r" | \pi_2 \rangle").move_to([2, -3.2, 0])
        pi3line = DashedLine([4, 2.75, 0], [4, -2.75, 0])
        pi3 = MathTex(r" | \pi_3 \rangle").move_to([4, -3.2, 0])

        pis = VGroup(pi1line, pi1, pi2line, pi2, pi3line, pi3)

        rectangle = SurroundingRectangle(VGroup(zer, on)).set_color([TEAL_B, MAROON_A])

        groupf = VGroup(lines, group, zer, on, rectangle).move_to([0, 0, 0])
        groupff = VGroup(lines, group, zer, on, rectangle, pis).move_to([0, 0, 0])

        title = Tex(r" Deutsch's Algorithm ").set_color([TEAL_B, MAROON_A]).to_edge(UL)

        self.wait()

        self.play(FadeIn(title), FadeIn(VGroup(group, lines, zer, on, rectangle).move_to([0, -0.5, 0])), run_time = 4)

        self.wait(2)

        self.play(Unwrite(VGroup(title, group, lines, zer, on, rectangle)))

        self.wait()

        

        

        
class Bloch(ThreeDScene):
    def construct(self): 
        self.set_camera_orientation(
            phi = 70*DEGREES,
            theta = 20*DEGREES, 
            distance = 4
        )

        bloch = Surface(
            lambda u, v: np.array([
            3 * np.cos(u) * np.cos(v),
            3 * np.cos(u) * np.sin(v),
            3 * np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2],
            checkerboard_colors=[GRAY, GRAY], resolution=(16, 32), fill_opacity = 0.15
        ).scale(0.7)

        bloch.set_color_by_gradient(TEAL, GRAY_D, YELLOW)

        axes = ThreeDAxes(
            x_range = (-8, 8, 8), 
            y_range = (-8, 8, 8), 
            z_range = (-7, 7, 7), 
            x_length = 8, 
            y_length = 8, 
            z_length = 7
        ).scale(0.7)

        labels = axes.get_axis_labels(MathTex("x"), MathTex("y"), MathTex("z"))


        self.play(Write(axes), Write(labels))

        zeroone = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([0, 0, 2.1]),
            resolution = 8,
            color = PURE_RED,

        )


        one = MathTex(r"|1\rangle").move_to([1, 0, -2.7]).scale(0.7)
        zero = MathTex(r"|0\rangle").move_to([1, 0, 3]).scale(0.7)

        self.add_fixed_orientation_mobjects(one, zero)
        
        self.wait(2)
        
        self.play(Create(bloch), run_time = 6)
        
        self.play(Create(zeroone))
 
        self.wait(2)
        

        self.play(Rotate(
                    bloch, 
                    angle = 0.5*PI,
                    axis = np.array([0,1,0])
                ), Rotate(
                    zeroone,
                    angle = 0.5*PI, 
                    axis = np.array([0,1,0]),
                    about_point = ORIGIN),
                run_time = 5
        )
        
        self.wait(2)
  
        self.play(Rotate(
                    bloch,
                    angle = PI,
                    axis = np.array([1,0,0])
                ), Rotate(
                    zeroone, 
                    angle = PI,
                    axis = np.array([1,0,0]), 
                    about_point = ORIGIN), 
                run_time = 5
        )
        self.wait()

        finaloutput = MathTex(r" \frac{ |0\rangle + |1\rangle}{\sqrt{2}} ").move_to([-2, -2.3, -4]).scale(0.7)

        self.add_fixed_in_frame_mobjects(finaloutput)
        self.remove(finaloutput)

        self.wait(2)
        self.play(Write(finaloutput))
        
        self.wait(2)

        self.play(FadeOut(zeroone, finaloutput), run_time = 3)

        onezero = Arrow3D(
            start = np.array([0, 0, 0]),
            end = np.array([0, 0, -2.1]),
            resolution = 8, 
            color = PURE_BLUE, 
            thickness = 0.01
        )
 
        self.wait(2)

        self.play(Create(onezero))

        self.wait(2)

        self.play(Rotate(
                    bloch,
                    angle = 0.5*PI,
                    axis = np.array([0,1,0])
                ), Rotate(
                    onezero,
                    angle = 0.5*PI,
                    axis = np.array([0,1,0]),
                    about_point = ORIGIN),
                run_time = 5
        )

        self.wait(2)

        self.play(Rotate(
                    bloch,
                    angle = PI,
                    axis = np.array([1,0,0])
                ), Rotate(
                    onezero,
                    angle = PI,
                    axis = np.array([1,0,0]),
                    about_point = ORIGIN),
                run_time = 5
        )


        finaloutput = MathTex(r" \frac{ |0\rangle - |1\rangle}{\sqrt{2}} ").move_to([2, 2.3, 4]).scale(0.7)
        self.add_fixed_in_frame_mobjects(finaloutput)
        self.remove(finaloutput)

        self.wait(2)
        self.play(Write(finaloutput))

        self.wait(2)

        self.play(FadeOut(onezero, finaloutput), run_time = 3)

        self.play(Unwrite(VGroup(bloch, axes, labels, one, zero)))

        self.wait()


class Qiskit(Scene):
    def construct(self):

        qiskit_logo = ImageMobject("/Users/devaldeliwala/Desktop/qiskit.jpeg").move_to([0, 0, 0])

        qiskit = Tex(r" Qiskit ").move_to([1, 0, 0]).scale(1.5)


        self.play(FadeIn(qiskit_logo))
        self.wait(1)
        self.play(qiskit_logo.animate.shift(LEFT*1), Write(qiskit))

        self.wait(2)

        self.play(FadeOut(qiskit_logo), Unwrite(qiskit))

        self.wait(2)

        func_code1 = '''from qiskit import QuantumCircuit

def deutsch_function(case: int):

    f = QuantumCircuit(2)
'''
        func_code2 = '''from qiskit import QuantumCircuit

def deutsch_function(case: int): 
    f = QuantumCircuit(2)
    if case in [2, 3]:
        f.cx(0, 1)
    if case in [3, 4]:
        f.x(1)
    return f
'''


        func_code1_code = Code(code = func_code2, tab_width = 1, background = "window", language = "Python", font = "Monospace", style = 'vim', line_spacing=1 ).to_edge(UL)

        self.play(Write(func_code1_code))

        qcircuitin = MathTex(r" q_0: \\[4px] q_1: " ).to_edge(LEFT).shift(DOWN*2.8).shift(RIGHT*0.5)

        self.wait(2)

        qcircuitin_rect = Rectangle(height = 0.5, width = 8, color = YELLOW, fill_opacity = 0.2, stroke_width = 1).move_to([-2.6, 1.25, 0])
        case_rect = Rectangle(height = 2, width = 8, color = YELLOW, fill_opacity = 0.2, stroke_width = 1).move_to([-2.6, 0, 0])

        q1line = Line(start =  [0, 0, 0], end = [3, 0, 0])
        q1line.move_to([-3.9, -2.3, 0])
        q2line = q1line.copy().shift(DOWN*0.95)

        rect = SurroundingRectangle(VGroup(qcircuitin, q1line, q2line), corner_radius = 0.1, buff = 0.3).set_color([TEAL_B, MAROON_A])



        self.play(FadeIn(qcircuitin_rect))

        self.wait()

        self.play(Write(qcircuitin))

        self.wait(3)

        self.play(ReplacementTransform(qcircuitin_rect, case_rect))

        self.wait()

        self.play(Write(VGroup(q1line, q2line, rect)))

        case1 = Tex(r" if `case' $= $", r"\hspace{2mm}$1$").move_to([4, 0, 0])
        case1[1].set_color([PINK, YELLOW])
        case2 = Tex(r" if `case' $= $", r"\hspace{2mm}$2$").move_to([4, 0, 0])
        case2[1].set_color([PINK, YELLOW])
        case3 = Tex(r" if `case' $= $", r"\hspace{2mm}$3$").move_to([4, 0, 0])
        case3[1].set_color([PINK, YELLOW])
        case4 = Tex(r" if `case' $= $", r"\hspace{2mm}$4$").move_to([4, 0, 0])
        case4[1].set_color([PINK, YELLOW])

        f1 = MathTex(r"f_1(a)").move_to([4, -2.7, 0]).set_color([PINK, YELLOW]).scale(1.2)
        f2 = MathTex(r"f_2(a)").move_to([4, -2.7, 0]).set_color([PINK, YELLOW]).scale(1.2)
        f3 = MathTex(r"f_3(a)").move_to([4, -2.7, 0]).set_color([PINK, YELLOW]).scale(1.2)
        f4 = MathTex(r"f_4(a)").move_to([4, -2.7, 0]).set_color([PINK, YELLOW]).scale(1.2)
        

        dot = Dot([0,0,0], radius = 0.08).move_to([-4, -2.3, 0])
        X = MathTex(r"X").move_to([-4, -3.25, 0]).set_color([GRAY_E])
        Xsq = Square(side_length = 0.5, fill_opacity = 1).set_color([TEAL_B, MAROON_A]).move_to([-4, -3.25, 0])
        vline = Line(start =  [-4, -2.3, 0], end = [-4, -3, 0])

        X2 = X.copy().shift(RIGHT*0.5)
        X2sq = Xsq.copy().shift(RIGHT*0.5)


        self.play(Write(case1))

        self.wait(1)

        self.play(Write(f1))

        self.wait(4)

        self.play(Transform(case1, case2), Transform(f1, f2), run_time = 1.5)

        self.wait()


        self.play(Write(VGroup(dot, Xsq, vline)))
        self.play(Write(X))

        self.wait(4)

        self.play(Transform(case1, case3), Transform(f1, f3), run_time = 1.5)

        self.wait()
        self.play(VGroup(dot, X, Xsq, vline).animate.shift(LEFT*0.5), Write(X2sq))

        X3 = MathTex(r"X").move_to([-4.5, -3.25, 0]).set_color([GRAY_E])

        self.play(Write(X2), Write(X3))

        self.wait(4)
        self.play(FadeOut(X))
        self.play(Transform(case1, case4), Transform(f1, f4), run_time = 1.5)

        self.wait()

        X4 = MathTex(r"X").move_to([-4, -3.25, 0]).set_color([GRAY_E])

        self.play(Unwrite(VGroup(dot, Xsq, X3, vline, X2)))
        self.play(X2sq.animate.shift(LEFT*0.5))
        self.play(Write(X4))

        self.wait(4)
        
        self.play(FadeOut(VGroup(func_code1_code, case_rect)))
        self.play(Unwrite(VGroup(qcircuitin, q1line, q2line, X4, X2sq, case1, f1, rect)), run_time = 3)

        code = '''def compile_circuit(function: QuantumCircuit):
    n = function.num_qubits - 1
    qc = QuantumCircuit(n + 1, n)

    qc.x(n)
    qc.h(range(n + 1))

    qc.barrier()
    qc.compose(function, inplace=True)
    qc.barrier()

    qc.h(range(n))
    qc.measure(range(n), range(n))

    return qc

from qiskit_aer import AerSimulator

def deutsch_algorithm(function: QuantumCircuit):
    qc = compile_circuit(function)

    result = AerSimulator().run(qc, shots=1, memory=True).result()
    measurements = result.get_memory()
    if measurements[0] == "0":
        return "constant"
    return "balanced"
'''


        func_code2_code = Code(code = code, tab_width = 1, background = "window", language = "Python", font = "Monospace", style = 'vim').scale(0.74)

        self.wait(2)

        self.play(Write(func_code2_code), run_time = 4)

        self.wait(5)

        self.play(FadeOut(func_code2_code), run_time = 2)
        self.wait()



        









        


    
    
    
        




        











        

        

    



        
        

        



 
        




        
    



    

        

                







