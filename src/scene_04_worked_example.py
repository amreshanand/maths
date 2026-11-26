"""
Scene 4: Worked Example
Step-by-Step Matrix Vector Multiplication: v1 = (1,1) -> (3,3) and v2 = (2,-1) -> (3,0)
"""

from manim import *
import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))
from helpers.theme import *
from helpers.grid_utils import (
    create_styled_plane, 
    create_scene_header, 
    create_matrix_mobject, 
    create_col_vector_mobject
)

class Scene04WorkedExample(Scene):
    def construct(self):
        apply_scene_style(self)

        # 1. Header (3 seconds)
        header = create_scene_header("Worked Example: Calculating Vector Transformations",
                                     "Algebraic Matrix Multiplication & Geometric Alignment")
        self.play(FadeIn(header), run_time=1.2)
        self.wait(1.8)

        # 2. Setup Split Layout: Plane on Right, Calculations on Left (5 seconds)
        plane = create_styled_plane(
            x_range=(-2, 5, 1),
            y_range=(-2, 4, 1),
            x_length=6.5,
            y_length=5.5
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)

        self.play(Create(plane), run_time=1.5)
        self.wait(1.0)

        # 3. Calculation 1: v1 = (1, 1) -> (3, 3) (22 seconds)
        # Vector on plane
        v1_arr = Arrow(plane.c2p(0, 0), plane.c2p(1, 1), buff=0, color=COLOR_V1, stroke_width=4.5)
        lbl_v1 = Text("v₁ (1, 1)", font_size=18, color=COLOR_V1, weight=BOLD).next_to(plane.c2p(1, 1), UL, buff=0.1)

        # Calculation card on left
        calc1_title = Text("Example 1: v₁ = (1, 1)ᵀ", font_size=22, weight=BOLD, color=COLOR_V1)
        
        step1_formula = Text("T(x, y) = [2x + y ; x + 2y]", font_size=18, color=COLOR_MUTED)
        
        step1_eval = VGroup(
            Text("Top:    2(1) + 1(1) = 2 + 1 = 3", font_size=19, color=COLOR_TEXT),
            Text("Bottom: 1(1) + 2(1) = 1 + 2 = 3", font_size=19, color=COLOR_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        step1_result = Text("⟹  A · v₁ = (3, 3)ᵀ", font_size=22, weight=BOLD, color=COLOR_HIGHLIGHT)

        calc1_group = VGroup(calc1_title, step1_formula, step1_eval, step1_result).arrange(
            DOWN, aligned_edge=LEFT, buff=0.25
        ).to_edge(LEFT, buff=0.6).shift(UP * 0.5)

        self.play(GrowArrow(v1_arr), FadeIn(lbl_v1), run_time=1.2)
        self.play(FadeIn(calc1_title), FadeIn(step1_formula), run_time=1.5)
        self.wait(1.5)
        self.play(FadeIn(step1_eval), run_time=2.0)
        self.wait(2.0)
        self.play(FadeIn(step1_result), run_time=1.5)
        self.wait(1.5)

        # Animate v1 stretching to (3, 3)
        v1_target = Arrow(plane.c2p(0, 0), plane.c2p(3, 3), buff=0, color=COLOR_TRANS_V1, stroke_width=4.5)
        lbl_v1_target = Text("T(v₁) = (3, 3)", font_size=18, color=COLOR_TRANS_V1, weight=BOLD).next_to(plane.c2p(3, 3), UR, buff=0.1)

        self.play(
            Transform(v1_arr, v1_target),
            Transform(lbl_v1, lbl_v1_target),
            run_time=2.5
        )
        self.wait(3.5)

        # Clear Example 1 elements
        self.play(
            FadeOut(calc1_group),
            FadeOut(v1_arr),
            FadeOut(lbl_v1),
            run_time=1.2
        )

        # 4. Calculation 2: v2 = (2, -1) -> (3, 0) (24 seconds)
        v2_arr = Arrow(plane.c2p(0, 0), plane.c2p(2, -1), buff=0, color=COLOR_V2, stroke_width=4.5)
        lbl_v2 = Text("v₂ (2, -1)", font_size=18, color=COLOR_V2, weight=BOLD).next_to(plane.c2p(2, -1), DR, buff=0.1)

        calc2_title = Text("Example 2: v₂ = (2, -1)ᵀ", font_size=22, weight=BOLD, color=COLOR_V2)
        
        step2_formula = Text("T(x, y) = [2x + y ; x + 2y]", font_size=18, color=COLOR_MUTED)
        
        step2_eval = VGroup(
            Text("Top:    2(2) + 1(-1) = 4 - 1 = 3", font_size=19, color=COLOR_TEXT),
            Text("Bottom: 1(2) + 2(-1) = 2 - 2 = 0", font_size=19, color=COLOR_TEXT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        step2_result = Text("⟹  A · v₂ = (3, 0)ᵀ", font_size=22, weight=BOLD, color=COLOR_HIGHLIGHT)
        note_axis = Text("Notice: Lands directly on the x-axis!", font_size=17, color=COLOR_TRANS_E1, weight=BOLD)

        calc2_group = VGroup(calc2_title, step2_formula, step2_eval, step2_result, note_axis).arrange(
            DOWN, aligned_edge=LEFT, buff=0.25
        ).to_edge(LEFT, buff=0.6).shift(UP * 0.5)

        self.play(GrowArrow(v2_arr), FadeIn(lbl_v2), run_time=1.2)
        self.play(FadeIn(calc2_title), FadeIn(step2_formula), run_time=1.5)
        self.wait(1.5)
        self.play(FadeIn(step2_eval), run_time=2.0)
        self.wait(2.0)
        self.play(FadeIn(step2_result), FadeIn(note_axis), run_time=1.5)
        self.wait(1.5)

        # Animate v2 landing on (3, 0)
        v2_target = Arrow(plane.c2p(0, 0), plane.c2p(3, 0), buff=0, color=COLOR_TRANS_V2, stroke_width=4.5)
        lbl_v2_target = Text("T(v₂) = (3, 0)", font_size=18, color=COLOR_TRANS_V2, weight=BOLD).next_to(plane.c2p(3, 0), UP, buff=0.1)

        self.play(
            Transform(v2_arr, v2_target),
            Transform(lbl_v2, lbl_v2_target),
            run_time=2.5
        )
        self.wait(4.0)

        # Clean exit
        self.play(
            FadeOut(calc2_group),
            FadeOut(v2_arr),
            FadeOut(lbl_v2),
            FadeOut(plane),
            FadeOut(header),
            run_time=1.5
        )
        self.wait(0.5)
