"""
Test Runner - Execute All Unit Tests
Runs the complete algorithmic verification suite.
"""
import sys
import subprocess
import os


def run_test(test_file: str, description: str) -> bool:
    """Runs a single test file and returns success status."""
    print("\n" + "="*70)
    print(f"RUNNING: {description}")
    print("="*70)
    
    try:
        result = subprocess.run(
            [sys.executable, test_file],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            capture_output=False,
            text=True
        )
        
        success = result.returncode == 0
        
        if success:
            print(f"\n✅ {description} PASSED")
        else:
            print(f"\n❌ {description} FAILED (exit code {result.returncode})")
        
        return success
        
    except Exception as e:
        print(f"\n❌ {description} FAILED WITH EXCEPTION: {e}")
        return False


def main():
    """Main test runner."""
    print("\n" + "#"*70)
    print("# FACT-CHECKING REASONING ENGINE")
    print("# ALGORITHMIC VERIFICATION TEST SUITE")
    print("#"*70)
    
    tests = [
        ("tests/test_sigmoid.py", "Sigmoid Function Verification (100 values)"),
        ("tests/test_trie_stress.py", "Trie Stress Test (1000 words + 500 vectors)"),
        ("tests/test_mathematical_core.py", "Mathematical Core (unittest - 1000 sigmoid values)"),
        ("tests/test_structural_integrity.py", "Structural Integrity (unittest - Trie fuzzing)"),
        ("tests/test_entropy_generation.py", "Entropy Generation (unittest - 1000 vector uniqueness)")
    ]
    
    results = []
    
    for test_file, description in tests:
        passed = run_test(test_file, description)
        results.append((description, passed))
    
    # Final summary
    print("\n" + "#"*70)
    print("# TEST SUITE SUMMARY")
    print("#"*70)
    
    total_tests = len(results)
    passed_tests = sum(1 for _, passed in results if passed)
    
    for description, passed in results:
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{status}: {description}")
    
    print("\n" + "-"*70)
    print(f"TOTAL: {passed_tests}/{total_tests} tests passed")
    print("-"*70)
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED - SYSTEM VERIFIED")
        print("   - Custom tests: 2 (Sigmoid 100-val, Trie 1000-word)")
        print("   - Unittest suite: 3 (Math core, Structural, Entropy)")
        print("#"*70 + "\n")
        return 0
    else:
        print("\n⚠️  SOME TESTS FAILED - REVIEW REQUIRED")
        print("#"*70 + "\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
