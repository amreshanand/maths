# Six-Scene Storyboard: Linear Transformations
**Project Title:** Linear Transformations: How Matrices Transform 2D Space  
**Course:** M3 Mathematics Animation Video Project  
**Student Name:** [ENTER STUDENT NAME]  
**Student ID:** [ENTER STUDENT ID]  
**Aspect Ratio:** 16:9 | **Target Resolution:** 1920 × 1080 | **Target Duration:** ~5 mins 10 secs

---

## Scene 1: Hook / Context
- **Duration:** 00:00 – 00:35 (~35s)
- **Learning Objective:** Engage the student by contrasting static numerical tables with dynamic spatial transformations, posing the core question: How does a matrix transform space?
- **Key Equations & Concepts:**
  - $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$
  - Question: *"How does a matrix reshape space?"*
- **Visual Description:**
  - Deep slate background (`#14141E`).
  - Coordinate plane with faint, elegant grid lines (`#2B2D42`).
  - A vector moves smoothly across the grid.
  - A dramatic morph illustrates the grid skewing and rotating into transformed space.
  - Title card appears with high-contrast typography, student name placeholder, and student ID placeholder.
- **Narration Summary:** Real-world motivation (computer graphics, game engines, physics) leading to the geometric interpretation of matrices.
- **Animation Sequence:**
  1. Fade in coordinate axes and grid.
  2. Spawn dynamic test vector navigating the plane.
  3. Warp the grid using a preliminary transformation.
  4. Display Title, Topic, Student Name, Student ID.
  5. Fade to black transition.
- **Transition:** Smooth cross-fade to Scene 2.

---

## Scene 2: Concept Introduction
- **Duration:** 00:35 – 01:25 (~50s)
- **Learning Objective:** Formally define a linear transformation: $T(\mathbf{v}) = A\mathbf{v}$, establishing the two fundamental conditions (additivity and homogeneity) and why the origin must be fixed.
- **Key Equations & Concepts:**
  - $T(\mathbf{v}) = A\mathbf{v}$
  - Additivity: $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$
  - Homogeneity: $T(c\mathbf{u}) = c\,T(\mathbf{u})$
  - Origin Preservation: $T(\mathbf{0}) = \mathbf{0}$
  - Non-example: Affine translation $T(\mathbf{v}) = \mathbf{v} + \mathbf{b}$ ($\mathbf{b} \ne \mathbf{0}$) moves origin $\implies$ non-linear.
- **Visual Description:**
  - Left panel: algebraic definitions with clean color highlights.
  - Right panel: animated vector addition parallelogram before and after transformation.
  - Scalar multiplication vector stretching smoothly.
  - Origin callout highlighting why $(0, 0) \to (0, 0)$ is mandatory.
- **Narration Summary:** Explaining transformations as vector functions and walking through linearity properties.
- **Animation Sequence:**
  1. Introduce function notation $T: \mathbb{R}^2 \to \mathbb{R}^2$ and $T(\mathbf{v}) = A\mathbf{v}$.
  2. Show two vectors $\mathbf{u}$ and $\mathbf{v}$ with tip-to-tail addition; transform both and show $T(\mathbf{u}+\mathbf{v})$.
  3. Animate scalar scaling $c\mathbf{u}$ and transformation.
  4. Highlight origin $(0,0)$ with a pulsing warning when a translation attempts to displace it.
- **Transition:** Slide transition into Scene 3.

---

## Scene 3: Visual Intuition
- **Duration:** 01:25 – 02:25 (~60s)
- **Learning Objective:** Establish the visual intuition that tracking standard basis vectors $\mathbf{e}_1$ and $\mathbf{e}_2$ fully determines the transformation of the entire plane.
- **Key Equations & Concepts:**
  - $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$
  - Chosen Matrix: $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$
  - Columns as basis targets: $T(\mathbf{e}_1) = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$, $T(\mathbf{e}_2) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$
  - Unit square: $(0,0), (1,0), (1,1), (0,1) \to$ Parallelogram: $(0,0), (2,1), (3,3), (1,2)$
- **Visual Description:**
  - Full coordinate plane with standard grid.
  - Vibrant red vector $\mathbf{e}_1$ and green vector $\mathbf{e}_2$.
  - Unit square filled with translucent cyan (`#4CC9F0`).
  - Smooth animation of the entire grid morphing continuously as $\mathbf{e}_1 \to (2, 1)$ and $\mathbf{e}_2 \to (1, 2)$.
  - Parallelogram shaded in translucent violet (`#9D4EDD`) with highlighted vertices.
- **Narration Summary:** Guiding viewer's focus to matrix columns as landing spots of basis vectors.
- **Animation Sequence:**
  1. Draw standard grid and highlight unit basis vectors $\mathbf{e}_1$ and $\mathbf{e}_2$.
  2. Display matrix $A$, highlighting column 1 in red and column 2 in green.
  3. Animate $\mathbf{e}_1 \to (2, 1)$ and $\mathbf{e}_2 \to (1, 2)$ while transforming the coordinate grid.
  4. Track the four corners of the unit square as it morphs into the parallelogram.
  5. Label transformed vertices: $(0,0)$, $(2,1)$, $(3,3)$, $(1,2)$.
- **Transition:** Wipe right to Scene 4.

---

## Scene 4: Worked Example
- **Duration:** 02:25 – 03:25 (~60s)
- **Learning Objective:** Walk through step-by-step matrix multiplication for two distinct test vectors, linking algebraic steps to geometric vector trajectories.
- **Key Equations & Concepts:**
  - $T(x, y) = \begin{pmatrix} 2x + y \\ x + 2y \end{pmatrix}$
  - Calculation 1: $A \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(1) \\ 1(1) + 2(1) \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$
  - Calculation 2: $A \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 2(2) + 1(-1) \\ 1(2) + 2(-1) \end{pmatrix} = \begin{pmatrix} 4 - 1 \\ 2 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$
- **Visual Description:**
  - Split screen: Left half displays step-by-step arithmetic reveals; right half displays coordinate plane.
  - Vector $\mathbf{v}_1 = (1, 1)$ in blue, animating to $(3, 3)$.
  - Vector $\mathbf{v}_2 = (2, -1)$ in gold, animating to $(3, 0)$ landing squarely on the x-axis.
- **Narration Summary:** Detailed walkthrough of arithmetic rows multiplying vector components.
- **Animation Sequence:**
  1. Present vector $\mathbf{v}_1 = (1, 1)$ on grid.
  2. Step-by-step matrix multiplication display for $\mathbf{v}_1$.
  3. Animate $\mathbf{v}_1$ stretching along diagonal to $(3, 3)$.
  4. Present vector $\mathbf{v}_2 = (2, -1)$ in quadrant IV.
  5. Step-by-step matrix multiplication display for $\mathbf{v}_2$.
  6. Animate $\mathbf{v}_2$ rotating and landing directly on the positive x-axis at $(3, 0)$.
- **Transition:** Morph transition to Scene 5.

---

## Scene 5: Interpretation (Determinant, Eigenvectors, & Area vs Rotation)
- **Duration:** 03:25 – 04:35 (~70s)
- **Learning Objective:** Deepen conceptual understanding of the determinant as area scaling, explore invariant directions (eigenvectors), and debunk the misconception that area preservation implies rotation.
- **Key Equations & Concepts:**
  - $\det(A) = (2)(2) - (1)(1) = 3$
  - Area scaling factor: $|\det(A)| = 3$ (Unit square area $1 \to 3$)
  - Orientation preservation: $\det(A) > 0$
  - Eigenvalue $\lambda_1 = 3$, direction $\mathbf{v} = (1, 1)$ (stretch factor 3)
  - Eigenvalue $\lambda_2 = 1$, direction $\mathbf{v} = (1, -1)$ (length preserved)
  - Squeeze Matrix: $B = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$, $\det(B) = 1$
  - Distinguish: Area preservation ($\det=1$) vs. Isometry / Rigid Rotation ($R^T R = I$)
- **Visual Description:**
  - Parallelogram area measurement graphic showing $3\times$ expansion of unit square.
  - Pink line along $(1, 1)$ demonstrating pure 3-fold elongation without rotation.
  - Blue line along $(1, -1)$ showing length invariant under $A$.
  - Comparison side-by-side: Unit square transforming under matrix $B$ into a $2 \times 0.5$ rectangle.
  - Length callouts showing width doubled and height halved while area remains 1.
- **Narration Summary:** Conceptual interpretation of determinant, eigenvectors, and why determinant 1 does not mean rotation.
- **Animation Sequence:**
  1. Reveal determinant formula and calculate $\det(A) = 3$.
  2. Overlay area grids showing 1 unit area expanding to 3 units.
  3. Highlight eigenvector $(1, 1)$ stretching $\times 3$.
  4. Highlight eigenvector $(1, -1)$ remaining unchanged in length.
  5. Introduce matrix $B$; animate unit square stretching into a $2 \times 0.5$ rectangle.
  6. Display callout: *"Area Preserved ($\det=1$), but NOT a Rigid Rotation (Lengths Changed)!"*
- **Transition:** Dissolve into Scene 6.

---

## Scene 6: Summary and Credits
- **Duration:** 04:35 – 05:10 (~35s)
- **Learning Objective:** Synthesize all core takeaways into a cohesive summary and display academic submission credits.
- **Key Equations & Concepts:**
  - Summary of: Matrix columns = Transformed basis vectors; $\det(A)$ = Area scaling; Linearity conditions; Eigenvector directions.
- **Visual Description:**
  - Elegant summary card with five bullet icons and crisp typography.
  - Closing frame with Course details, Project Title, Student Name, Student ID, software credits (Manim Community, Python, NumPy).
- **Narration Summary:** Final recap and formal sign-off.
- **Animation Sequence:**
  1. Sequentially reveal the 5 key takeaway points.
  2. Transition to closing credits frame.
  3. Fade out gracefully to black.
- **Transition:** Fade out to black.
