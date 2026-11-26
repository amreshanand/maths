# Linear Transformations: How Matrices Transform 2D Space
### M3 Mathematics Animation Video Project

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Manim Community](https://img.shields.io/badge/manim-v0.22.1-orange.svg)](https://www.manim.community/)
[![NumPy](https://img.shields.io/badge/numpy-2.x-green.svg)](https://numpy.org/)
[![FFmpeg](https://img.shields.io/badge/ffmpeg-v9.1-red.svg)](https://ffmpeg.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 1. Project Overview
This repository contains the complete, production-grade source code, assets, mathematical verification suite, storyboard, narration scripts, and rendering pipeline for the **M3 Mathematics Animation Video Project**:
**"Linear Transformations: How Matrices Transform 2D Space"**.

The project visually explains *why* matrices alter geometric space rather than presenting static formulas. Following the required six-scene educational progression, it demonstrates how standard basis vectors determine full-plane transformations, explores the geometric meaning of the determinant as an area scaling factor, visualizes eigenspaces, and clarifies the crucial distinction between area preservation ($\det = 1$) and rigid rotations (isometries).

---

## 2. Student & Submission Configuration
- **Student Name:** `[ENTER STUDENT NAME]`
- **Student ID:** `[ENTER STUDENT ID]`
- **Course / Project:** M3 Mathematics Animation Video Project
- **Topic:** Linear Transformations
- **Video Title:** Linear Transformations: How Matrices Transform 2D Space
- **Video Specifications:** 1920 × 1080 (16:9), 60 FPS, H.264 Video / AAC Audio
- **Final Output Location:** `output/Linear_Transformations_Final.mp4`

---

## 3. Mathematical Scope and Key Findings
1. **Linear Transformation Definition:** $T: \mathbb{R}^2 \to \mathbb{R}^2$ represented by $T(\mathbf{v}) = A\mathbf{v}$.
2. **Linearity Axioms:**
   - Additivity: $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
   - Homogeneity: $T(c\mathbf{u}) = c\,T(\mathbf{u})$
   - Origin Fixation: $T(\mathbf{0}) = \mathbf{0}$ (shifts like $T(\mathbf{v}) = \mathbf{v} + \mathbf{b}$ are affine, non-linear).
3. **Primary Transformation Matrix:**
   $$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$
4. **Basis Vector Tracking:**
   $$\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \implies T(\mathbf{e}_1) = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \quad \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \implies T(\mathbf{e}_2) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
   *Columns of $A$ are precisely the transformed standard basis vectors.*
5. **Unit Square to Parallelogram:**
   The unit square with vertices $(0, 0), (1, 0), (1, 1), (0, 1)$ transforms into a parallelogram with vertices:
   $$(0, 0), (2, 1), (3, 3), (1, 2)$$
6. **Worked Examples:**
   - $\mathbf{v}_1 = (1, 1)^T \implies A\mathbf{v}_1 = (3, 3)^T$
   - $\mathbf{v}_2 = (2, -1)^T \implies A\mathbf{v}_2 = (3, 0)^T$ (lands directly on horizontal x-axis)
7. **Determinant and Area Scaling:**
   $$\det(A) = (2)(2) - (1)(1) = 3$$
   - Area scaling factor: $|\det(A)| = 3$ (Unit square area $1 \to 3$).
   - Positive determinant confirms that spatial orientation is preserved.
8. **Eigenspace Analysis:**
   - $\lambda_1 = 3$, eigenvector direction $(1, 1)^T$: 3-fold stretch without rotation.
   - $\lambda_2 = 1$, eigenvector direction $(1, -1)^T$: invariant length.
9. **Squeeze Transformation & Isometry Distinction:**
   $$B = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}, \quad \det(B) = 1.0$$
   - Area is preserved ($\text{Area} = 2 \times 0.5 = 1.0$).
   - Side lengths change (width doubled, height halved).
   - $B^T B \ne I \implies$ **Area preservation ($\det=1$) does NOT imply distance preservation (rigid rotation/isometry).**

---

## 4. Six-Scene Storyboard Architecture
- **Scene 1: Hook / Context (~35s)** — Real-world motivation (gaming, physics, computer graphics), vector motion, dramatic grid deformation, and project title/student metadata card.
- **Scene 2: Concept Introduction (~50s)** — Input/output mapping, additivity, homogeneity, and why $T(\mathbf{0}) = \mathbf{0}$ is mandatory.
- **Scene 3: Visual Intuition (~60s)** — Standard basis vectors $\mathbf{e}_1, \mathbf{e}_2$, columns of $A$ as landing sites, and smooth grid morph into a parallelogram.
- **Scene 4: Worked Example (~60s)** — Step-by-step arithmetic multiplication for $\mathbf{v}_1 = (1, 1)$ and $\mathbf{v}_2 = (2, -1)$ linked to animated trajectories.
- **Scene 5: Interpretation (~70s)** — Determinant area tripling, eigenvector scaling, and contrast between area preservation ($\det=1$) and rigid rotations.
- **Scene 6: Summary & Credits (~35s)** — Synthesis of 5 core principles, academic credits, and closing sign-off.

---

## 5. Repository Structure
```
maths/
├── README.md                               # Project documentation and guide
├── requirements.txt                        # Python dependencies
├── config.py                               # Central project configuration & metadata
│
├── src/                                    # Modular Manim scene source code
│   ├── main.py                             # Master CLI pipeline runner
│   ├── scene_01_hook.py                    # Scene 1: Hook & context
│   ├── scene_02_concept.py                 # Scene 2: Concept & axioms
│   ├── scene_03_visual_intuition.py        # Scene 3: Basis vectors & grid morph
│   ├── scene_04_worked_example.py          # Scene 4: Step-by-step arithmetic
│   ├── scene_05_interpretation.py          # Scene 5: Determinant, eigenvalues, squeeze
│   ├── scene_06_summary.py                 # Scene 6: Summary & credits
│   └── helpers/                            # Reusable Manim styling & grid components
│       ├── __init__.py
│       ├── theme.py                        # Color palette & styling
│       └── grid_utils.py                   # Typography & vector/matrix builders
│
├── scripts/                                # Audio synthesis & render pipelines
│   ├── generate_music.py                   # Procedural ambient soundtrack generator
│   ├── generate_audio.py                   # Neural TTS narration generator
│   ├── generate_storyboard_pdf.py          # Storyboard PDF compilation (ReportLab)
│   └── render_and_mux.py                   # Full 1080p rendering & soundtrack muxing
│
├── assets/                                 # Audio and multimedia assets
│   ├── audio/                              # Scene-by-scene narration MP3s
│   ├── music/                              # Ambient background soundtrack
│   └── other_assets/
│
├── output/                                 # Final rendered deliverable
│   └── Linear_Transformations_Final.mp4    # 1080p60 full video (~5 mins)
│
├── storyboard/                             # Storyboard deliverables
│   ├── storyboard.md                       # Markdown storyboard
│   └── storyboard.pdf                      # Polished publication PDF
│
├── documentation/                          # Academic documentation & viva prep
│   ├── narration_script.md                 # Complete spoken narration script
│   ├── mathematical_verification.md        # Formula verification & proof report
│   ├── viva_questions.md                   # 25 Viva Voce Q&As with detailed answers
│   ├── credits.md                          # Academic & software attributions
│   └── ai_disclosure.md                    # Transparent AI tool usage statement
│
└── tests/                                  # Numerical verification suite
    └── verify_transformations.py           # NumPy verification tests (9 tests)
```

---

## 6. Installation & Environment Setup

### System Prerequisites
- **Operating System:** macOS, Linux, or Windows (WSL recommended)
- **Python:** 3.12+
- **System Libraries:** FFmpeg, Pango, Cairo, pkg-config

On macOS with Homebrew:
```bash
brew install ffmpeg pango cairo pkg-config
```

### Python Virtual Environment
```bash
# Clone the repository
git clone https://github.com/amreshanand/maths.git
cd maths

# Create virtual environment with uv or python venv
python3.12 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 7. Execution and Rendering Instructions

### A. Run Mathematical Verification Tests
```bash
python tests/verify_transformations.py
```
*Executes all 9 independent matrix, basis, area, eigenvalue, and linearity tests.*

### B. Generate Narration & Music
```bash
python scripts/generate_music.py
python scripts/generate_audio.py
```

### C. Compile Storyboard PDF
```bash
python scripts/generate_storyboard_pdf.py
```

### D. Render Complete 1080p Video & Mux Audio
```bash
python scripts/render_and_mux.py
```
*Or execute the master pipeline:*
```bash
python src/main.py --all
```
The final video will be generated at `output/Linear_Transformations_Final.mp4`.

---

## 8. Verification and Quality Control
- **Mathematical Rigor:** 9/9 automated tests passing with zero discrepancies.
- **Video Standards:** 1920 × 1080 resolution, 60.0 FPS, H.264 video encoding, AAC 192kbps stereo audio.
- **Duration:** Approximately 5 minutes 10 seconds (well within 5–7 minute requirement).
- **Audio Mix:** Crystal-clear vocal narration with subtle ambient background score mixed at -22 dB.

---

## 9. Academic Credits & AI Disclosure
- **Mathematical Foundations:** Gilbert Strang (*Introduction to Linear Algebra*), Sheldon Axler (*Linear Algebra Done Right*), 3Blue1Brown (*Essence of Linear Algebra*).
- **Animation Framework:** Manim Community Edition (MIT License).
- **AI Disclosure:** Detailed in [`documentation/ai_disclosure.md`](documentation/ai_disclosure.md) in full accordance with academic transparency standards.
- **Viva Voce Preparation:** 25 comprehensive model Q&As available in [`documentation/viva_questions.md`](documentation/viva_questions.md).
