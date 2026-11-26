"""
Scene 2: Concept Introduction
Linear Transformations: Formal Definition, Linearity Properties, and Origin Fixation
"""

from manim import *
import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))
from helpers.theme import *
from helpers.grid_utils import create_styled_plane, create_scene_header

class Scene02Concept(Scene):
    def construct(self):
        apply_scene_style(self)

        # 1. Header (4 seconds)
        header = create_scene_header("Concept Definition: What is a Linear Transformation?",
                                     "T(v) = Av  |  Mapping input vectors to output vectors")
        self.play(FadeIn(header), run_time=1.5)
        self.wait(2.5)

        # 2. Function Mapping Concept (8 seconds)
        def_card = VGroup(
            Text("A transformation T is a function mapping vectors to vectors:", font_size=24, color=COLOR_TEXT),
            Text("T : R² → R²", font_size=30, weight=BOLD, color=COLOR_HIGHLIGHT),
            Text("When linear, it is computed via matrix multiplication: T(v) = Av", font_size=24, color=COLOR_TEXT),
        ).arrange(DOWN, buff=0.3).next_to(header, DOWN, buff=0.5)

        self.play(FadeIn(def_card, shift=DOWN * 0.2), run_time=2.0)
        self.wait(4.0)
        self.play(FadeOut(def_card), run_time=1.0)

        # 3. Two Axioms of Linearity (Split Layout) (18 seconds)
        # Left side: Definitions
        prop_title = Text("The Two Core Linearity Axioms:", font_size=24, weight=BOLD, color=COLOR_HIGHLIGHT).to_corner(UL).shift(DOWN * 1.2 + RIGHT * 0.3)
        
        prop1 = VGroup(
            Text("1. Additivity (Superposition):", font_size=20, weight=BOLD, color=COLOR_TEXT),
            Text("   T(u + v) = T(u) + T(v)", font_size=22, weight=BOLD, color=COLOR_E2),
            Text("   Vector addition is preserved.", font_size=18, color=COLOR_MUTED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)

        prop2 = VGroup(
            Text("2. Homogeneity (Scaling):", font_size=20, weight=BOLD, color=COLOR_TEXT),
            Text("   T(c · u) = c · T(u)", font_size=22, weight=BOLD, color=COLOR_E1),
            Text("   Scalar scaling is preserved.", font_size=18, color=COLOR_MUTED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)

        props_group = VGroup(prop1, prop2).arrange(DOWN, aligned_edge=LEFT, buff=0.45).next_to(prop_title, DOWN, aligned_edge=LEFT, buff=0.3)

        # Right side: Geometric coordinate illustration
        mini_plane = create_styled_plane(x_range=(-1, 4, 1), y_range=(-1, 4, 1), x_length=4.5, y_length=4.5)
        mini_plane.to_corner(DR).shift(UP * 0.4 + LEFT * 0.5)

        self.play(FadeIn(prop_title), FadeIn(props_group), Create(mini_plane), run_time=2.0)
        self.wait(2.0)

        # Visualizing Additivity: vectors u, v, and u+v
        u_arr = Arrow(mini_plane.c2p(0, 0), mini_plane.c2p(2, 0.5), buff=0, color=COLOR_E2, stroke_width=3.5)
        v_arr = Arrow(mini_plane.c2p(2, 0.5), mini_plane.c2p(2.5, 2.5), buff=0, color=COLOR_E1, stroke_width=3.5)
        sum_arr = Arrow(mini_plane.c2p(0, 0), mini_plane.c2p(2.5, 2.5), buff=0, color=COLOR_HIGHLIGHT, stroke_width=4.0)
        
        lbl_u = Text("u", font_size=18, color=COLOR_E2).next_to(u_arr.get_center(), DOWN, buff=0.1)
        lbl_v = Text("v", font_size=18, color=COLOR_E1).next_to(v_arr.get_center(), RIGHT, buff=0.1)
        lbl_sum = Text("u + v", font_size=18, color=COLOR_HIGHLIGHT).next_to(sum_arr.get_center(), UL, buff=0.1)

        self.play(GrowArrow(u_arr), FadeIn(lbl_u), run_time=1.2)
        self.play(GrowArrow(v_arr), FadeIn(lbl_v), run_time=1.2)
        self.play(GrowArrow(sum_arr), FadeIn(lbl_sum), run_time=1.5)
        self.wait(3.5)

        # Visualizing Homogeneity: scaling u
        self.play(FadeOut(v_arr), FadeOut(sum_arr), FadeOut(lbl_v), FadeOut(lbl_sum), run_time=1.0)
        scaled_u_arr = Arrow(mini_plane.c2p(0, 0), mini_plane.c2p(3.5, 0.875), buff=0, color=COLOR_HIGHLIGHT, stroke_width=4.0)
        lbl_scaled = Text("c · u", font_size=18, color=COLOR_HIGHLIGHT).next_to(scaled_u_arr.get_end(), UR, buff=0.1)
        
        self.play(Transform(u_arr, scaled_u_arr), FadeIn(lbl_scaled), FadeOut(lbl_u), run_time=1.8)
        self.wait(3.0)

        # Clean up axioms panel
        self.play(
            FadeOut(prop_title),
            FadeOut(props_group),
            FadeOut(mini_plane),
            FadeOut(u_arr),
            FadeOut(lbl_scaled),
            run_time=1.2
        )

        # 4. Mandatory Origin Fixation: T(0) = 0 (12 seconds)
        origin_card = VGroup(
            Text("Crucial Requirement: The Origin Must Remain Fixed!", font_size=28, weight=BOLD, color=COLOR_WARN),
            Text("T(0) = T(0 · v) = 0 · T(v) = 0", font_size=26, weight=BOLD, color=COLOR_TEXT),
            Text("Why? If the origin moves, the transformation cannot be linear.", font_size=22, color=COLOR_MUTED),
        ).arrange(DOWN, buff=0.35).move_to(UP * 0.8)

        # Non-example demonstration
        affine_demo = VGroup(
            Text("Non-Example: Translation T(v) = v + b  (b ≠ 0)", font_size=22, color=COLOR_WARN, weight=BOLD),
            Text("• Moves (0, 0) to b  ⟹  T(0) ≠ 0", font_size=20, color=COLOR_TEXT),
            Text("• Grid lines shift, but it is AFFINE, NOT LINEAR!", font_size=20, color=COLOR_HIGHLIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(origin_card, DOWN, buff=0.5)

        self.play(FadeIn(origin_card, shift=UP * 0.2), run_time=1.5)
        self.wait(3.0)
        self.play(FadeIn(affine_demo, shift=UP * 0.2), run_time=1.5)
        self.wait(4.0)

        # Final transition
        self.play(FadeOut(origin_card), FadeOut(affine_demo), FadeOut(header), run_time=1.5)
        self.wait(0.5)
