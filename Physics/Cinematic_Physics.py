import numpy as np
import matplotlib.pyplot as plt
from manim import *

class ParticleAccelerator(Scene):
    def construct(self):
        grid = Axes(
            x_range=[0, 12, 5],
            y_range=[0, 100, 25],
            axis_config={"color": BLUE_C, "stroke_width": 2},
            x_length=7,
            y_length=5,
            tips=False
        ).add_coordinates()
        grid.to_edge(LEFT, buff=0.5)
        labels = grid.get_axis_label(x_label="t (s)", y_label="v (m/s)")
        title = Text("Relativistic Kinetic Simulation", font="Consolas", color=GREEN_C).scale(0.7)
        title.to_edge(UP)

        info_box = VGroup(
            Text("ENGINE STATISTICS", font="Consolas", color=GREY_A).scale(0.4),
            Line(LEFT, RIGHT, color=BLUE_D.scale(1.5)),
        ). arrange(DOWN, buff=0.15)
        time_text = always_redraw(lambda: Text(f"Time:{self.time:.2f} s", font="Consolas", color=WHITE).scale(0.5))
        vel_text = always_redraw(lambda: Text(f"Speed:{self.current_v:.1f} m/s", font="Consolas", color=RED).scale(0.5))
        energy_text = always_redraw(lambda: Text(f"Energy: {0.5 * 2.0 *(self.current_v**2):.0f} J", font="Consolas", color=GOLD_C).scale(0.5))
        stats_panel = VGroup(info_box, time_text, vel_text, energy_text).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        stats_panel.to_edge(RIGHT, buff=0.8)
        self.time = 0.0
        self.current_v = 0.0
    def dynamic_acceleration(t):
        self.time = t
        if t < 4:
            self.current_v = 4.5 * (t**2)
        else:
            self.current_v = 72 + 5 * (t - 4)
            return self.current_v
trajectory_curve = grid.plot(dynamic_acceleration, color=RED_C, x_range=[0, 9])
quantum_dot = Dot(color=Gold_E).scale(0.8).move_to(grid.c2p(0, 0))
self.play(Write(title), FadeIn(stats_panel, shift=LEFT))
self.play(Creator(grid), Write(labels), run_time=2)
self.wait(0.5)
self.play(
    Create(trajectory_curve, rate_func=linear),
    MoveAlongPath(quantum_dot, trajectory_curve, rate_func=linear),
    run_time=6
)
self.play(Flash(quantum_dot, color=GOLD_A, flash_radius=0.6, num_lines=15, run_time=1))
self.wait(2)

