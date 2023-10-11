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
        FeedForwardLayer(25)
            ],
            layer_spacing=0.8,
        )
        nn.move_to(ORIGIN)
        self.add(nn)
        self.play(
            make_neural_network_dropout_animation(
                nn, dropout_rate=0.2, do_forward_pass=True
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

        self.play(Create(vgf.shift(3.5*LEFT).scale(0.7).set_color([GRAY_D])))

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

