# Mathematical Verification Report
**Project Title:** Linear Transformations: How Matrices Transform 2D Space  
**Course:** M3 Mathematics Animation Video Project  
**Student Name:** [ENTER STUDENT NAME]  
**Student ID:** [ENTER STUDENT ID]  
**Verification Script:** `tests/verify_transformations.py`  
**Test Engine:** Python 3.12 / NumPy 2.x  

---

## Executive Summary
This report provides independent mathematical verification for all algebraic formulas, geometric claims, matrix-vector transformations, determinants, and eigenspace properties presented in the video. All 9 automated numerical verification tests passed with 100% success using floating-point tolerance $\epsilon = 10^{-12}$.

---

## 1. Matrix Definition & Basic Multiplications
### Theoretical Formula
Given the primary matrix:
$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$
Matrix multiplication for an arbitrary vector $\mathbf{v} = \begin{pmatrix} x \\ y \end{pmatrix}$:
$$A\mathbf{v} = \begin{pmatrix} 2x + y \\ x + 2y \end{pmatrix}$$

### Step-by-Step Numerical Verification
Test with generic vector $\mathbf{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$:
- Component 1: $2(3) + 1(4) = 6 + 4 = 10$
- Component 2: $1(3) + 2(4) = 3 + 8 = 11$
- Expected: $\begin{pmatrix} 10 \\ 11 \end{pmatrix}$
- Computed: $\begin{pmatrix} 10.0 \\ 11.0 \end{pmatrix}$
- **Test Status: PASSED**

---

## 2. Standard Basis Vector Mappings
### Theoretical Formulation
The standard basis vectors in $\mathbb{R}^2$ are:
$$\mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$$
Applying transformation $T(\mathbf{v}) = A\mathbf{v}$:
$$T(\mathbf{e}_1) = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(0) \\ 1(1) + 2(0) \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
$$T(\mathbf{e}_2) = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(0) + 1(1) \\ 1(0) + 2(1) \end{pmatrix} = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$

### Pedagogical Insight
Notice that:
$$\operatorname{Col}_1(A) = T(\mathbf{e}_1) = \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \quad \operatorname{Col}_2(A) = T(\mathbf{e}_2) = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$
This demonstrates the foundational theorem of linear algebra: **The columns of any transformation matrix are precisely the coordinates of the transformed basis vectors.**
- **Test Status: PASSED**

---

## 3. Worked Examples (Step-by-Step)
### Example 1: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
- Formula: $A\mathbf{v}_1 = \begin{pmatrix} 2(1) + 1(1) \\ 1(1) + 2(1) \end{pmatrix} = \begin{pmatrix} 2 + 1 \\ 1 + 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix}$
- Expected Result: $(3, 3)^T$
- Programmatic Result: `[3.0, 3.0]`
- Geometric Meaning: The vector along the diagonal expands directly outward by a factor of 3 to the apex of the transformed parallelogram.
- **Test Status: PASSED**

### Example 2: $\mathbf{v}_2 = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$
- Formula: $A\mathbf{v}_2 = \begin{pmatrix} 2(2) + 1(-1) \\ 1(2) + 2(-1) \end{pmatrix} = \begin{pmatrix} 4 - 1 \\ 2 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \end{pmatrix}$
- Expected Result: $(3, 0)^T$
- Programmatic Result: `[3.0, 0.0]`
- Geometric Meaning: The vector pointing into quadrant IV rotates and stretches to land precisely on the positive horizontal x-axis.
- **Test Status: PASSED**

---

## 4. Transformed Unit Square Vertices
### Coordinate Tracking
The canonical unit square has four ordered vertices:
1. Origin: $O = (0, 0)$
2. Basis 1: $P_1 = (1, 0)$
3. Diagonal: $P_2 = (1, 1)$
4. Basis 2: $P_3 = (0, 1)$

Applying transformation $A$:
1. $A(0, 0)^T = (0, 0)^T$
2. $A(1, 0)^T = (2, 1)^T$
3. $A(1, 1)^T = (3, 3)^T$
4. $A(0, 1)^T = (1, 2)^T$

Expected Vertices: `[(0, 0), (2, 1), (3, 3), (1, 2)]`  
Computed Vertices: `[(0.0, 0.0), (2.0, 1.0), (3.0, 3.0), (1.0, 2.0)]`  
Geometric Insight: Under linear transformation, the unit square morphs into a parallelogram whose adjacent sides are $T(\mathbf{e}_1)$ and $T(\mathbf{e}_2)$ and whose diagonal is $T(\mathbf{e}_1 + \mathbf{e}_2) = T(\mathbf{e}_1) + T(\mathbf{e}_2)$.  
- **Test Status: PASSED**

---

## 5. Determinant, Area Scaling, and Orientation
### Determinant Formula
For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$:
$$\det(A) = ad - bc = (2)(2) - (1)(1) = 4 - 1 = 3$$

### Geometric Area Calculation (Shoelace Formula)
Vertices: $(x_0, y_0)=(0,0), (x_1, y_1)=(2,1), (x_2, y_2)=(3,3), (x_3, y_3)=(1,2)$.
$$\text{Area} = \frac{1}{2} |(x_0 y_1 - x_1 y_0) + (x_1 y_2 - x_2 y_1) + (x_2 y_3 - x_3 y_2) + (x_3 y_0 - x_0 y_3)|$$
$$\text{Area} = \frac{1}{2} |(0 - 0) + (6 - 3) + (6 - 3) + (0 - 0)| = \frac{1}{2} |3 + 3| = 3.0$$

### Findings:
1. $\text{Transformed Area} = 3.0 = |\det(A)| \times \text{Original Area} (1.0)$.
2. $\det(A) = +3 > 0$, confirming that spatial orientation is strictly preserved.
- **Test Status: PASSED**

---

## 6. Eigensystem Analysis
### Characteristic Polynomial
$$\det(A - \lambda I) = \det \begin{pmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{pmatrix} = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$$
Roots:
$$\lambda_1 = 3, \quad \lambda_2 = 1$$

### Eigenvector 1 ($\lambda_1 = 3$):
$$(A - 3I)\mathbf{v} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies -x + y = 0 \implies y = x$$
Normalized direction: $\mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.  
Action: $A \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.  
Length ratio: $\frac{\|A\mathbf{v}_1\|}{\|\mathbf{v}_1\|} = \frac{\sqrt{3^2 + 3^2}}{\sqrt{1^2 + 1^2}} = \frac{3\sqrt{2}}{\sqrt{2}} = 3.0$.  
Geometric meaning: Vectors along $y = x$ undergo pure expansion by factor 3 with zero rotational deflection.

### Eigenvector 2 ($\lambda_2 = 1$):
$$(A - I)\mathbf{v} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies x + y = 0 \implies y = -x$$
Normalized direction: $\mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.  
Action: $A \begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(-1) \\ 1(1) + 2(-1) \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \end{pmatrix} = 1 \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.  
Length ratio: $\frac{\|A\mathbf{v}_2\|}{\|\mathbf{v}_2\|} = \frac{\sqrt{1^2 + (-1)^2}}{\sqrt{1^2 + (-1)^2}} = 1.0$.  
Geometric meaning: Vectors along $y = -x$ maintain invariant length and invariant direction.
- **Test Status: PASSED**

---

## 7. Linearity Axioms Rigorous Validation
Tested over 100 random vector pairs $\mathbf{u}, \mathbf{v} \in [-10, 10]^2$ and random scalars $c \in [-5, 5]$:
1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$: maximum residual $< 10^{-14}$.
2. $T(c\mathbf{u}) = c\,T(\mathbf{u})$: maximum residual $< 10^{-14}$.
3. $T(\mathbf{0}) = \mathbf{0}$: verified exactly.
- **Test Status: PASSED**

---

## 8. Squeeze Transformation: Area Preservation vs. Rotation
### Matrix Definition
$$B = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix}$$
### Determinant
$$\det(B) = (2)(0.5) - (0)(0) = 1.0$$
### Transformed Unit Square Vertices
- $(0, 0) \to (0, 0)$
- $(1, 0) \to (2, 0)$
- $(1, 1) \to (2, 0.5)$
- $(0, 1) \to (0, 0.5)$
Area of rectangle: $\text{width} \times \text{height} = 2.0 \times 0.5 = 1.0$.  
Area scaling factor: $|\det(B)| = 1.0$. Area is perfectly preserved.
- **Test Status: PASSED**

---

## 9. Non-Isometry of Squeeze Matrix (Lengths Changed)
### Distance and Length Analysis
- Original length of $\mathbf{e}_1$: $\|\mathbf{e}_1\| = 1.0$
- Transformed length: $\|B\mathbf{e}_1\| = \|(2, 0)^T\| = 2.0$ (Stretched by 200%)
- Original length of $\mathbf{e}_2$: $\|\mathbf{e}_2\| = 1.0$
- Transformed length: $\|B\mathbf{e}_2\| = \|(0, 0.5)^T\| = 0.5$ (Compressed by 50%)

### Orthogonality Check (Isometry Condition)
$$B^T B = \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix} \begin{pmatrix} 2 & 0 \\ 0 & 0.5 \end{pmatrix} = \begin{pmatrix} 4 & 0 \\ 0 & 0.25 \end{pmatrix} \ne I$$
Since $B^T B \ne I$, matrix $B$ is **not orthogonal**.  
**Crucial Mathematical Conclusion:** A transformation with $\det(M) = 1$ preserves area and orientation, but is NOT necessarily an isometry (rigid rotation/reflection). Rigid rotations preserve all Euclidean distances, whereas general $\det=1$ maps distort lengths and angles.
- **Test Status: PASSED**
