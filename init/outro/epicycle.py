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
            circ = mn.Circle(**kwargs).set_color([mn.TEAL_B, mn.MAROON_A]).set_opacity(0.1)
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
    path_str = "M 832.86,537.62\
           C 685.23,632.04 595.90,795.18 595.87,970.42\
             596.09,1121.53 662.81,1264.88 778.28,1362.35\
             775.57,1375.86 775.66,1391.35 780.37,1405.79\
             794.36,1448.25 841.97,1466.86 868.02,1475.78\
             886.24,1481.94 914.39,1490.14 921.33,1482.30\
             931.06,1471.84 928.41,1455.30 884.86,1443.72\
             861.79,1437.37 839.77,1419.88 829.05,1400.61\
             912.50,1455.12 1010.01,1484.17 1109.69,1484.23\
             1280.11,1484.19 1439.41,1399.66 1534.98,1258.56\
             1465.81,1302.63 1387.11,1329.50 1305.43,1336.93\
             1306.39,1336.43 1307.48,1335.72 1308.51,1334.63\
             1315.75,1327.15 1313.57,1308.46 1304.28,1302.31\
             1298.37,1298.32 1291.98,1301.09 1287.76,1295.78\
             1285.71,1292.89 1285.23,1289.75 1285.23,1287.46\
             1285.23,1287.46 1322.57,1231.98 1306.86,1139.40\
             1302.02,1104.46 1298.78,1086.43 1303.25,1056.87\
             1314.70,980.79 1303.49,923.87 1297.69,874.33\
             1294.25,844.92 1302.16,826.31 1294.76,787.24\
             1289.69,728.26 1276.66,718.60 1271.84,718.24\
             1267.01,717.88 1258.28,721.48 1245.37,743.19\
             1245.37,743.19 1202.36,730.91 1152.18,757.32\
             1152.18,757.32 1139.73,752.07 1121.24,746.50\
             1065.14,729.07 1105.99,776.45 1106.42,777.77\
             1114.17,789.74 1119.85,798.01 1120.16,805.33\
             1117.50,826.31 1120.73,860.40 1134.62,876.63\
             1137.66,881.11 1141.95,883.59 1132.91,910.86\
             1128.14,922.24 1119.81,927.52 1113.88,933.50\
             1076.58,971.34 991.99,1081.12 1038.68,1263.58\
             1017.34,1258.41 996.71,1255.84 976.97,1255.31\
             831.96,1160.51 744.49,999.01 744.32,825.76\
             744.32,723.02 775.20,622.66 832.86,537.62\
             832.86,537.62 832.86,537.62 832.86,537.62 Z"

    def construct(self):
        # Scale because I don't want to edit the SVG because I'm lazy
        path = SVGPath(self.path_str).scale(0.005)
        path.set_color([mn.TEAL_B, mn.MAROON_A]).set_opacity(0.5)

        self.add(path)

        for num_coeffs in range(45, 105 + 1, 20):
            ep = Epicycle(path, num_coeffs)
            ep_copy = ep.copy().draw_circles(0, color=mn.BLUE_A)


            self.play(mn.FadeIn(mn.VGroup(ep_copy)), run_time=0.75)
            self.remove(ep_copy)

            self.play(ep.animate_circles(color=mn.PURPLE_A), run_time=20, rate_func=mn.linear)
            self.wait()
            self.play(mn.FadeOut(mn.VGroup(ep)), run_time = 4)
