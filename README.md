# Klingon LLM Architecture Proof (ICT3507C)

**Module:** ICT3507C Large-Language Models (LLM) Architecture  
**Author:** Gwendalynn Lim (Lim Wan Ting Gwendalynn)  
**Institution:** Singapore Institute of Technology (SIT)  
**Email:** gwendalynn.lim@sit.singaporetech.edu.sg  

---
![Aliens training an LLM](assets/alien_comic.png)

This repository serves as a verifiable portfolio demonstrating proficiency in Large Language Models (LLMs), including transformer architectures, encoder-decoder models, attention mechanisms, and positional embeddings.

**Crucially, Klingon is not utilized here for novelty.** Rather, its highly rigid Object-Verb-Subject (OVS) syntax and extreme agglutinative grammar provide a perfect programmatic test-bed to prove the core thesis of LLM learning: *Distributional Semantics*. This project demonstrates that LLMs do not inherently understand "meaning" via dictionaries, but rather map semantic relationships through high-dimensional geometric context. 

## Files Included

1. `paper.html`: The core thesis document. **[View the live Interactive Paper here!](https://evecount.github.io/klingon_LLM/paper.html)** Open this in any modern web browser to view the interactive breakdown of how Transformers handle Klingon's Object-Verb-Subject (OVS) syntax and extreme agglutination.
2. `klingon_transformer.py`: A toy Python script implementing the mathematical proofs discussed in the paper. It simulates Byte-Pair Encoding (BPE) sub-word tokenization and $Q \times K^T$ Self-Attention matrices resolving OVS structural dependencies.

## How to run the Simulation

No external deep learning libraries (like PyTorch or TensorFlow) are required to run the toy proof, as the matrices are computed natively using standard Python structures for maximal portability.

Simply execute the script in your terminal:
```bash
python klingon_transformer.py
```