"""
Scene 5: Interpretation
Determinant (Area Scaling), Eigenvectors (Invariant Directions), and Area Preservation vs. Rotation
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
    create_matrix_mobject
)

class Scene05Interpretation(Scene):
    def construct(self):
        apply_scene_style(self)

        # 1. Header (3 seconds)
        header = create_scene_header("Geometric Interpretation: Determinant & Eigenstructure",
                                     "Area Scaling, Invariant Axes, and Area vs Distance Preservation")
        self.play(FadeIn(header), run_time=1.2)
        self.wait(1.8)

        # 2. Section A: Determinant & Area Scaling (22 seconds)
        det_panel = VGroup(
            Text("Determinant = Area Scaling Factor", font_size=24, weight=BOLD, color=COLOR_HIGHLIGHT),
            Text("det(A) = (2 · 2) - (1 · 1) = 4 - 1 = 3", font_size=22, weight=BOLD, color=COLOR_TEXT),
            Text("• Original Unit Square Area = 1", font_size=19, color=COLOR_SQUARE),
            Text("• Transformed Parallelogram Area = 3", font_size=19, color=COLOR_PARALLELOGRAM),
            Text("• det(A) > 0  ⟹  Orientation is Preserved!", font_size=19, weight=BOLD, color=COLOR_E2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(LEFT, buff=0.6).shift(UP * 0.2)

        plane_a = create_styled_plane(
            x_range=(-1, 4, 1),
            y_range=(-1, 4, 1),
            x_length=5.5,
            y_length=5.0
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.2)

        # Unit square vs transformed parallelogram
        u_sq = Polygon(plane_a.c2p(0, 0), plane_a.c2p(1, 0), plane_a.c2p(1, 1), plane_a.c2p(0, 1),
                       color=COLOR_SQUARE, fill_color=COLOR_SQUARE, fill_opacity=0.35, stroke_width=2.5)
        u_sq_lbl = Text("Area = 1", font_size=15, color=COLOR_SQUARE, weight=BOLD).move_to(plane_a.c2p(0.5, 0.5))

        trans_para = Polygon(plane_a.c2p(0, 0), plane_a.c2p(2, 1), plane_a.c2p(3, 3), plane_a.c2p(1, 2),
                             color=COLOR_PARALLELOGRAM, fill_color=COLOR_PARALLELOGRAM, fill_opacity=0.4, stroke_width=3.0)
        para_lbl = Text("Area = 3\n(Tripled!)", font_size=16, color=COLOR_HIGHLIGHT, weight=BOLD).move_to(plane_a.c2p(1.5, 1.5))

        self.play(FadeIn(det_panel), Create(plane_a), DrawBorderThenFill(u_sq), FadeIn(u_sq_lbl), run_time=2.0)
        self.wait(2.5)
        self.play(Transform(u_sq, trans_para), Transform(u_sq_lbl, para_lbl), run_time=2.5)
        self.wait(3.5)

        # Clear Section A
        self.play(
            FadeOut(det_panel),
            FadeOut(plane_a),
            FadeOut(u_sq),
            FadeOut(u_sq_lbl),
            run_time=1.2
        )

        # 3. Section B: Eigenvalues and Eigenvector Directions (22 seconds)
        eigen_panel = VGroup(
            Text("Eigenvectors: Invariant Directions", font_size=24, weight=BOLD, color=COLOR_HIGHLIGHT),
            Text("Directions where A acts as pure scaling (no turning):", font_size=18, color=COLOR_TEXT),
            Text("1. λ₁ = 3, direction v = (1, 1)ᵀ", font_size=20, weight=BOLD, color=COLOR_EIGEN_3),
            Text("   ⟹ Stretched by factor of 3!", font_size=17, color=COLOR_MUTED),
            Text("2. λ₂ = 1, direction v = (1, -1)ᵀ", font_size=20, weight=BOLD, color=COLOR_EIGEN_1),
            Text("   ⟹ Length perfectly preserved!", font_size=17, color=COLOR_MUTED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).to_edge(LEFT, buff=0.6).shift(UP * 0.2)

        plane_b = create_styled_plane(
            x_range=(-3, 4, 1),
            y_range=(-3, 4, 1),
            x_length=5.5,
            y_length=5.0
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.2)

        # Eigenvector 1: along (1, 1)
        ev1_line = Line(plane_b.c2p(-2.5, -2.5), plane_b.c2p(3.5, 3.5), color=COLOR_EIGEN_3, stroke_width=2.0, stroke_opacity=0.6)
        ev1_vec = Arrow(plane_b.c2p(0, 0), plane_b.c2p(1, 1), buff=0, color=COLOR_EIGEN_3, stroke_width=4.0)
        ev1_scaled = Arrow(plane_b.c2p(0, 0), plane_b.c2p(3, 3), buff=0, color=COLOR_EIGEN_3, stroke_width=4.5)
        ev1_lbl = Text("λ = 3 (×3 stretch)", font_size=16, color=COLOR_EIGEN_3, weight=BOLD).next_to(plane_b.c2p(3, 3), UR, buff=0.1)

        # Eigenvector 2: along (1, -1)
        ev2_line = Line(plane_b.c2p(-2.5, 2.5), plane_b.c2p(2.5, -2.5), color=COLOR_EIGEN_1, stroke_width=2.0, stroke_opacity=0.6)
        ev2_vec = Arrow(plane_b.c2p(0, 0), plane_b.c2p(1, -1), buff=0, color=COLOR_EIGEN_1, stroke_width=4.0)
        ev2_lbl = Text("λ = 1 (length preserved)", font_size=16, color=COLOR_EIGEN_1, weight=BOLD).next_to(plane_b.c2p(1, -1), DR, buff=0.1)

        self.play(FadeIn(eigen_panel), Create(plane_b), Create(ev1_line), Create(ev2_line), run_time=2.0)
        self.play(GrowArrow(ev1_vec), GrowArrow(ev2_vec), FadeIn(ev2_lbl), run_time=1.5)
        self.wait(1.5)
        self.play(Transform(ev1_vec, ev1_scaled), FadeIn(ev1_lbl), run_time=2.0)
        self.wait(3.5)

        # Clear Section B
        self.play(
            FadeOut(eigen_panel),
            FadeOut(plane_b),
            FadeOut(ev1_line),
            FadeOut(ev2_line),
            FadeOut(ev1_vec),
            FadeOut(ev2_vec),
            FadeOut(ev1_lbl),
            FadeOut(ev2_lbl),
            run_time=1.2
        )

        # 4. Section C: Squeeze Transformation - Area vs. Distance Preservation (24 seconds)
        squeeze_title = Text("Critical Distinction: Area Preservation vs. Rotation", 
                             font_size=24, weight=BOLD, color=COLOR_WARN).to_edge(UP, buff=1.2)
        
        matrix_b_card = VGroup(
            Text("Squeeze Matrix B = [[2, 0], [0, 0.5]]", font_size=20, weight=BOLD, color=COLOR_TEXT),
            Text("det(B) = (2 · 0.5) - 0 = 1", font_size=20, weight=BOLD, color=COLOR_HIGHLIGHT),
            Text("• Area is preserved (Area = 1)", font_size=18, color=COLOR_E2),
            Text("• Horizontal lengths: 1 → 2 (Doubled!)", font_size=18, color=COLOR_WARN),
            Text("• Vertical lengths: 1 → 0.5 (Halved!)", font_size=18, color=COLOR_WARN),
            Text("det = 1 DOES NOT MEAN ROTATION!", font_size=20, weight=BOLD, color=COLOR_WARN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).to_edge(LEFT, buff=0.8).shift(DOWN * 0.3)

        plane_c = create_styled_plane(
            x_range=(-1, 4, 1),
            y_range=(-1, 2.5, 1),
            x_length=5.5,
            y_length=4.0
        ).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.3)

        orig_sq_b = Polygon(plane_c.c2p(0, 0), plane_c.c2p(1, 0), plane_c.c2p(1, 1), plane_c.c2p(0, 1),
                            color=COLOR_SQUARE, fill_color=COLOR_SQUARE, fill_opacity=0.35, stroke_width=2.5)
        rect_b = Polygon(plane_c.c2p(0, 0), plane_c.c2p(2, 0), plane_c.c2p(2, 0.5), plane_c.c2p(0, 0.5),
                         color=COLOR_HIGHLIGHT, fill_color=COLOR_HIGHLIGHT, fill_opacity=0.45, stroke_width=3.0)
        
        rect_lbl = Text("Rectangle: 2 × 0.5\nArea = 1", font_size=15, color=COLOR_TEXT, weight=BOLD).move_to(plane_c.c2p(1.0, 0.25))

        self.play(FadeIn(squeeze_title), FadeIn(matrix_b_card), Create(plane_c), DrawBorderThenFill(orig_sq_b), run_time=2.0)
        self.wait(2.0)
        self.play(Transform(orig_sq_b, rect_b), FadeIn(rect_lbl), run_time=2.5)
        self.wait(4.5)

        # Clean exit
        self.play(
            FadeOut(squeeze_title),
            FadeOut(matrix_b_card),
            FadeOut(plane_c),
            FadeOut(orig_sq_b),
            FadeOut(rect_lbl),
            FadeOut(header),
            run_time=1.5
        )
        self.wait(0.5)
