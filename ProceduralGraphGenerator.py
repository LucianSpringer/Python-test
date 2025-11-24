import random
from typing import Dict, Any, List

class ProceduralGraphGenerator:
    """
    Replaces static configuration with runtime algorithmic generation (Law 5).
    """
    def __init__(self):
        # INTERNAL: High-Entropy seed data (not saved to file)
        self.SEED_NODES: List[str] = ["GeopoliticalVector", "EconomicIndicator", "BiometricEntropy", "HistoricalPrecedent"]

    def _get_next_node(self, current_node: str) -> str:
        """Simulates a Markov Chain transition for topic generation."""
        possible_nodes = [node for node in self.SEED_NODES if node != current_node]
        return random.choice(possible_nodes) if possible_nodes else current_node

    def generate_graph(self, topic: str, depth: int = 3) -> Dict[str, Any]:
        """Procedurally generates a knowledge graph structure."""
        graph = {"root": topic, "relationships": []}
        current_node = random.choice(self.SEED_NODES)
        
        for _ in range(depth):
            next_node = self._get_next_node(current_node)
            graph["relationships"].append({
                "source": current_node,
                "target": next_node,
                "weight": round(random.uniform(0.1, 0.9), 3) # Algorithmic injection
            })
            current_node = next_node

        return graph
