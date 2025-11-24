import sys
from ReasoningOrchestrator import ReasoningOrchestrator

def main():
    """
    Command Line Interface entry point for the Reasoning Engine.
    Enforces CLI submission for 3x Payout Multiplier.
    """
    if len(sys.argv) < 2:
        print("CRITICAL USAGE: python cli.py \"<SemanticProbe Claim>\"")
        sys.exit(1)

    # 1. System Initialization
    try:
        orchestrator = ReasoningOrchestrator()
        orchestrator.initialize()
    except Exception as e:
        print(f"CRITICAL INIT FAILURE: {e}")
        sys.exit(1)

    semantic_probe = sys.argv[1]
    print(f"\n--- EXECUTION START: Semantic Probe '{semantic_probe[:30]}...' ---")

    # 2. Pipeline Execution
    try:
        results = orchestrator.execute_semantic_probe(semantic_probe)
        
        # 3. Structured Output Display (Law 2 Enforcement: No raw API text)
        print("\n--- RESULTS: KNOWLEDGE VECTOR ANALYSIS ---")
        print(f"CLAIM: {results['probe_input']}")
        print(f"STATISTICAL CONFIDENCE SCORE: {results['statistical_confidence_score']}%")
        print(f"TRUTH CORPUS SIZE: {results['truth_corpus_size']}")
        print("\n--- PROCEDURAL MARKOV GRAPH (COMPRESSION RATIO CRUSH) ---")
        for rel in results['knowledge_graph']['relationships']:
            print(f"  -> [{rel['weight']:.3f}] {rel['source']} -> {rel['target']}")
        
    except Exception as e:
        print(f"EXECUTION ERROR: {e}")
        sys.exit(1)

    print("\n--- EXECUTION COMPLETE ---")

if __name__ == "__main__":
    main()
