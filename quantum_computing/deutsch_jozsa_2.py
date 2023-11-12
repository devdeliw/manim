from manim import * 
import math 
import numpy as np

class Introduction(Scene):
    def construct(self): 
        self.camera.background_color = GRAY_E

        self.wait(30)


class Classical(Scene):
    def construct(self):
        
        axis = NumberPlane(
                x_range=(-1, 4, 1),
                y_range=(-1, 10, 1),
                x_length=4,
                y_length=6,
                ).scale(0.9).to_edge(DR)shift(RIGHT*0.4)

        graph = axis.plot(lambda x: 2**(x-1) + 1).set_color([YELLOW])

        graph_lbl = axis.get_graph_label(graph, label=MathTex(r" 2^{n - 1} + 1")).set_color([WHITE]).shift(DR*0.3)
        rect = Rectangle(color = WHITE, height = 5.5, width = 4).to_edge(DL).shift(UP*0.24).shift(RIGHT(0.4)

        self.play(Write(axis))
        self.wait()
        self.play(Write(graph))
        self.wait()
        self.play(Write(rect))
        self.wait()
        self.play(Write(graph_lbl))

        classical = Tex(r" Classical $\#$ Query ").move_to([-4.1, 3, 0])

        self.wait(3)
        self.play(Write(classical))
        
        self.wait()

        self.play(graph_lbl.animate.set_color([YELLOW]))
        self.wait(20)

        axis2 = axis.copy().to_edge(DR).shift(LEFT*0.4)
        graph2 = axis2.plot(lambda x: 1).set_color([YELLOW])

        graph_lbl2 = axis.get_graph_label(graph, label=MathTex(r"1")).set_color([WHITE]).shift(LEFT*0.3)
        rect2 = Rectangle(color = WHITE, height = 5.5, width = 4).to_edge(DR).shift(UP*0.24)

        self.play(Write(axis2))
        self.wait()
        self.play(Write(graph2))
        self.wait()
        self.play(Write(rect2))
        self.wait()
        self.play(Write(graph_lbl2))

        classical2 = Tex(r" Quantum $\#$ Query ").move_to([4.1, 3, 0])

        self.wait(3)
        self.play(Write(classical2))

        self.wait()

        self.play(graph_lbl2.animate.set_color([YELLOW]))
