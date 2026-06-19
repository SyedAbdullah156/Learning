from manim import *
import numpy as np

class LinearDependence3D(ThreeDScene):
    def construct(self):

        # -----------------------
        # Scene setup
        # -----------------------
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)

        axes = ThreeDAxes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
        )

        self.add(axes)

        # -----------------------
        # Column vectors (DEPENDENT case)
        # One vector is linear combination of others
        # -----------------------
        v1 = np.array([1, 0, 0])
        v2 = np.array([0, 1, 0])
        v3 = np.array([1, 1, 0])  # lies in span of v1 and v2 → NOT full 3D

        origin = np.array([0, 0, 0])

        vec1 = Arrow3D(origin, v1, color=BLUE)
        vec2 = Arrow3D(origin, v2, color=GREEN)
        vec3 = Arrow3D(origin, v3, color=RED)

        self.play(Create(vec1), Create(vec2), Create(vec3))

        # -----------------------
        # Show plane (z = 0 plane)
        # -----------------------
        plane = Surface(
            lambda u, v: np.array([u, v, 0]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(10, 10),
            fill_opacity=0.2,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )

        self.play(FadeIn(plane))

        # -----------------------
        # Linear combination cloud
        # a*v1 + b*v2 + c*v3
        # but all stay in z = 0 plane
        # -----------------------
        dots = VGroup()

        for _ in range(120):
            a = np.random.uniform(-1, 1)
            b = np.random.uniform(-1, 1)
            c = np.random.uniform(-1, 1)

            point = a * v1 + b * v2 + c * v3

            dot = Dot3D(point, color=YELLOW, radius=0.03)
            dots.add(dot)

        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.01))

        # -----------------------
        # Highlight conclusion
        # -----------------------
        text = Text("All combinations stay in a plane (rank < 3)", font_size=28)
        text.to_edge(UP)

        self.play(Write(text))

        self.wait(3)