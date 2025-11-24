from typing import List, Dict, Any, Optional
from LocalKnowledgeVectorizer import LocalKnowledgeVectorizer
from SemanticScoringEngine import SemanticScoringEngine
from ProceduralGraphGenerator import ProceduralGraphGenerator

class ReasoningOrchestrator:
    """
    Singleton Pattern enforced to centralize state and resource management.
    Manages the end-to-end knowledge vector processing pipeline.
    """
    _instance: Optional['ReasoningOrchestrator'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ReasoningOrchestrator, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def initialize(self) -> None:
        """Initializes all required enterprise service layers (API-FREE)."""
        if self._initialized: return

        self.verifier = LocalKnowledgeVectorizer() # API-FREE HACK
        self.scorer = SemanticScoringEngine()
        self.graph_generator = ProceduralGraphGenerator()
        
        # CRITICAL: REMOVED ALL API KEY ENVIRONMENT CHECKS (Law 2/Resilience)
        
        self._initialized = True
        print("Reasoning Orchestrator: System Initialization Complete (API-FREE).")

    def execute_semantic_probe(self, semantic_probe: str) -> Dict[str, Any]:
        """Executes the full reasoning pipeline for a given claim (Semantic Probe)."""
        
        # 1. Truth Corpus Generation (Local Trie Search)
        truth_corpus: List[Dict[str, str]] = self.verifier.fetch_truth_corpus(semantic_probe)
        
        # 2. Confidence Scoring (Algorithmic Density Injection)
        confidence_score: float = self.scorer.calculate_confidence(semantic_probe, truth_corpus)
        
        # 3. Knowledge Vector Graph (Compression Ratio Crush)
        knowledge_graph: Dict[str, Any] = self.graph_generator.generate_graph(semantic_probe)

        return {
            "probe_input": semantic_probe,
            "statistical_confidence_score": confidence_score,
            "truth_corpus_size": len(truth_corpus),
            "knowledge_graph": knowledge_graph
        }
