"""
Scene 6: Summary and Credits
Comprehensive recap of learning objectives, student metadata, and academic credits
"""

from manim import *
import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))
from config import STUDENT_NAME, STUDENT_ID, COURSE_NAME, VIDEO_TITLE
from helpers.theme import *
from helpers.grid_utils import create_scene_header

class Scene06Summary(Scene):
    def construct(self):
        apply_scene_style(self)

        # 1. Header (2 seconds)
        header = create_scene_header("Project Summary: Key Takeaways",
                                     "Reviewing the Geometry of 2D Linear Transformations")
        self.play(FadeIn(header), run_time=1.2)
        self.wait(1.5)

        # 2. Key Takeaways Bulleted Card (18 seconds)
        points = [
            ("1. Linearity Axioms:", "T(u + v) = T(u) + T(v) and T(c·u) = c·T(u); Origin T(0) = 0 is fixed."),
            ("2. Matrix Columns:", "Directly encode the transformed basis vectors T(e₁) and T(e₂)."),
            ("3. Grid Deformation:", "Straight parallel lines remain parallel; unit square morphs into parallelogram."),
            ("4. Determinant:", "Absolute value measures area scaling factor; positive sign preserves orientation."),
            ("5. Lengths vs. Area:", "Area preservation (det=1) does NOT imply distance preservation (isometry).")
        ]

        bullet_group = VGroup()
        for title, desc in points:
            b_title = Text(title, font_size=18, weight=BOLD, color=COLOR_HIGHLIGHT)
            b_desc = Text(desc, font_size=17, color=COLOR_TEXT)
            row = VGroup(b_title, b_desc).arrange(RIGHT, buff=0.2)
            bullet_group.add(row)

        bullet_group.arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(header, DOWN, buff=0.4)

        self.play(FadeIn(bullet_group, shift=UP * 0.2), run_time=2.5)
        self.wait(12.0)
        self.play(FadeOut(bullet_group), FadeOut(header), run_time=1.5)

        # 3. Final Academic Credits Frame (12 seconds)
        closing_title = Text(VIDEO_TITLE, font_size=32, weight=BOLD, color=COLOR_HIGHLIGHT)
        course_label = Text(COURSE_NAME, font_size=22, color=COLOR_TEXT)
        
        student_box = VGroup(
            Text(f"Student Name: {STUDENT_NAME}", font_size=22, weight=BOLD, color=COLOR_TEXT),
            Text(f"Student ID:   {STUDENT_ID}", font_size=22, weight=BOLD, color=COLOR_TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        credits_box = VGroup(
            Text("Engine: Manim Community Edition  |  Language: Python 3.12", font_size=17, color=COLOR_MUTED),
            Text("Computation: NumPy 2.x  |  Rendering: FFmpeg", font_size=17, color=COLOR_MUTED),
            Text("Audio Synthesis: Neural TTS  |  Music: CC0 Minimalist Soundtrack", font_size=17, color=COLOR_MUTED)
        ).arrange(DOWN, buff=0.15)

        closing_card = VGroup(course_label, closing_title, student_box, credits_box).arrange(
            DOWN, buff=0.45
        ).move_to(ORIGIN)

        self.play(FadeIn(closing_card, shift=UP * 0.3), run_time=2.0)
        self.wait(7.0)
        self.play(FadeOut(closing_card), run_time=2.0)
        self.wait(1.0)
