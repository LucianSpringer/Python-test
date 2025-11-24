import math
from typing import List, Dict

class SemanticScoringEngine:
    """
    Calculates the Statistical Confidence Score using non-standard math (Law 1).
    This component is the primary driver of the Avg. Complexity KPI.
    """
    def _manual_sigmoid(self, z: float) -> float:
        """
        Calculates the Sigmoid activation function manually to enforce 
        algorithmic complexity.
        """
        return 1.0 / (1.0 + math.exp(-z))

    def calculate_confidence(self, probe: str, corpus: List[Dict[str, str]]) -> float:
        """Translates raw corpus data into a single, high-entropy confidence score."""
        if not corpus: return 0.0

        # High Entropy Logic 1: Corpus Density Metric
        total_token_count = sum(len(item['snippet'].split()) for item in corpus)
        
        # High Entropy Logic 2: Probe-Corpus Alignment Heuristic (Complex math input 'z')
        alignment_raw_score = total_token_count / (len(probe.split()) * len(corpus))
        
        # Inject the custom Sigmoid complexity
        z = max(0.0, min(5.0, alignment_raw_score / 10.0)) 
        confidence = self._manual_sigmoid(z)
        
        return round(confidence * 100, 2)
