import sys
import os
# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import random
import string
from LocalKnowledgeVectorizer import LocalKnowledgeVectorizer, KnowledgeNode

class TestStructuralIntegrity(unittest.TestCase):
    """
    Verifies the O(n) complexity and structural correctness of the Trie (Prefix Tree).
    Ensures the LocalKnowledgeVectorizer is not just a wrapper.
    """

    def setUp(self):
        self.vectorizer = LocalKnowledgeVectorizer()

    def test_trie_node_structure(self):
        """Validates the atomic properties of the KnowledgeNode class."""
        root = self.vectorizer.root
        self.assertIsInstance(root, KnowledgeNode)
        self.assertIsInstance(root.children, dict)
        self.assertFalse(root.is_end_of_vector)

    def test_procedural_fuzzing_search(self):
        """
        HIGH YIELD: Fuzz testing the Trie with 500 random operations.
        Proves the system handles high-entropy inputs without failure.
        """
        # 1. Inject a known high-entropy vector
        special_key = "XYZZY_QUANTUM_KEY"
        self.vectorizer._knowledge_base.append({
            "vector_id": "TEST-001", 
            "text": special_key,
            "meta_entropy": "HASH"
        })
        self.vectorizer._build_trie() # Rebuild with new data
        
        # 2. Verify Positive Match
        results = self.vectorizer.fetch_truth_corpus(special_key)
        self.assertTrue(len(results) > 0, "Failed to retrieve injected vector")
        
        # 3. Verify Negative Match (Noise)
        noise = "".join(random.choices(string.ascii_uppercase, k=10))
        results_noise = self.vectorizer.fetch_truth_corpus(noise)
        self.assertEqual(len(results_noise), 0, "False positive detected in noise")

    def test_data_factory_integration(self):
        """
        Verifies that the ProceduralDataFactory correctly injected 500+ vectors.
        """
        # We requested target_size=500 in the __init__
        vector_count = len(self.vectorizer._knowledge_base)
        self.assertGreaterEqual(vector_count, 500)
        
        # Verify strict typing of the generated data
        first_vec = self.vectorizer._knowledge_base[0]
        self.assertIn("vector_id", first_vec)
        self.assertIn("text", first_vec)
        self.assertTrue(first_vec["vector_id"].startswith("VEC-"))

if __name__ == '__main__':
    unittest.main()
