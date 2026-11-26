"""
Scene 3: Visual Intuition
Basis Vectors e1, e2, Matrix Columns as Landing Sites, and Unit Square to Parallelogram
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

class Scene03VisualIntuition(Scene):
    def construct(self):
        apply_scene_style(self)

        # 1. Header (3 seconds)
        header = create_scene_header("Visual Intuition: Tracking Basis Vectors",
                                     "Every vector is a combination of e1 and e2")
        self.play(FadeIn(header), run_time=1.2)
        self.wait(1.8)

        # 2. Setup Background Plane & Original Grid (6 seconds)
        plane = create_styled_plane(
            x_range=(-2, 6, 1),
            y_range=(-2, 5, 1),
            x_length=9.0,
            y_length=6.0
        ).shift(DOWN * 0.4 + RIGHT * 1.2)

        self.play(Create(plane), run_time=1.8)
        self.wait(1.0)

        # 3. Introduce Standard Basis Vectors e1 and e2 (8 seconds)
        e1_arr = Arrow(plane.c2p(0, 0), plane.c2p(1, 0), buff=0, color=COLOR_E1, stroke_width=4.5)
        e2_arr = Arrow(plane.c2p(0, 0), plane.c2p(0, 1), buff=0, color=COLOR_E2, stroke_width=4.5)
        
        lbl_e1 = Text("e₁ (1, 0)", font_size=18, color=COLOR_E1, weight=BOLD).next_to(e1_arr.get_end(), DOWN, buff=0.15)
        lbl_e2 = Text("e₂ (0, 1)", font_size=18, color=COLOR_E2, weight=BOLD).next_to(e2_arr.get_end(), LEFT, buff=0.15)

        # Unit square polygon
        unit_square = Polygon(
            plane.c2p(0, 0),
            plane.c2p(1, 0),
            plane.c2p(1, 1),
            plane.c2p(0, 1),
            color=COLOR_SQUARE,
            fill_color=COLOR_SQUARE,
            fill_opacity=0.35,
            stroke_width=2.5
        )
        sq_lbl = Text("Unit Square\nArea = 1", font_size=16, color=COLOR_SQUARE, weight=BOLD).move_to(plane.c2p(0.5, 0.5))

        self.play(GrowArrow(e1_arr), FadeIn(lbl_e1), run_time=1.2)
        self.play(GrowArrow(e2_arr), FadeIn(lbl_e2), run_time=1.2)
        self.play(DrawBorderThenFill(unit_square), FadeIn(sq_lbl), run_time=1.5)
        self.wait(3.0)

        # 4. Matrix A Display & Column Correspondence (12 seconds)
        matrix_a_data = [[2, 1], [1, 2]]
        mat_mobj = create_matrix_mobject(matrix_a_data, col_colors=[COLOR_E1, COLOR_E2], font_size=28)
        
        matrix_panel = VGroup(
            Text("Transformation Matrix A:", font_size=18, color=COLOR_TEXT, weight=BOLD),
            mat_mobj,
            Text("Col 1: T(e₁) = (2, 1)", font_size=16, color=COLOR_TRANS_E1, weight=BOLD),
            Text("Col 2: T(e₂) = (1, 2)", font_size=16, color=COLOR_TRANS_E2, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_corner(UL).shift(DOWN * 1.0 + RIGHT * 0.2)

        self.play(FadeIn(matrix_panel, shift=RIGHT * 0.3), run_time=2.0)
        self.wait(4.0)

        # 5. Smooth Transformation of Grid, Basis Vectors, and Unit Square (15 seconds)
        # Transformation matrix [[2, 1], [1, 2]]
        # Transformed unit square becomes parallelogram with vertices:
        # (0, 0), (2, 1), (3, 3), (1, 2)
        transformed_parallelogram = Polygon(
            plane.c2p(0, 0),
            plane.c2p(2, 1),
            plane.c2p(3, 3),
            plane.c2p(1, 2),
            color=COLOR_PARALLELOGRAM,
            fill_color=COLOR_PARALLELOGRAM,
            fill_opacity=0.45,
            stroke_width=3.0
        )

        target_e1_arr = Arrow(plane.c2p(0, 0), plane.c2p(2, 1), buff=0, color=COLOR_TRANS_E1, stroke_width=4.5)
        target_e2_arr = Arrow(plane.c2p(0, 0), plane.c2p(1, 2), buff=0, color=COLOR_TRANS_E2, stroke_width=4.5)
        
        lbl_target_e1 = Text("T(e₁) = (2, 1)", font_size=17, color=COLOR_TRANS_E1, weight=BOLD).next_to(plane.c2p(2, 1), DR, buff=0.1)
        lbl_target_e2 = Text("T(e₂) = (1, 2)", font_size=17, color=COLOR_TRANS_E2, weight=BOLD).next_to(plane.c2p(1, 2), UL, buff=0.1)
        
        para_lbl = Text("Parallelogram\nArea = 3", font_size=16, color=COLOR_HIGHLIGHT, weight=BOLD).move_to(plane.c2p(1.5, 1.5))

        # Vertex dots and labels
        p0 = Dot(plane.c2p(0, 0), color=COLOR_TEXT, radius=0.07)
        p1 = Dot(plane.c2p(2, 1), color=COLOR_TRANS_E1, radius=0.07)
        p2 = Dot(plane.c2p(3, 3), color=COLOR_HIGHLIGHT, radius=0.07)
        p3 = Dot(plane.c2p(1, 2), color=COLOR_TRANS_E2, radius=0.07)
        
        v_lbl_p2 = Text("(3, 3)", font_size=16, color=COLOR_HIGHLIGHT, weight=BOLD).next_to(p2, UR, buff=0.1)

        self.play(FadeOut(sq_lbl), run_time=0.8)
        self.play(
            plane.animate.apply_matrix([[2, 1], [1, 2]]),
            Transform(e1_arr, target_e1_arr),
            Transform(e2_arr, target_e2_arr),
            Transform(lbl_e1, lbl_target_e1),
            Transform(lbl_e2, lbl_target_e2),
            Transform(unit_square, transformed_parallelogram),
            run_time=4.0
        )
        self.play(
            FadeIn(para_lbl),
            FadeIn(p0), FadeIn(p1), FadeIn(p2), FadeIn(p3),
            FadeIn(v_lbl_p2),
            run_time=1.5
        )
        self.wait(5.0)

        # 6. Callout Summary (8 seconds)
        summary_callout = Text(
            "Matrix columns ARE the landing sites of basis vectors!\nUnit square morphs into a parallelogram: (0,0) → (2,1) → (3,3) → (1,2)",
            font_size=20, color=COLOR_HIGHLIGHT, weight=BOLD, line_spacing=1.2
        ).to_edge(DOWN, buff=0.35)

        self.play(FadeIn(summary_callout), run_time=1.2)
        self.wait(4.5)

        # Clean exit
        self.play(
            FadeOut(plane), FadeOut(e1_arr), FadeOut(e2_arr),
            FadeOut(lbl_e1), FadeOut(lbl_e2), FadeOut(unit_square),
            FadeOut(para_lbl), FadeOut(p0), FadeOut(p1), FadeOut(p2), FadeOut(p3),
            FadeOut(v_lbl_p2), FadeOut(matrix_panel), FadeOut(summary_callout),
            FadeOut(header),
            run_time=1.5
        )
        self.wait(0.5)
