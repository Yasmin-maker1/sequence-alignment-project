# From Algorithm Theory to Molecular Biology: A Computational Study of Sequence Alignment Algorithms

**Course:** CSCI 7432 – Algorithms and Data Structures  
**Institution:** Georgia Southern University | Department of Computer Science  
**Semester:** Spring 2026  
**Instructor:** Dr. Yao Xu  
**Author:** Yasmin Rocio Orduz Landazabal | yo00553@georgiasouthern.edu  
**Project Type:** Application  

---

## Overview

This project implements and analyzes two foundational sequence alignment algorithms — **Needleman-Wunsch** (global alignment) and **Smith-Waterman** (local alignment) — and examines how dynamic programming supports critical problems in molecular biology. Both algorithms are implemented from scratch in Python without relying on external bioinformatics libraries.

The project bridges algorithm theory and real biological applications by applying both methods to protein comparison, mutation detection, and short motif matching using sequences from UniProt and NCBI.

---

## Algorithms

### Needleman-Wunsch (Global Alignment)
Introduced by Needleman & Wunsch (1970), this algorithm computes the optimal **global** alignment between two sequences by forcing an end-to-end comparison. It is best suited for sequences of similar length and biological origin, such as homologous proteins.

- **Time complexity:** O(mn)
- **Space complexity:** O(mn)
- **Approach:** Dynamic programming with gap penalty initialization and full traceback from bottom-right to top-left

### Smith-Waterman (Local Alignment)
Introduced by Smith & Waterman (1981), this algorithm finds the optimal **local** alignment — the highest-scoring subsequence match between two sequences. It is best suited for finding conserved regions, motifs, or mutations within longer sequences.

- **Time complexity:** O(mn)
- **Space complexity:** O(mn)
- **Key difference from NW:** Zero floor on all matrix cells; traceback starts at the maximum score cell and stops at zero

---

## Project Structure
```
Sequence-Alignment-Project/
├── src/
│   ├── __init__.py
│   ├── needleman_wunsch.py      # Global alignment implementation
│   ├── smith_waterman.py        # Local alignment implementation
│   └── scoring.py               # Scoring scheme (match, mismatch, gap)
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py       # Formal validation test suite (19 tests)
├── experiments/
│   ├── runtime_experiment.py    # Empirical O(mn) complexity validation
│   └── biological_experiments.py # Real biological sequence experiments
├── data/
│   └── sequences/               # FASTA files from UniProt and NCBI
├── main.py                      # Demo script with example alignments
├── requirements.txt             # Python dependencies
└── README.md
```

---

## Scoring Scheme

| Parameter | Value |
|-----------|-------|
| Match | +1 |
| Mismatch | -1 |
| Gap penalty | -2 |

These can be modified in `src/scoring.py`.

---

## Requirements

- Python 3.9 or higher
- matplotlib (for runtime plots)
```bash
pip install matplotlib
```

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Yasmin-maker1/Sequence-Alignment-Project.git
cd Sequence-Alignment-Project
```

### 2. Run the demo
```bash
python main.py
```

### 3. Run the test suite
```bash
python tests/test_algorithms.py
```
Expected output: **19/19 tests passing**

### 4. Run biological experiments
```bash
python experiments/biological_experiments.py
```

### 5. Run runtime complexity experiment
```bash
python experiments/runtime_experiment.py
```

---

## Biological Experiments Summary

| Experiment | Sequences | Algorithm | Key Result |
|------------|-----------|-----------|------------|
| Protein comparison | Human vs horse hemoglobin α | Needleman-Wunsch | 88% identity, 142-position alignment |
| Mutation detection | BRCA1 wild-type vs 185delAG | Smith-Waterman | Gaps at deletion site identified |
| Motif matching | TATA box vs promoter region | Smith-Waterman | Score 7 (with motif) vs 2 (without) |

---

## References

1. Needleman, S. B., & Wunsch, C. D. (1970). *Journal of Molecular Biology, 48*(3), 443–453.
2. Smith, T. F., & Waterman, M. S. (1981). *Journal of Molecular Biology, 147*(1), 195–197.
3. Altschul, S. F., et al. (1990). *Journal of Molecular Biology, 215*(3), 403–410.
4. Chao, J., Tang, F., & Xu, L. (2022). *Biomolecules, 12*(4), 546.
5. Zielezinski, A., et al. (2019). *Genome Biology, 20*, 144.
6. Petti, S., et al. (2023). *Bioinformatics, 39*(1), btac724.
7. Alberts, B., et al. (2019). *Essential Cell Biology* (5th ed.). W. W. Norton.

---

## GenAI Use Statement

Claude (Anthropic, claude.ai, Claude Sonnet 4.6) was used on February 12, 2026, to support preliminary project development, including identification of relevant academic references and initial exploration of biological datasets. Claude was additionally used on March 16, 2026, to assist with code review, test suite development, biological experiment design, and README writing as part of the learning and documentation process.