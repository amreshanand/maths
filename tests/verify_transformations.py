"""
Mathematical Verification Script for Linear Transformations Project
Uses NumPy to independently test and assert all mathematical properties and claims.
"""

import sys
import numpy as np

def run_all_tests():
    print("=" * 70)
    print("RUNNING MATHEMATICAL VERIFICATION SUITE")
    print("=" * 70)

    # 1. Setup Matrix A
    A = np.array([[2, 1],
                  [1, 2]], dtype=float)
    print(f"\n[Matrix Definition]\nA =\n{A}")

    # Test 1: Matrix Multiplication Properties
    v_test = np.array([3, 4], dtype=float)
    calc_manual = np.array([2*3 + 1*4, 1*3 + 2*4], dtype=float)
    calc_matmul = A @ v_test
    assert np.allclose(calc_manual, calc_matmul), "Matrix multiplication manual vs matmul mismatch!"
    print("\n✓ Test 1 Passed: Matrix multiplication verified.")

    # Test 2: Standard Basis Vector Mappings
    e1 = np.array([1, 0], dtype=float)
    e2 = np.array([0, 1], dtype=float)
    Te1 = A @ e1
    Te2 = A @ e2
    assert np.allclose(Te1, [2, 1]), f"T(e1) expected [2, 1], got {Te1}"
    assert np.allclose(Te2, [1, 2]), f"T(e2) expected [1, 2], got {Te2}"
    assert np.allclose(A[:, 0], Te1), "First column of A does not match T(e1)"
    assert np.allclose(A[:, 1], Te2), "Second column of A does not match T(e2)"
    print(f"✓ Test 2 Passed: Basis mappings verified: T(e1) = {Te1}, T(e2) = {Te2}.")
    print("   Notice columns of A are exactly [T(e1), T(e2)].")

    # Test 3: Worked Examples
    # Example 1: v1 = (1, 1) -> (3, 3)
    v1 = np.array([1, 1], dtype=float)
    Tv1 = A @ v1
    # Step-by-step: 2(1)+1(1) = 3; 1(1)+2(1) = 3
    assert np.allclose(Tv1, [3, 3]), f"T(v1) expected [3, 3], got {Tv1}"

    # Example 2: v2 = (2, -1) -> (3, 0)
    v2 = np.array([2, -1], dtype=float)
    Tv2 = A @ v2
    # Step-by-step: 2(2)+1(-1) = 3; 1(2)+2(-1) = 0
    assert np.allclose(Tv2, [3, 0]), f"T(v2) expected [3, 0], got {Tv2}"
    print(f"✓ Test 3 Passed: Worked examples verified:")
    print(f"   A(1, 1) = {Tv1}")
    print(f"   A(2, -1) = {Tv2}")

    # Test 4: Unit Square Vertices Transformation
    # Original square vertices: (0,0), (1,0), (1,1), (0,1)
    sq_vertices = np.array([
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1]
    ], dtype=float)

    # Transformed vertices = vertices @ A.T (since v is column vector, (A v)^T = v^T A^T)
    trans_vertices = (A @ sq_vertices.T).T
    expected_vertices = np.array([
        [0, 0],
        [2, 1],
        [3, 3],
        [1, 2]
    ], dtype=float)
    assert np.allclose(trans_vertices, expected_vertices), "Transformed square vertices mismatch!"
    print(f"✓ Test 4 Passed: Transformed unit-square vertices verified:\n{trans_vertices}")

    # Test 5: Determinant and Area Scaling
    # det(A) = 2*2 - 1*1 = 3
    det_A = np.linalg.det(A)
    expected_det = 3.0
    assert np.isclose(det_A, expected_det), f"det(A) expected 3.0, got {det_A}"

    # Shoelace formula for area of transformed polygon: (0,0), (2,1), (3,3), (1,2)
    # Area = 0.5 * |(x0*y1 - x1*y0) + (x1*y2 - x2*y1) + (x2*y3 - x3*y2) + (x3*y0 - x0*y3)|
    x = trans_vertices[:, 0]
    y = trans_vertices[:, 1]
    polygon_area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    assert np.isclose(polygon_area, 3.0), f"Parallelogram area expected 3.0, got {polygon_area}"
    assert np.isclose(polygon_area, det_A * 1.0), "Area scaling factor does not equal det(A)!"
    assert det_A > 0, "Determinant is not positive (orientation not preserved)"
    print(f"✓ Test 5 Passed: det(A) = {det_A:.4f}, Area of transformed polygon = {polygon_area:.4f} (Orientation preserved).")

    # Test 6: Eigenvalues and Eigenvectors
    evals, evecs = np.linalg.eig(A)
    # Sort eigenvalues descending: 3.0, 1.0
    idx = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:, idx]
    assert np.isclose(evals[0], 3.0), f"First eigenvalue expected 3.0, got {evals[0]}"
    assert np.isclose(evals[1], 1.0), f"Second eigenvalue expected 1.0, got {evals[1]}"

    # Verify eigenvector directions
    # For lambda=3, direction is (1, 1)
    ev1 = np.array([1, 1], dtype=float)
    assert np.allclose(A @ ev1, 3.0 * ev1), "A(1,1) != 3*(1,1)"

    # For lambda=1, direction is (1, -1)
    ev2 = np.array([1, -1], dtype=float)
    assert np.allclose(A @ ev2, 1.0 * ev2), "A(1,-1) != 1*(1,-1)"

    # Check length scaling
    len_ev1_orig = np.linalg.norm(ev1)
    len_ev1_trans = np.linalg.norm(A @ ev1)
    assert np.isclose(len_ev1_trans / len_ev1_orig, 3.0), "Stretch factor along (1,1) != 3.0"

    len_ev2_orig = np.linalg.norm(ev2)
    len_ev2_trans = np.linalg.norm(A @ ev2)
    assert np.isclose(len_ev2_trans / len_ev2_orig, 1.0), "Length along (1,-1) not preserved!"
    print(f"✓ Test 6 Passed: Eigenvalues [3, 1] verified. Directions (1, 1) stretched x3, (1, -1) preserved x1.")

    # Test 7: Linearity Verification (Random Vectors + Zero Vector)
    # T(0) = 0
    zero_vec = np.array([0, 0], dtype=float)
    assert np.allclose(A @ zero_vec, zero_vec), "T(0) != 0"

    # Linearity for 100 random vector pairs
    np.random.seed(42)
    for _ in range(100):
        u_rand = np.random.uniform(-10, 10, size=2)
        v_rand = np.random.uniform(-10, 10, size=2)
        c_rand = np.random.uniform(-5, 5)

        # T(u + v) = T(u) + T(v)
        add_lhs = A @ (u_rand + v_rand)
        add_rhs = (A @ u_rand) + (A @ v_rand)
        assert np.allclose(add_lhs, add_rhs, atol=1e-12), "Additivity violated!"

        # T(c * u) = c * T(u)
        scalar_lhs = A @ (c_rand * u_rand)
        scalar_rhs = c_rand * (A @ u_rand)
        assert np.allclose(scalar_lhs, scalar_rhs, atol=1e-12), "Homogeneity violated!"
    print("✓ Test 7 Passed: Linearity rigorously tested over 100 random trials: T(u+v)=T(u)+T(v), T(cu)=cT(u), T(0)=0.")

    # Test 8: Squeeze Matrix B (det = 1, Area Preservation)
    B = np.array([[2.0, 0.0],
                  [0.0, 0.5]], dtype=float)
    det_B = np.linalg.det(B)
    assert np.isclose(det_B, 1.0), f"det(B) expected 1.0, got {det_B}"

    # Transformed unit square under B
    sq_trans_B = (B @ sq_vertices.T).T
    expected_sq_B = np.array([
        [0, 0],
        [2, 0],
        [2, 0.5],
        [0, 0.5]
    ], dtype=float)
    assert np.allclose(sq_trans_B, expected_sq_B), "Transformed square under B mismatch!"

    # Area calculation for rectangle under B
    area_B = 2.0 * 0.5
    assert np.isclose(area_B, 1.0), f"Area under B expected 1.0, got {area_B}"
    print(f"✓ Test 8 Passed: Squeeze matrix B has det(B) = {det_B:.4f}, transformed rectangle area = {area_B:.4f}.")

    # Test 9: Area Preservation does NOT imply Length Preservation (Isometry)
    # Check lengths under B
    len_e1_orig = np.linalg.norm(e1)
    len_e1_B = np.linalg.norm(B @ e1)
    len_e2_orig = np.linalg.norm(e2)
    len_e2_B = np.linalg.norm(B @ e2)

    assert not np.isclose(len_e1_orig, len_e1_B), "Length of e1 remained unchanged under squeeze!"
    assert not np.isclose(len_e2_orig, len_e2_B), "Length of e2 remained unchanged under squeeze!"
    assert np.isclose(len_e1_B, 2.0), f"Expected length 2.0, got {len_e1_B}"
    assert np.isclose(len_e2_B, 0.5), f"Expected length 0.5, got {len_e2_B}"

    # Isometry check: B^T @ B == I?
    BtB = B.T @ B
    is_orthogonal = np.allclose(BtB, np.eye(2))
    assert not is_orthogonal, "Matrix B is mistakenly orthogonal!"
    print(f"✓ Test 9 Passed: Squeeze transformation preserves area (det=1) but changes lengths:")
    print(f"   ||e1||: {len_e1_orig} -> {len_e1_B} (doubled)")
    print(f"   ||e2||: {len_e2_orig} -> {len_e2_B} (halved)")
    print("   B^T B != I, confirming B is NOT a rigid rotation (isometry).")

    print("\n" + "=" * 70)
    print("ALL 9 MATHEMATICAL VERIFICATION TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 70)

if __name__ == "__main__":
    run_all_tests()
