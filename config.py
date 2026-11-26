"""
Project Configuration for M3 Mathematics Animation Video Project
Topic: Linear Transformations: How Matrices Transform 2D Space
"""

import os
from pathlib import Path

# Student Details - As specified in the master prompt
STUDENT_NAME = "[ENTER STUDENT NAME]"
STUDENT_ID = "[ENTER STUDENT ID]"
COURSE_NAME = "M3 Mathematics Animation Video Project"
TOPIC = "Linear Transformations"
VIDEO_TITLE = "Linear Transformations: How Matrices Transform 2D Space"

# Video Specifications
VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
VIDEO_RESOLUTION = f"{VIDEO_WIDTH}x{VIDEO_HEIGHT}"
ASPECT_RATIO = "16:9"
FRAME_RATE = 60
OUTPUT_FORMAT = "mp4"
VIDEO_CODEC = "libx264"
AUDIO_CODEC = "aac"
TARGET_DURATION_SECONDS = 300  # ~5 minutes (under 7 minutes maximum)

# Directory Paths
PROJECT_ROOT = Path(__file__).parent.resolve()
SRC_DIR = PROJECT_ROOT / "src"
ASSETS_DIR = PROJECT_ROOT / "assets"
AUDIO_DIR = ASSETS_DIR / "audio"
MUSIC_DIR = ASSETS_DIR / "music"
OUTPUT_DIR = PROJECT_ROOT / "output"
STORYBOARD_DIR = PROJECT_ROOT / "storyboard"
DOCS_DIR = PROJECT_ROOT / "documentation"
TESTS_DIR = PROJECT_ROOT / "tests"

# Mathematical Constants & Matrices
MATRIX_A = [[2, 1], [1, 2]]
MATRIX_B_SQUEEZE = [[2, 0], [0, 0.5]]

# Basis Vectors
BASIS_E1 = [1, 0]
BASIS_E2 = [0, 1]

# Worked Example Vectors
VECTOR_V1 = [1, 1]
VECTOR_V2 = [2, -1]

# Eigenvalues & Eigenvectors for Matrix A
EIGENVALUES_A = [3.0, 1.0]
EIGENVECTORS_A = [[1.0, 1.0], [1.0, -1.0]]

# Theme & Palette
COLOR_THEME = {
    "background": "#14141E",         # Deep slate dark background
    "grid": "#2B2D42",               # Subtle grid lines
    "grid_transformed": "#415A77",   # Subtle transformed grid
    "axis": "#8D99AE",               # Axes color
    "basis_e1": "#EF233C",           # Vivid Red for e1 / x-basis
    "basis_e2": "#04D361",           # Vivid Green for e2 / y-basis
    "trans_e1": "#FF6B6B",           # Transformed e1
    "trans_e2": "#51CF66",           # Transformed e2
    "vector_v1": "#3A86FF",          # Blue for v1
    "vector_v2": "#FFBE0B",          # Yellow for v2
    "unit_square": "#4CC9F0",        # Cyan fill for unit square
    "transformed_poly": "#8338EC",   # Purple fill for transformed parallelogram
    "text": "#EDF2F4",               # Bright readable off-white
    "text_muted": "#8D99AE",         # Secondary text
    "highlight": "#FFD166",          # Golden highlight
    "eigen_1": "#F72585",            # Hot pink for lambda=3
    "eigen_2": "#4895EF",            # Azure for lambda=1
}
