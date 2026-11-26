"""
Theme and visual styling for Manim animations
"""

from manim import *

# Color Palette
BG_COLOR = "#14141E"
GRID_COLOR = "#2B2D42"
GRID_TRANS_COLOR = "#415A77"
AXIS_COLOR = "#8D99AE"

COLOR_E1 = "#EF233C"         # Red for e1 (1, 0)
COLOR_E2 = "#04D361"         # Green for e2 (0, 1)
COLOR_TRANS_E1 = "#FF6B6B"   # Bright salmon red for T(e1)
COLOR_TRANS_E2 = "#51CF66"   # Bright lime green for T(e2)

COLOR_V1 = "#3A86FF"         # Blue for v1 (1, 1)
COLOR_TRANS_V1 = "#70B8FF"   # Light blue for T(v1)

COLOR_V2 = "#FFBE0B"         # Gold for v2 (2, -1)
COLOR_TRANS_V2 = "#FFE066"   # Light gold for T(v2)

COLOR_SQUARE = "#4CC9F0"     # Cyan for unit square
COLOR_PARALLELOGRAM = "#9D4EDD" # Violet for transformed parallelogram

COLOR_EIGEN_3 = "#F72585"    # Vivid pink for lambda=3
COLOR_EIGEN_1 = "#4895EF"    # Vivid blue for lambda=1

COLOR_TEXT = "#EDF2F4"       # Primary text
COLOR_MUTED = "#8D99AE"      # Secondary text
COLOR_HIGHLIGHT = "#FFD166"  # Callout/Accent
COLOR_WARN = "#FF5964"       # Warning / Non-example

def apply_scene_style(scene: Scene):
    """Sets standard background and camera styling for a scene."""
    scene.camera.background_color = BG_COLOR
