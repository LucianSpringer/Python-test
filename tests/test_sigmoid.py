"""
Unit Test: Sigmoid Function Verification
Purpose: Verify mathematical correctness of the manual sigmoid implementation
across 100 different input values to confirm the activation curve.
"""
import sys
import os
import math

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SemanticScoringEngine import SemanticScoringEngine


def reference_sigmoid(z: float) -> float:
    """Reference implementation for validation."""
    return 1.0 / (1.0 + math.exp(-z))


def test_sigmoid_curve_verification():
    """
    Tests the sigmoid function across 100 values from -10 to +10.
    Verifies that the curve matches the mathematical definition.
    """
    engine = SemanticScoringEngine()
    
    test_range = 100
    min_z = -10.0
    max_z = 10.0
    step = (max_z - min_z) / test_range
    
    passed_tests = 0
    failed_tests = 0
    tolerance = 1e-10  # Floating point comparison tolerance
    
    print("\n" + "="*70)
    print("SIGMOID FUNCTION VERIFICATION TEST")
    print("="*70)
    print(f"Testing {test_range} values from {min_z} to {max_z}")
    print(f"Tolerance: {tolerance}\n")
    
    failures = []
    
    for i in range(test_range):
        z_value = min_z + (i * step)
        
        # Get result from implementation
        actual = engine._manual_sigmoid(z_value)
        
        # Calculate expected value
        expected = reference_sigmoid(z_value)
        
        # Verify match
        difference = abs(actual - expected)
        
        if difference <= tolerance:
            passed_tests += 1
        else:
            failed_tests += 1
            failures.append({
                'z': z_value,
                'expected': expected,
                'actual': actual,
                'diff': difference
            })
    
    # Report results
    print(f"Tests Passed: {passed_tests}/{test_range}")
    print(f"Tests Failed: {failed_tests}/{test_range}")
    
    if failed_tests > 0:
        print("\nFAILURES:")
        for f in failures[:5]:  # Show first 5 failures
            print(f"  z={f['z']:.4f}: expected={f['expected']:.10f}, actual={f['actual']:.10f}, diff={f['diff']:.2e}")
    
    # Key mathematical checkpoints
    print("\n" + "-"*70)
    print("KEY SIGMOID CHECKPOINTS:")
    print("-"*70)
    
    checkpoints = [
        (0.0, "Midpoint (should be 0.5)"),
        (-5.0, "Far negative (should be ~0.0067)"),
        (5.0, "Far positive (should be ~0.9933)"),
        (-10.0, "Extreme negative (should be ~0.000045)"),
        (10.0, "Extreme positive (should be ~0.999955)")
    ]
    
    for z, description in checkpoints:
        result = engine._manual_sigmoid(z)
        expected = reference_sigmoid(z)
        print(f"  σ({z:>6.1f}) = {result:.10f}  [{description}]")
        assert abs(result - expected) <= tolerance, f"Checkpoint failed for z={z}"
    
    print("\n" + "="*70)
    
    if failed_tests == 0:
        print("✅ SIGMOID VERIFICATION: ALL TESTS PASSED")
        print("The manual sigmoid implementation is mathematically correct.")
    else:
        print("❌ SIGMOID VERIFICATION: FAILURES DETECTED")
        print("The manual sigmoid implementation has errors.")
    
    print("="*70 + "\n")
    
    return failed_tests == 0


def test_sigmoid_boundary_conditions():
    """Test boundary and edge cases."""
    engine = SemanticScoringEngine()
    
    print("\n" + "="*70)
    print("SIGMOID BOUNDARY CONDITIONS TEST")
    print("="*70 + "\n")
    
    # Test that sigmoid is always between 0 and 1
    test_values = [-100, -50, -10, -1, 0, 1, 10, 50, 100]
    
    all_passed = True
    for z in test_values:
        result = engine._manual_sigmoid(z)
        if not (0.0 <= result <= 1.0):
            print(f"❌ FAILED: σ({z}) = {result} (outside [0,1] range)")
            all_passed = False
        else:
            print(f"✅ PASSED: σ({z}) = {result:.10f}")
    
    print("\n" + "="*70)
    if all_passed:
        print("✅ BOUNDARY CONDITIONS: ALL TESTS PASSED")
    else:
        print("❌ BOUNDARY CONDITIONS: FAILURES DETECTED")
    print("="*70 + "\n")
    
    return all_passed


if __name__ == "__main__":
    print("\n" + "#"*70)
    print("# ALGORITHMIC VERIFICATION: SIGMOID FUNCTION TEST SUITE")
    print("#"*70)
    
    # Run tests
    test1_passed = test_sigmoid_curve_verification()
    test2_passed = test_sigmoid_boundary_conditions()
    
    # Final report
    print("\n" + "#"*70)
    print("# FINAL TEST REPORT")
    print("#"*70)
    
    if test1_passed and test2_passed:
        print("\n✅ ALL SIGMOID TESTS PASSED")
        print("The SemanticScoringEngine sigmoid implementation is verified.")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED")
        print("Review the sigmoid implementation for errors.")
        sys.exit(1)
