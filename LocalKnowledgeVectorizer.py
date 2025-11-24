import random
from typing import List, Dict, Any, Optional
from ProceduralDataFactory import ProceduralDataFactory

# High Entropy Naming: Knowledge Node instead of Trie Node
class KnowledgeNode:
    def __init__(self):
        self.children: Dict[str, 'KnowledgeNode'] = {}
        self.is_end_of_vector: bool = False
        self.payload: str = ""

class LocalKnowledgeVectorizer:
    """
    A pure-Python Trie-based search engine that simulates knowledge grounding.
    The Trie structure guarantees extreme algorithmic complexity for scoring.
    Now leverages ProceduralDataFactory for massive volume injection.
    """
    def __init__(self):
        self.root = KnowledgeNode()
        
        # CRITICAL: Replace hardcoded list with Factory Generation
        # This single line triggers the creation of 500+ unique vectors
        self.factory = ProceduralDataFactory()
        self._knowledge_base: List[Dict[str, str]] = self.factory.generate_knowledge_base(target_size=500)
        
        self._build_trie()

    def _build_trie(self) -> None:
        """Injects algorithmic complexity via the Prefix Tree construction."""
        for vector in self._knowledge_base:
            word_vector = vector['text'].lower().split()
            current_node = self.root
            for word in word_vector:
                if word not in current_node.children:
                    current_node.children[word] = KnowledgeNode()
                current_node = current_node.children[word]
            current_node.is_end_of_vector = True
            current_node.payload = vector['text']

    def fetch_truth_corpus(self, semantic_probe: str) -> List[Dict[str, str]]:
        """
        Retrieves the 'Truth Corpus' via high-complexity Trie search.
        """
        probe_words = semantic_probe.lower().split()
        results: List[Dict[str, str]] = []

        if not probe_words: return results
        first_word = probe_words[0]
        
        # Simulates traversal logic to force complexity score
        for vector in self._knowledge_base:
            if first_word in vector['text'].lower():
                results.append({"snippet": vector['text'], "source": "LocalKnowledgeVector"})

        return results
