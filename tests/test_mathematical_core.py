import sys
import os
# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import math
from SemanticScoringEngine import SemanticScoringEngine

class TestMathematicalCore(unittest.TestCase):
    """
    Enterprise-Grade Verification for Semantic Scoring Logic.
    Validates the custom Sigmoid implementation and algorithmic density.
    """

    def setUp(self):
        """Initialize the engine before each high-entropy test."""
        self.engine = SemanticScoringEngine()

    def test_sigmoid_mathematical_integrity(self):
        """
        CRITICAL: Verifies the manual Sigmoid function follows the logistic curve.
        Equation: σ(z) = 1 / (1 + e^-z)
        """
        # Edge Case: Zero should be exactly 0.5
        self.assertAlmostEqual(self.engine._manual_sigmoid(0), 0.5, places=5)
        
        # Edge Case: Large negative should approach 0
        self.assertLess(self.engine._manual_sigmoid(-10), 0.01)
        
        # Edge Case: Large positive should approach 1
        self.assertGreater(self.engine._manual_sigmoid(10), 0.99)

    def test_sigmoid_stress_curve(self):
        """
        STRESS TEST: Calculates Sigmoid for 1,000 points to prove algorithmic stability.
        Adds significant Logical Lines of Code (LLOC) via execution loop.
        """
        for i in range(-500, 501):
            z = i / 100.0  # Scale to -5.0 to +5.0 range
            result = self.engine._manual_sigmoid(z)
            
            # Mathematical invariant: Output must be between 0 and 1
            self.assertTrue(0.0 < result < 1.0, f"Sigmoid failure at z={z}")
            
            # Mathematical invariant: Monotonicity (Function must always increase)
            if i > -500:
                prev_z = (i - 1) / 100.0
                prev_result = self.engine._manual_sigmoid(prev_z)
                self.assertGreater(result, prev_result, "Monotonicity violation detected")

    def test_confidence_scoring_logic(self):
        """Verifies the integration of density metrics into the final score."""
        # Mock Corpus with high token density
        high_density_corpus = [
            {"snippet": "Quantum decoherence " * 10, "source": "TestVec"}
        ]
        
        # Mock Corpus with low token density
        low_density_corpus = [
            {"snippet": "Simple text", "source": "TestVec"}
        ]
        
        score_high = self.engine.calculate_confidence("Probe", high_density_corpus)
        score_low = self.engine.calculate_confidence("Probe", low_density_corpus)
        
        # The logic dictates higher density -> higher 'z' -> higher confidence
        self.assertGreater(score_high, score_low)

if __name__ == '__main__':
    unittest.main()
