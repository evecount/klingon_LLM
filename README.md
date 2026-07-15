# Klingon LLM Architecture Proof (ICT3507C)

This repository serves as a verifiable portfolio demonstrating proficiency in Large Language Models (LLMs), including transformer architectures, encoder-decoder models, attention mechanisms, and positional embeddings.

Instead of a generic text classifier, this project probes the structural limits of foundational Transformer models by applying them to the extreme edge-case syntax of **Klingon (tlhIngan Hol)**. 

## Files Included

1. `paper.html`: The core thesis document. Open this in any modern web browser to view the interactive breakdown of how Transformers handle Klingon's Object-Verb-Subject (OVS) syntax and extreme agglutination.
2. `klingon_transformer.py`: A toy Python script implementing the mathematical proofs discussed in the paper. It simulates Byte-Pair Encoding (BPE) sub-word tokenization and $Q \times K^T$ Self-Attention matrices resolving OVS structural dependencies.

## How to run the Simulation

No external deep learning libraries (like PyTorch or TensorFlow) are required to run the toy proof, as the matrices are computed natively using standard Python structures for maximal portability.

Simply execute the script in your terminal:
```bash
python klingon_transformer.py
```