import random
import numpy as np
import manim as mn
from svg.path import parse_path

def integrate(func, a, b, *, dx=0.01):
    return sum(func(x) * dx for x in np.arange(a, b, dx))

class SVGPath(mn.VMobject):
    def __init__(self, path_str, *, num_points=500, **kwargs):
        self.path       = parse_path(path_str)
        self.num_points = num_points

        super().__init__(**kwargs)

    def point(self, alpha):
        z = self.path.point(alpha)

        return np.array([z.real, z.imag, 0])

    def generate_points(self):
        step = 1 / self.num_points

        points = [self.point(x) for x in np.arange(0, 1, step)]
        self.start_new_path(points[0])
        self.add_points_as_corners(points[1:])
        self.add_line_to(self.point(1))

        self.flip(mn.RIGHT)
        self.center()

        return self

class Epicycle(mn.VMobject):
    def __init__(self, path, coeff_start, coeff_end=None, *, num_points=500, **kwargs):
        self.num_points = num_points

        if coeff_end is None:
            coeff_end   = int(np.ceil(coeff_start / 2))
            coeff_start = coeff_end - coeff_start

        self.coeffs = self.gen_fourier_coeffs(path, coeff_start, coeff_end)

        super().__init__(**kwargs)

    def generate_points(self):
        step = 1 / self.num_points

        points = [self.point(x) for x in np.arange(0, 1, step)]
        self.start_new_path(points[0])
        self.add_points_as_corners(points[1:])
        self.add_line_to(points[0])

        return self

    def point(self, alpha):
        z = sum(radius * np.exp(alpha * speed * mn.TAU * 1j) for speed, radius in self.coeffs.items())

        return np.array([z.real, z.imag, 0])

    def gen_fourier_coeffs(self, path, start, end):
        def point(alpha):
            pt = path.point_from_proportion(alpha) - path.get_center()

            return complex(pt[0], pt[1])

        # speed: radius
        return {i: integrate(lambda x: point(x) * np.exp(x * -i * mn.TAU * 1j), 0, 1) for i in range(start, end)}

    def draw_circles(self, alpha, whole_mobject=None, **kwargs):
        if whole_mobject is None:
            whole_mobject = self.copy()

        self.submobjects.clear()

        self.pointwise_become_partial(whole_mobject, 0, alpha)

        speeds_and_radii = sorted(self.coeffs.items(), key=lambda x: abs(x[1]), reverse=True)

        z = 0
        for speed, radius in speeds_and_radii:
            circ = mn.Circle(**kwargs)
            circ.scale(abs(radius))
            circ.move_to([z.real, z.imag, 0])
            self.add(circ)

            z += radius * np.exp(alpha * speed * mn.TAU * 1j)

        return self

    def animate_circles(self, **kwargs):
        class Draw(mn.Animation):
            def interpolate_submobject(self, submobject, starting_submobject, alpha):
                submobject.draw_circles(alpha, starting_submobject, **kwargs)

        return Draw(self)

class EpicCycle(mn.Scene):
    path_str = "M 231.17,301.72 C 231.17,301.72 240.00,301.72 240.00,301.72 240.00,327.57 235.79,346.38 227.36,358.16 218.94,369.94 208.43,375.83 195.83,375.83 185.52,375.83 175.62,371.94 166.13,364.17 156.65,356.40 148.14,335.58 140.61,301.72 140.61,301.72 119.51,206.50 119.51,206.50 119.51,206.50 46.38,372.39 46.38,372.39 46.38,372.39 -0.00,372.39 -0.00,372.39 -0.00,372.39 105.03,146.13 105.03,146.13 99.47,116.85 92.76,95.17 84.91,81.10 77.06,67.04 67.32,60.00 55.71,60.00 46.38,60.00 38.24,63.56 31.29,70.67 24.34,77.79 20.45,88.79 19.63,103.68 19.63,103.68 10.80,103.68 10.80,103.68 11.29,79.63 16.11,60.37 25.28,45.89 34.44,31.41 45.89,24.17 59.63,24.17 68.47,24.17 76.85,27.81 84.79,35.09 92.72,42.37 99.59,54.81 105.40,72.39 111.21,89.98 120.25,126.42 132.52,181.72 132.52,181.72 149.94,259.51 149.94,259.51 156.97,291.74 164.38,313.29 172.15,324.17 179.92,335.05 189.20,340.49 200.00,340.49 218.32,340.49 228.71,327.57 231.17,301.72 231.17,301.72 231.17,301.72 231.17,301.72 Z"
    def construct(self):
        # Scale because I don't want to edit the SVG because I'm lazy
        path = SVGPath(self.path_str).scale(0.01)
        path.set_color(mn.TEAL).set_opacity(0.8)

        self.add(path)

        for num_coeffs in range(5, 105 + 1, 20):
            ep = Epicycle(path, num_coeffs)
            ep_copy = ep.copy().draw_circles(0, color=mn.BLUE)

            text = mn.Tex(f"").to_edge(mn.UP).shift(mn.LEFT)

            self.play(mn.FadeIn(mn.VGroup(ep_copy, text)), run_time=0.75)
            self.remove(ep_copy)

            self.play(ep.animate_circles(color=mn.BLUE), run_time=10, rate_func=mn.linear)

            self.play(mn.FadeOut(mn.VGroup(ep, text)), run_time = 4)
