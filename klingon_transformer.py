import math

def print_header(title):
    print(f"\n{'='*60}")
    print(f" {title}")
    print(f"{'='*60}")

# ==========================================
# 1. BPE TOY TOKENIZER (AGGLUTINATION)
# ==========================================
def run_bpe_simulation():
    print_header("1. Tokenization & Embeddings (Agglutination)")
    print("Demonstrating Byte-Pair Encoding (BPE) on highly agglutinative Klingon words.")
    
    # Vocabulary dictionary (mock embeddings spatial locations)
    vocab = {
        "Qong": "Action(Sleep)",
        "##Daq": "Modifier(Place)",
        "##Daq2": "Modifier(At/In)"
    }
    
    raw_word = "QongDaqDaq"
    print(f"\nRaw Input Word: {raw_word} (Meaning: 'in the bed' or 'sleep-place-at')")
    
    # Toy BPE split
    tokens = ["Qong", "##Daq", "##Daq"]
    print(f"BPE Sub-word Tokens: {tokens}")
    
    print("\nGeometric Translation in Latent Space:")
    current_vector_meaning = ""
    for idx, token in enumerate(tokens):
        if idx == 0:
            current_vector_meaning = vocab.get(token)
            print(f"Step 1: Root '{token}' maps to {current_vector_meaning}")
        elif idx == 1:
            current_vector_meaning += " -> Noun(Bed)"
            print(f"Step 2: Suffix '{token}' shifts vector: {current_vector_meaning}")
        elif idx == 2:
            current_vector_meaning += " -> Location(In the Bed)"
            print(f"Step 3: Suffix '{token}' final shift: {current_vector_meaning}")

# ==========================================
# 2. TOY SELF-ATTENTION (OVS SYNTAX)
# ==========================================
def run_attention_simulation():
    print_header("2. Self-Attention Matrix (Object-Verb-Subject)")
    print("Demonstrating how Self-Attention resolves Klingon OVS syntax.\n")
    
    # Input Sequence: Hiq (Ale) tlhutlh (drinks) suvwI' (warrior)
    # English equivalent: The warrior drinks the ale (SVO)
    # Klingon: Hiq tlhutlh suvwI' (OVS)
    
    sequence = ["Hiq (Ale/Obj)", "tlhutlh (Drinks/Verb)", "suvwI' (Warrior/Subj)"]
    
    # Mock Attention Scores (pre-softmax Q x K^T)
    # Row i represents the query, Col j represents the key.
    # How much attention does word i pay to word j?
    # In OVS, the Verb (idx 1) must look BACK to Object (idx 0) and FORWARD to Subject (idx 2).
    
    attention_scores = [
        # Hiq       tlhutlh    suvwI'
        [ 1.0,      0.2,       0.1 ],  # Hiq (Ale) pays attention mostly to itself
        [ 0.8,      1.0,       0.9 ],  # tlhutlh (Drinks) MUST pay high attention to BOTH neighbors
        [ 0.1,      0.3,       1.0 ]   # suvwI' (Warrior) pays attention mostly to itself
    ]
    
    print("Input Sequence (OVS Position):")
    for i, token in enumerate(sequence):
        print(f"  Pos {i}: {token}")
        
    print("\nAttention Matrix (Softmax Q x K^T mock):")
    # Print headers
    header = f"{'':>25}"
    for token in sequence:
        header += f"{token.split()[0]:>15}"
    print(header)
    
    # Print rows
    for i, query_token in enumerate(sequence):
        row_str = f"{query_token:>25}"
        for j, score in enumerate(attention_scores[i]):
            row_str += f"{score:>15.2f}"
        print(row_str)
        
    print("\nAnalysis:")
    print("Notice the 'tlhutlh' (Verb) row. To resolve the relationship, the Transformer uses Positional Embeddings")
    print("to cast a massive backward attention weight (0.80) to 'Hiq' (Object) at Position 0, and a massive forward")
    print("weight (0.90) to 'suvwI'' (Subject) at Position 2. Without Positional Embeddings, the model would fail")
    print("to differentiate the actor from the target.")

if __name__ == "__main__":
    print("\n============================================================")
    print("  KLINGON LLM ARCHITECTURE PROOF - ICT3507C DEMONSTRATION")
    print("============================================================")
    run_bpe_simulation()
    run_attention_simulation()
    print("\nSimulation Complete.\n")
