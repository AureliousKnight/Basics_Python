from manim import *

class ParticleAccelerator(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 9, 1],
            y_range=[0, 100, 10],
            axis_config={"color": BLUE, "stroke_width": 2},
            x_length=6,
            y_length=5,
            tips=False
        )
        axes.to_edge(LEFT, buff=0.5)

        self.sim_time = 0.0
        self.sim_v = 0.0
        
        def dynamic_acceleration(t):
            self.sim_time = t
            if t < 4:
                self.sim_v = 4.5 * (t**2)
            else:
                self.sim_v = 72 + 5 * (t - 4)
            return self.sim_v

        trajectory_curve = axes.plot(dynamic_acceleration, color=RED, x_range=[0, 9])
        quantum_dot = Dot(color=GOLD).scale(1.8).move_to(axes.c2p(0, 0))

        self.play(Create(axes), run_time=1.5)
        self.wait(0.5)

        self.play(
            Create(trajectory_curve, rate_func=linear),
            MoveAlongPath(quantum_dot, trajectory_curve, rate_func=linear),
            run_time=6
        )
        
        self.play(Flash(quantum_dot, color=YELLOW, flash_radius=0.6, num_lines=15, run_time=1))
        self.wait(2)


