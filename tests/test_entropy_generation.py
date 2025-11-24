import sys
import os
# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from ProceduralGraphGenerator import ProceduralGraphGenerator
from ProceduralDataFactory import ProceduralDataFactory

class TestEntropyGeneration(unittest.TestCase):
    """
    Verifies the uniqueness and randomness of the procedural generation subsystems.
    Strictly enforces Lumen Law 5 (No Static Data).
    """

    def test_markov_chain_transitions(self):
        """
        Verifies that the graph generator produces valid, weighted edges.
        """
        generator = ProceduralGraphGenerator()
        graph = generator.generate_graph("RootTopic", depth=5)
        
        self.assertEqual(graph["root"], "RootTopic")
        self.assertEqual(len(graph["relationships"]), 5)
        
        for edge in graph["relationships"]:
            # Check for high-entropy naming in nodes
            self.assertIn(edge["source"], generator.SEED_NODES + ["RootTopic"])
            self.assertIn(edge["target"], generator.SEED_NODES)
            
            # Check weight bounds (0.0 to 1.0)
            self.assertTrue(0.1 <= edge["weight"] <= 0.9)

    def test_factory_uniqueness_guarantee(self):
        """
        CRITICAL: Generates 1,000 vectors and proves 100% uniqueness.
        This validates the 'Combinatorial Explosion' logic.
        """
        factory = ProceduralDataFactory()
        
        # Generate a massive batch
        data = factory.generate_knowledge_base(target_size=1000)
        
        # Extract all IDs
        ids = [item["vector_id"] for item in data]
        unique_ids = set(ids)
        
        # The set length must equal list length (No duplicates)
        self.assertEqual(len(ids), len(unique_ids), "Duplicate Vector IDs detected - Entropy Failure")
        
        # Extract all text hashes to ensure content uniqueness
        hashes = [item["meta_entropy"] for item in data]
        unique_hashes = set(hashes)
        self.assertEqual(len(hashes), len(unique_hashes), "Duplicate Content detected")

if __name__ == '__main__':
    unittest.main()
