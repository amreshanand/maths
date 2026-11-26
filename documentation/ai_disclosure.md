# AI Disclosure Statement
**Project Title:** Linear Transformations: How Matrices Transform 2D Space  
**Course:** M3 Mathematics Animation Video Project  
**Student Name:** [ENTER STUDENT NAME]  
**Student ID:** [ENTER STUDENT ID]  

---

## Declaration of Tool Usage

In compliance with academic integrity guidelines and project requirements, this document outlines the extent and nature of AI assistance utilized during the planning, authoring, and production of this M3 Mathematics Animation Video Project.

### 1. Scripting and Ideation
- **Role of AI:** Assisted in drafting initial storyboard outlines, structuring pedagogical flow according to the 6-scene master specification, and formulating comprehensive viva preparation questions.
- **Human / Student Oversight:** All mathematical formulations, definitions, examples, and educational goals were strictly checked against standard linear algebra textbooks (Strang, Axler, Lay).

### 2. Manim Python Development
- **Role of AI:** Assisted in generating modular boilerplate code for Manim scene classes, coordinate grid transforms, and FFmpeg video pipeline scripts.
- **Verification:** All visual code was executed, inspected frame-by-frame, and debugged locally to ensure seamless rendering without artifacting, overlapping text, or incorrect geometric representations.

### 3. Voiceover & Audio
- **Narration Audio:** The narration voice tracks were generated using high-fidelity Neural Text-to-Speech (Edge-TTS `en-US-ChristopherNeural` / `en-US-GuyNeural`). No human voice actor was recorded. This is transparently disclosed in accordance with requirement 6 of the project prompt.
- **Background Music:** An ambient, minimalist instrumental soundtrack was rendered programmatically / derived from CC0 royalty-free public domain ambient audio beds.

### 4. Mathematical Verification
- All mathematical assertions (including matrix multiplications, standard basis projections, unit square vertex mapping, determinants, eigenvalue/eigenvector decompositions, and the non-isometry of determinant-1 squeeze matrices) were tested and independently validated using a standalone NumPy test suite (`tests/verify_transformations.py`).
- 100% of mathematical test assertions passed without discrepancy.
