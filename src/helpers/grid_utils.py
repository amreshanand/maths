"""
Grid and Mathematical Typography Utilities for Manim (Pango/Cairo based)
Provides helper functions for matrix formatting, vector displays, and styled coordinate grids.
"""

from manim import *
import numpy as np
from .theme import *

def create_styled_plane(
    x_range=(-5, 5, 1),
    y_range=(-4, 4, 1),
    x_length=10,
    y_length=8,
    faded_line_ratio=1,
    axis_config=None,
    background_line_style=None
):
    """Creates a cleanly styled 2D NumberPlane adhering to the project theme."""
    bg_style = {
        "stroke_color": GRID_COLOR,
        "stroke_width": 1.2,
        "stroke_opacity": 0.6
    }
    if background_line_style:
        bg_style.update(background_line_style)

    ax_config = {
        "color": AXIS_COLOR,
        "stroke_width": 2.2,
        "include_numbers": False,
        "tip_width": 0.18,
        "tip_height": 0.18,
    }
    if axis_config:
        ax_config.update(axis_config)

    plane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        background_line_style=bg_style,
        faded_line_ratio=faded_line_ratio,
        axis_config=ax_config
    )
    return plane

def create_matrix_mobject(matrix_data, col_colors=None, font_size=32, font="sans-serif"):
    """
    Creates a beautifully formatted 2x2 matrix with brackets and color-coded columns.
    Uses pure Text/VGroup so it has 0 dependencies on external LaTeX compilers.
    """
    rows = len(matrix_data)
    cols = len(matrix_data[0])
    
    entries = VGroup()
    col_groups = [VGroup() for _ in range(cols)]
    
    for r in range(rows):
        for c in range(cols):
            val = matrix_data[r][c]
            val_str = f"{val:g}" if isinstance(val, (int, float)) else str(val)
            color = COLOR_TEXT
            if col_colors and c < len(col_colors):
                color = col_colors[c]
            txt = Text(val_str, font_size=font_size, color=color, weight=BOLD)
            entries.add(txt)
            col_groups[c].add(txt)
            
    # Arrange in grid
    grid = VGroup(*entries).arrange_in_grid(rows=rows, cols=cols, buff=(0.45, 0.35))
    
    # Left and Right brackets
    bracket_h = grid.height + 0.3
    bracket_w = 0.18
    stroke_w = 2.8
    
    # Left Bracket: [
    left_top = grid.get_corner(UL) + LEFT * 0.15 + UP * 0.15
    left_bot = grid.get_corner(DL) + LEFT * 0.15 + DOWN * 0.15
    lb_path = VMobject(color=COLOR_TEXT, stroke_width=stroke_w)
    lb_path.set_points_as_corners([
        left_top + RIGHT * bracket_w,
        left_top,
        left_bot,
        left_bot + RIGHT * bracket_w
    ])
    
    # Right Bracket: ]
    right_top = grid.get_corner(UR) + RIGHT * 0.15 + UP * 0.15
    right_bot = grid.get_corner(DR) + RIGHT * 0.15 + DOWN * 0.15
    rb_path = VMobject(color=COLOR_TEXT, stroke_width=stroke_w)
    rb_path.set_points_as_corners([
        right_top + LEFT * bracket_w,
        right_top,
        right_bot,
        right_bot + LEFT * bracket_w
    ])
    
    matrix_group = VGroup(lb_path, grid, rb_path)
    return matrix_group

def create_col_vector_mobject(vec_data, color=COLOR_TEXT, font_size=30):
    """Creates a 2x1 column vector representation [x; y]."""
    entries = [Text(f"{v:g}" if isinstance(v, (int, float)) else str(v), 
                    font_size=font_size, color=color, weight=BOLD) for v in vec_data]
    col = VGroup(*entries).arrange(DOWN, buff=0.3)
    
    bracket_w = 0.14
    stroke_w = 2.4
    
    left_top = col.get_corner(UL) + LEFT * 0.12 + UP * 0.12
    left_bot = col.get_corner(DL) + LEFT * 0.12 + DOWN * 0.12
    lb = VMobject(color=COLOR_TEXT, stroke_width=stroke_w).set_points_as_corners([
        left_top + RIGHT * bracket_w,
        left_top,
        left_bot,
        left_bot + RIGHT * bracket_w
    ])
    
    right_top = col.get_corner(UR) + RIGHT * 0.12 + UP * 0.12
    right_bot = col.get_corner(DR) + RIGHT * 0.12 + DOWN * 0.12
    rb = VMobject(color=COLOR_TEXT, stroke_width=stroke_w).set_points_as_corners([
        right_top + LEFT * bracket_w,
        right_top,
        right_bot,
        right_bot + LEFT * bracket_w
    ])
    return VGroup(lb, col, rb)

def create_scene_header(title_text, subtitle_text=None):
    """Creates a consistent, professional header across all scenes."""
    title = Text(title_text, font_size=32, weight=BOLD, color=COLOR_TEXT)
    line = Line(LEFT * 6.5, RIGHT * 6.5, stroke_width=1.5, color=AXIS_COLOR)
    header_group = VGroup(title, line).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.35)
    
    if subtitle_text:
        sub = Text(subtitle_text, font_size=20, color=COLOR_MUTED)
        header_group = VGroup(title, sub, line).arrange(DOWN, buff=0.12).to_edge(UP, buff=0.3)
        
    return header_group
