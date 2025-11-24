"""
Type Schemas for Enterprise-Grade Fact-Checking Engine
Provides strict typing layer for all data structures.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from typing_extensions import TypedDict


# ==================== REQUEST/RESPONSE SCHEMAS ====================

class ProbeRequest(TypedDict):
    """Type-safe definition for incoming semantic probe requests."""
    semantic_probe: str
    max_corpus_size: Optional[int]
    confidence_threshold: Optional[float]


class ProbeResponse(TypedDict):
    """Type-safe definition for probe analysis results."""
    probe_input: str
    statistical_confidence_score: float
    truth_corpus_size: int
    knowledge_graph: Dict[str, Any]


# ==================== TRIE/VECTORIZER SCHEMAS ====================

@dataclass
class TrieNodePayload:
    """Payload structure for Trie terminal nodes."""
    vector_id: str
    text: str
    meta_entropy: Optional[str] = None
    confidence_weight: float = 1.0


@dataclass
class TruthCorpusItem:
    """Individual item in the Truth Corpus result set."""
    snippet: str
    source: str
    relevance_score: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts to dictionary for legacy compatibility."""
        return {
            "snippet": self.snippet,
            "source": self.source,
            "relevance_score": self.relevance_score
        }


# ==================== SCORING ENGINE SCHEMAS ====================

@dataclass
class SigmoidMetrics:
    """Metrics and intermediate values from Sigmoid calculation."""
    raw_alignment_score: float
    normalized_z_value: float
    sigmoid_output: float
    confidence_percentage: float
    corpus_token_count: int
    probe_token_count: int


@dataclass
class ConfidenceReport:
    """Complete confidence analysis report."""
    probe: str
    corpus_size: int
    confidence_score: float
    metrics: SigmoidMetrics
    classification: str = field(init=False)
    
    def __post_init__(self):
        """Auto-classify confidence level."""
        if self.confidence_score >= 75.0:
            self.classification = "HIGH"
        elif self.confidence_score >= 50.0:
            self.classification = "MEDIUM"
        else:
            self.classification = "LOW"


# ==================== GRAPH GENERATOR SCHEMAS ====================

@dataclass
class GraphEdge:
    """Weighted edge in the knowledge graph."""
    source: str
    target: str
    weight: float
    edge_type: str = "MARKOV_TRANSITION"
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts to dictionary for serialization."""
        return {
            "source": self.source,
            "target": self.target,
            "weight": self.weight,
            "edge_type": self.edge_type
        }


@dataclass
class GraphNode:
    """Node in the knowledge graph."""
    node_id: str
    node_type: str
    label: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class KnowledgeGraph:
    """Complete knowledge graph structure."""
    root: str
    nodes: List[GraphNode] = field(default_factory=list)
    edges: List[GraphEdge] = field(default_factory=list)
    depth: int = 3
    generation_algorithm: str = "MARKOV_CHAIN"
    
    def add_edge(self, source: str, target: str, weight: float) -> None:
        """Adds a new edge to the graph."""
        edge = GraphEdge(source=source, target=target, weight=weight)
        self.edges.append(edge)
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts to dictionary for legacy compatibility."""
        return {
            "root": self.root,
            "relationships": [edge.to_dict() for edge in self.edges],
            "depth": self.depth,
            "algorithm": self.generation_algorithm
        }


# ==================== ORCHESTRATOR SCHEMAS ====================

@dataclass
class PipelineState:
    """State tracking for the reasoning pipeline."""
    current_step: str
    steps_completed: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    start_time: Optional[float] = None
    end_time: Optional[float] = None


@dataclass
class ExecutionContext:
    """Context object passed through the pipeline."""
    probe: str
    state: PipelineState
    truth_corpus: List[TruthCorpusItem] = field(default_factory=list)
    confidence_report: Optional[ConfidenceReport] = None
    knowledge_graph: Optional[KnowledgeGraph] = None


# ==================== FACTORY SCHEMAS ====================

@dataclass
class GenerationStats:
    """Statistics from the ProceduralDataFactory generation."""
    target_size: int
    actual_size: int
    attempts: int
    unique_hashes: int
    generation_time_ms: float
    avg_sentence_length: float


class VectorDefinition(TypedDict):
    """Legacy-compatible vector definition."""
    vector_id: str
    text: str
    meta_entropy: Optional[str]


# ==================== VALIDATION UTILITIES ====================

def validate_probe_request(data: Dict[str, Any]) -> ProbeRequest:
    """Validates and constructs a ProbeRequest from raw data."""
    if "semantic_probe" not in data:
        raise ValueError("Missing required field: semantic_probe")
    
    return ProbeRequest(
        semantic_probe=data["semantic_probe"],
        max_corpus_size=data.get("max_corpus_size"),
        confidence_threshold=data.get("confidence_threshold")
    )


def validate_confidence_score(score: float) -> None:
    """Validates confidence score is within acceptable range."""
    if not 0.0 <= score <= 100.0:
        raise ValueError(f"Invalid confidence score: {score}. Must be 0-100.")
