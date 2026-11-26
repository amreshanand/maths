"""
Scene 1: Hook / Context
Linear Transformations: How Matrices Transform 2D Space
"""

from manim import *
import numpy as np
import sys
from pathlib import Path

# Add project root to path for imports
sys.path.append(str(Path(__file__).parent.parent.resolve()))
from config import STUDENT_NAME, STUDENT_ID, COURSE_NAME, VIDEO_TITLE
from helpers.theme import *
from helpers.grid_utils import create_styled_plane

class Scene01Hook(Scene):
    def construct(self):
        apply_scene_style(self)

        # 1. Opening Title & Student Metadata Card (5 seconds)
        title_main = Text(VIDEO_TITLE, font_size=36, weight=BOLD, color=COLOR_HIGHLIGHT)
        course_txt = Text(COURSE_NAME, font_size=24, color=COLOR_TEXT)
        student_txt = Text(f"Student: {STUDENT_NAME}   |   ID: {STUDENT_ID}", font_size=22, color=COLOR_MUTED)
        
        title_card = VGroup(course_txt, title_main, student_txt).arrange(DOWN, buff=0.4)
        
        self.play(FadeIn(title_card, shift=UP * 0.3), run_time=2.0)
        self.wait(3.0)
        self.play(FadeOut(title_card, shift=UP * 0.5), run_time=1.5)

        # 2. Hook Question & Real-World Motivation (7 seconds)
        hook_question = Text("How can a simple table of numbers\nreshape an entire geometric space?", 
                             font_size=32, weight=BOLD, color=COLOR_TEXT, line_spacing=1.3)
        self.play(Write(hook_question), run_time=2.0)
        self.wait(3.0)
        self.play(hook_question.animate.to_edge(UP, buff=0.4).scale(0.75), run_time=1.5)

        # 3. Introduce Standard 2D Coordinate Grid (6 seconds)
        plane = create_styled_plane(x_range=(-5, 5, 1), y_range=(-3, 3, 1), x_length=10, y_length=6)
        plane.shift(DOWN * 0.3)
        
        x_label = Text("x", font_size=20, color=AXIS_COLOR).next_to(plane.get_x_axis().get_end(), RIGHT)
        y_label = Text("y", font_size=20, color=AXIS_COLOR).next_to(plane.get_y_axis().get_end(), UP)
        
        self.play(Create(plane, run_time=2.0), FadeIn(x_label), FadeIn(y_label))
        self.wait(2.0)

        # 4. Animate a vector moving across the grid (6 seconds)
        v_coords = np.array([2.0, 1.5, 0.0])
        v_arrow = Arrow(plane.c2p(0, 0), plane.c2p(*v_coords[:2]), buff=0, color=COLOR_V1, stroke_width=4.5)
        v_lbl = Text("v", font_size=22, color=COLOR_TRANS_V1, weight=BOLD).next_to(v_arrow.get_end(), UR, buff=0.1)
        
        self.play(GrowArrow(v_arrow), FadeIn(v_lbl), run_time=1.5)
        self.wait(1.0)
        
        # Move vector dynamically across the plane
        target_coords = np.array([-1.5, 2.0, 0.0])
        self.play(
            v_arrow.animate.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(*target_coords[:2])),
            v_lbl.animate.next_to(plane.c2p(*target_coords[:2]), UL, buff=0.1),
            run_time=2.0
        )
        self.wait(1.5)

        # 5. Dramatic Grid Deformation into Transformed Space (7 seconds)
        # Apply transformation matrix [[2, 1], [1, 2]] smoothly to grid and vector
        warp_matrix = [[2.0, 1.0], [1.0, 2.0]]
        
        caption_trans = Text("A matrix acts as a geometric engine: warping space!", 
                             font_size=24, color=COLOR_HIGHLIGHT, weight=BOLD).to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(caption_trans), run_time=1.0)
        
        # Smoothly apply transformation to the plane and vector
        self.play(
            plane.animate.apply_matrix(warp_matrix),
            v_arrow.animate.put_start_and_end_on(plane.c2p(0, 0), plane.c2p(-1.0, 2.5)),
            run_time=3.5
        )
        self.wait(2.0)

        # 6. Conclusion of Scene 1 Transition (2 seconds)
        self.play(
            FadeOut(plane),
            FadeOut(v_arrow),
            FadeOut(v_lbl),
            FadeOut(hook_question),
            FadeOut(caption_trans),
            FadeOut(x_label),
            FadeOut(y_label),
            run_time=1.5
        )
        self.wait(0.5)
