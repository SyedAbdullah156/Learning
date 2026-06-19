from manim import *

class PointMovingOnShapes(Scene):
    def construct(self):
        # 1. Create a background coordinate grid
        grid = NumberPlane(
            x_range=[-7, 7, 1],  # Min X, Max X, step size
            y_range=[-4, 4, 1],  # Min Y, Max Y, step size
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )
        grid.add_coordinates() # This adds the actual number labels (-3, -2, -1, 1, 2...)
        
        # 2. Define your line
        start_point = [3, 0, 0]
        end_point = [5, 0, 0]
        line = Line(start_point, end_point, color=YELLOW, stroke_width=6)
        
        # 3. Add dots at the start and end points so you can spot them perfectly
        start_dot = Dot(start_point, color=RED)
        end_dot = Dot(end_point, color=GREEN)
        
        # 4. Render everything on screen
        self.add(grid) # Display the grid instantly in the background
        self.play(FadeIn(start_dot), FadeIn(end_dot))
        self.play(Create(line))

        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()