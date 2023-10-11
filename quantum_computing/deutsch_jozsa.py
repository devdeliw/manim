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

            group_final.set_color([TEAL_B, MAROON_A])

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
