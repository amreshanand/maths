# Viva Voce Preparation Guide: 25 Key Questions and Model Answers
**Project Title:** Linear Transformations: How Matrices Transform 2D Space  
**Course:** M3 Mathematics Animation Video Project  
**Student Name:** [ENTER STUDENT NAME]  
**Student ID:** [ENTER STUDENT ID]  

---

### Q1: What is a linear transformation?
**Answer:**  
A linear transformation is a mapping $T: V \to W$ between two vector spaces (in our project, from $\mathbb{R}^2$ to $\mathbb{R}^2$) that preserves the algebraic operations of vector addition and scalar multiplication. Geometrically in 2D space, it maps lines to lines (or points), preserves parallelism, keeps grid lines evenly spaced, and keeps the origin $(0, 0)$ anchored in place.

---

### Q2: What are the two fundamental properties of linearity?
**Answer:**  
The two defining axioms are:
1. **Additivity (Superposition):** $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ for all vectors $\mathbf{u}, \mathbf{v} \in V$.
2. **Homogeneity (Scalar Scaling):** $T(c\mathbf{u}) = c\,T(\mathbf{u})$ for any scalar $c \in \mathbb{R}$ and vector $\mathbf{u} \in V$.
Together, they can be written as the single condition: $T(c\mathbf{u} + d\mathbf{v}) = c\,T(\mathbf{u}) + d\,T(\mathbf{v})$.

---

### Q3: Why must every linear transformation map the origin to itself?
**Answer:**  
From the homogeneity property, setting scalar $c = 0$ gives:
$$T(\mathbf{0}) = T(0 \cdot \mathbf{v}) = 0 \cdot T(\mathbf{v}) = \mathbf{0}$$
Alternatively, from additivity:
$$T(\mathbf{0}) = T(\mathbf{0} + \mathbf{0}) = T(\mathbf{0}) + T(\mathbf{0}) \implies T(\mathbf{0}) = \mathbf{0}$$
If a transformation moves the origin, such as a translation $T(\mathbf{v}) = \mathbf{v} + \mathbf{b}$ where $\mathbf{b} \ne \mathbf{0}$, it violates additivity and homogeneity, making it an **affine transformation**, not a linear transformation.

---

### Q4: What does a transformation matrix represent?
**Answer:**  
A transformation matrix $A$ is the concrete numerical encoding of a linear operator $T$ relative to a chosen basis. For $\mathbb{R}^2$, applying the transformation to any vector $\mathbf{x}$ corresponds directly to matrix-vector multiplication: $T(\mathbf{x}) = A\mathbf{x}$.

---

### Q5: What do the columns of a transformation matrix represent?
**Answer:**  
The columns of a transformation matrix are the landing coordinates of the standard basis vectors after the transformation is applied.
Specifically, if standard basis vectors are $\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ and $\mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$, then:
$$A = \begin{pmatrix} \vert & \vert \\ T(\mathbf{e}_1) & T(\mathbf{e}_2) \\ \vert & \vert \end{pmatrix}$$
The first column is $T(\mathbf{e}_1)$ and the second column is $T(\mathbf{e}_2)$.

---

### Q6: What happens to the standard basis vectors under our chosen matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$?
**Answer:**  
- For $\mathbf{e}_1 = (1, 0)^T$:
  $$T(\mathbf{e}_1) = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
- For $\mathbf{e}_2 = (0, 1)^T$:
  $$T(\mathbf{e}_2) = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
They land precisely at $(2, 1)$ and $(1, 2)$, which form the two columns of $A$.

---

### Q7: How do you calculate the transformed coordinates of an arbitrary vector $(x, y)^T$?
**Answer:**  
By expanding $(x, y)^T$ in terms of the basis vectors:
$$\mathbf{v} = x\,\mathbf{e}_1 + y\,\mathbf{e}_2$$
Applying linearity:
$$T(\mathbf{v}) = x\,T(\mathbf{e}_1) + y\,T(\mathbf{e}_2) = x \begin{pmatrix} 2 \\ 1 \end{pmatrix} + y \begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 2x + y \\ x + 2y \end{pmatrix}$$
This matches the standard row-by-column matrix multiplication $A\mathbf{v}$.

---

### Q8: What is the determinant of a $2 \times 2$ matrix algebraically?
**Answer:**  
For a matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the determinant is defined as:
$$\det(M) = ad - bc$$
For our project matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$:
$$\det(A) = (2)(2) - (1)(1) = 4 - 1 = 3$$

---

### Q9: What does the absolute value of the determinant represent geometrically?
**Answer:**  
The absolute value $|\det(A)|$ represents the **area scaling factor** of the transformation. Any region in the 2D plane with original area $S$ will have an area of $|\det(A)| \times S$ after the transformation. Since our unit square had area $1 \times 1 = 1$, the transformed parallelogram has an area of exactly $3 \times 1 = 3$.

---

### Q10: What does a negative determinant indicate?
**Answer:**  
A negative determinant indicates that the transformation reverses the **orientation** of the space. In 2D, this means the plane has undergone a reflection (like flipping a pancake). The basis vector $\mathbf{e}_2$, which was initially $90^\circ$ counterclockwise from $\mathbf{e}_1$, would end up clockwise relative to $\mathbf{e}_1$. Since our $\det(A) = +3 > 0$, orientation is preserved.

---

### Q11: What does a zero determinant indicate?
**Answer:**  
A determinant of zero ($\det(A) = 0$) indicates that the transformation collapses the 2D space into a lower dimension—either squashing the entire plane onto a 1D line or collapsing it entirely into a 0D point (the origin). In this case, the matrix is non-invertible (singular), and information is lost because infinite input vectors map to the same output vector.

---

### Q12: What is an eigenvector?
**Answer:**  
An eigenvector of a linear transformation $A$ is a non-zero vector $\mathbf{v}$ whose direction remains unchanged (or reversed) when $A$ is applied. That is, $A$ merely scales $\mathbf{v}$ by a factor without rotating it out of its span:
$$A\mathbf{v} = \lambda\mathbf{v}$$
where $\lambda$ is a scalar.

---

### Q13: What is an eigenvalue?
**Answer:**  
An eigenvalue $\lambda$ is the scalar factor by which the corresponding eigenvector is stretched, shrunk, or inverted under the transformation. If $\lambda > 1$, the vector is stretched; if $0 < \lambda < 1$, it is compressed; if $\lambda = 1$, its length is invariant; if $\lambda < 0$, it is scaled and flipped $180^\circ$.

---

### Q14: Why do some vector directions remain unchanged under our matrix $A$?
**Answer:**  
Solving the characteristic equation $\det(A - \lambda I) = 0$:
$$(2 - \lambda)^2 - 1 = 0 \implies \lambda^2 - 4\lambda + 3 = 0 \implies (\lambda - 3)(\lambda - 1) = 0$$
The eigenvalues are $\lambda_1 = 3$ and $\lambda_2 = 1$.
- For $\lambda_1 = 3$, solving $(A - 3I)\mathbf{v} = \mathbf{0}$ yields $y = x$, so the line along $(1, 1)$ is an invariant direction stretched by $3$.
- For $\lambda_2 = 1$, solving $(A - I)\mathbf{v} = \mathbf{0}$ yields $y = -x$, so the line along $(1, -1)$ is an invariant direction with scale factor $1$.
Along these specific directions, the off-diagonal shear components balance the diagonal stretches, resulting in pure scaling.

---

### Q15: Does a determinant of 1 always mean the transformation is a rigid rotation?
**Answer:**  
**No, absolutely not.** A determinant of 1 guarantees only that **area and orientation are preserved**. It does not guarantee that lengths or angles between vectors are preserved.
A rigid rotation is an **isometry** represented by an orthogonal matrix where $R^T R = I$.
A non-rotation counterexample is a squeeze mapping such as $B = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$:
$$\det(B) = (2)(0.5) - (0)(0) = 1$$
It preserves area, but it stretches horizontal vectors by 2 and compresses vertical vectors by 0.5, changing vector lengths and angles.

---

### Q16: What is the formal difference between area preservation and distance preservation (isometry)?
**Answer:**  
- **Area preservation** means that for any region $\Omega$, $\text{Area}(T(\Omega)) = \text{Area}(\Omega)$, which occurs if and only if $|\det(T)| = 1$.
- **Distance preservation (Isometry)** means that for any vectors $\mathbf{u}, \mathbf{v}$, $\|T(\mathbf{u}) - T(\mathbf{v})\| = \|\mathbf{u} - \mathbf{v}\|$, or equivalently $\|T(\mathbf{v})\| = \|\mathbf{v}\|$ for all $\mathbf{v}$.
An isometry requires the matrix $M$ to satisfy $M^T M = I$ (orthogonal matrix). All isometries in 2D preserve area, but area-preserving transformations form the much larger Special Linear Group $\mathrm{SL}(2, \mathbb{R})$, of which rotations $\mathrm{SO}(2)$ are merely a subgroup.

---

### Q17: How does a matrix deform the 2D coordinate grid?
**Answer:**  
Because a linear transformation preserves additivity and scalar multiplication, straight lines must transform into straight lines, parallel lines must remain parallel, and grid lines that are initially equidistant remain equidistant after the transformation. Thus, the square grid is deformed into a network of congruent parallelograms centered at the stationary origin.

---

### Q18: Why does the unit square become a parallelogram?
**Answer:**  
The unit square is bounded by vectors $\mathbf{e}_1 = (1, 0)^T$ and $\mathbf{e}_2 = (0, 1)^T$ originating from $(0, 0)$. Under linearity, $\mathbf{e}_1 \to T(\mathbf{e}_1)$ and $\mathbf{e}_2 \to T(\mathbf{e}_2)$. The opposite sides are parallel vectors $\mathbf{e}_1$ and $\mathbf{e}_2$ shifted by the other basis vector. Because linearity preserves vector addition:
$$T(\mathbf{e}_1 + \mathbf{e}_2) = T(\mathbf{e}_1) + T(\mathbf{e}_2)$$
The fourth vertex $(1, 1)$ must land at $(2, 1) + (1, 2) = (3, 3)$. Since opposite sides remain parallel and equal in length, the transformed shape is geometrically a parallelogram.

---

### Q19: How can you computationally verify a matrix transformation?
**Answer:**  
Computationally, one can:
1. Perform direct matrix-vector multiplication $A\mathbf{v}$ and compare against analytical formulas.
2. Evaluate linearity with random vectors: assert that $A(\mathbf{u} + \mathbf{v}) = A\mathbf{u} + A\mathbf{v}$ and $A(c\mathbf{u}) = c(A\mathbf{u})$ within floating-point tolerance ($10^{-12}$).
3. Calculate polygon area via the Shoelace formula on transformed vertices and check equality with $|\det(A)| \times \text{Original Area}$.
4. Compute eigenvalues and eigenvectors using `numpy.linalg.eig` and verify that $\|A\mathbf{v} - \lambda\mathbf{v}\| < \epsilon$.

---

### Q20: Where are linear transformations applied in modern computer science and engineering?
**Answer:**  
Linear transformations are pervasive across:
1. **Computer Graphics & Gaming:** 2D/3D model translation (using homogeneous coordinates), rotation, scaling, and camera view projections (rasterization pipeline).
2. **Machine Learning & Deep Learning:** Dense neural network layers compute $\mathbf{y} = W\mathbf{x} + \mathbf{b}$, where weights $W$ linearly transform activation spaces before non-linear activations.
3. **Computer Vision & Image Processing:** Affine image warping, perspective rectification, and convolutional kernel filtering.
4. **Robotics & Kinematics:** Forward and inverse kinematics using transformation matrices (DH parameters) to position robotic end-effectors.
5. **Quantum Computing:** Quantum logic gates are unitary matrices acting as linear transformations on complex state vectors (qubits).

---

### Q21: What is the trace of a matrix, and how does it relate to eigenvalues?
**Answer:**  
The trace is the sum of the main diagonal elements: $\operatorname{tr}(A) = 2 + 2 = 4$.
In linear algebra, the trace always equals the sum of the eigenvalues:
$$\lambda_1 + \lambda_2 = 3 + 1 = 4 = \operatorname{tr}(A)$$
Similarly, the product of eigenvalues equals the determinant:
$$\lambda_1 \times \lambda_2 = 3 \times 1 = 3 = \det(A)$$

---

### Q22: Is our matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ symmetric, and what does the Spectral Theorem tell us about it?
**Answer:**  
Yes, $A = A^T$ (symmetric). By the **Spectral Theorem for Real Symmetric Matrices**:
1. All eigenvalues of $A$ are guaranteed to be real ($\lambda = 3, 1$).
2. Eigenvectors corresponding to distinct eigenvalues are mutually orthogonal:
   $$\mathbf{v}_1 \cdot \mathbf{v}_2 = (1)(1) + (1)(-1) = 1 - 1 = 0$$
3. $A$ can be orthogonally diagonalized as $A = Q \Lambda Q^T$, representing space being rotated by $45^\circ$, scaled by factors of 3 and 1, and rotated back.

---

### Q23: What would happen if matrix $A$ had complex eigenvalues?
**Answer:**  
If a $2 \times 2$ real matrix has complex eigenvalues (which occurs when the discriminant $(\operatorname{tr}(A))^2 - 4\det(A) < 0$), there are no real invariant lines in 2D space. Geometrically, the transformation contains an intrinsic rotational component that turns all non-zero vectors in the plane, preventing any vector from pointing along its original span.

---

### Q24: What is the rank of matrix $A$, and what does the Rank-Nullity Theorem state?
**Answer:**  
The rank of $A$ is 2 because its columns $\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ and $\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ are linearly independent.
The Rank-Nullity Theorem states:
$$\operatorname{rank}(A) + \operatorname{nullity}(A) = n$$
For $n = 2$, $2 + \operatorname{nullity}(A) = 2 \implies \operatorname{nullity}(A) = 0$.
The kernel (null space) contains only the zero vector $\{\mathbf{0}\}$, meaning the transformation is bijective (one-to-one and onto).

---

### Q25: Why did we specifically choose $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ for this academic video?
**Answer:**  
This matrix is pedagogically ideal because:
1. It has integer coefficients and clean integer eigenvalues ($\lambda = 3, 1$).
2. Its determinant is $+3$, which provides an unmistakable visual tripling of area without flipping orientation.
3. Its eigenvectors align along the intuitive diagonals $y = x$ and $y = -x$.
4. It clearly combines both shear and stretch, contrasting sharply with pure scalings or trivial diagonal matrices.
