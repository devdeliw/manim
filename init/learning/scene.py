from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen


class AnimatedGraph(Scene):
    def construct(self):
        ax = Axes(x_range = (-3, 3), y_range = (-3, 3))
        curve = ax.plot(lambda x: (x+2)*x*(x-2)/2, color = RED)
        area = ax.get_area(curve, x_range = (-2, 0))
        self.play(Create(ax, run_time = 2), Create(curve, run_time = 5))
        self.play(FadeIn(area))
        self.wait(2)

class Positioning(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)

        # positioning dots
        red_dot = Dot(color = RED)
        green_dot = Dot(color = GREEN)
        green_dot.next_to(red_dot, RIGHT + UP)

        self.add(red_dot, green_dot)

        # shift
        s = Square(color = ORANGE)
        s.shift(2 * UP + 4 * RIGHT)
        self.add(s)

        # move_to
        c = Circle(color = PURPLE)
        c.move_to([-3, -2, 0])
        self.add(c) 

        # align_to
        c2 = Circle(radius = 0.5, color = RED, fill_opacity = 0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        c2.align_to(s, UP)
        c3.align_to(s, DOWN)
        c4.align_to(s, LEFT)
        self.add(c2,c3,c4)

from colour import Color

class LaggingGroup(Scene):
    def construct(self):
        squares = VGroup(*[Square(color = Color(hue = j/20, saturation = 1, luminance = 0.5), 
        fill_opacity = 0.5) for j in range(20)]).arrange_in_grid(4, 5).scale(0.75)
        self.play(AnimationGroup(*[FadeIn(s) for s in squares], lag_ratio = 0.15))

class AnimateSyntax(Scene):
    def construct(self):
        s = Square(color = GREEN, fill_opacity = 0.5)
        c = Circle(color = RED, fill_opacity = 0.5)
        self. add(s,c) 

        self.play(s.animate.shift(UP), c.animate.shift(DOWN))


