# src/smith_waterman.py

from src.scoring import score, GAP_PENALTY

def smith_waterman(seq1, seq2):

    m = len(seq1)
    n = len(seq2)

    # Create matrix (all zeros) — KEY DIFFERENCE FROM NW:
    # First row AND column stay as zeros (not gap penalties)
    # This allows alignment to start anywhere in either sequence
    matrix = [[0] * (n + 1) for _ in range(m + 1)]

    max_score = 0      # Tracks the highest score anywhere in the matrix (starts at 0)
    max_pos   = (0, 0) # Tracks the position (row, column) of that highest score (starts at origin)
    # Important: SW's traceback starts at the maximum cell, not the bottom-right corner

    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            diagonal = matrix[i-1][j-1] + score(seq1[i-1], seq2[j-1])
            up       = matrix[i-1][j]   + GAP_PENALTY
            left     = matrix[i][j-1]   + GAP_PENALTY

            # KEY DIFFERENCE: 0 is always an option (zero floor)
            # If all three options are negative, reset to 0 instead
            # This means: "start a fresh local alignment here"
            matrix[i][j] = max(0, diagonal, up, left)

            # Track the highest score and its position
            # So we know exactly where the best local alignment ends
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_pos   = (i, j)

    # Traceback
    aligned1 = ""
    aligned2 = ""
    i, j = max_pos # KEY DIFFERENCE: traceback starts at the cell with the highest score

    # KEY DIFFERENCE: stop when we hit a zero (not the top-left corner like NW)
    while i > 0 and j > 0 and matrix[i][j] != 0:

        current = matrix[i][j]

        if current == matrix[i-1][j-1] + score(seq1[i-1], seq2[j-1]):
            aligned1 = seq1[i-1] + aligned1
            aligned2 = seq2[j-1] + aligned2
            i -= 1
            j -= 1

        elif current == matrix[i-1][j] + GAP_PENALTY:
            aligned1 = seq1[i-1] + aligned1
            aligned2 = "-"       + aligned2
            i -= 1

        else:
            aligned1 = "-"       + aligned1
            aligned2 = seq2[j-1] + aligned2
            j -= 1

    return aligned1, aligned2, max_score, max_pos
    # aligned1:   The first sequence with gaps inserted
    # aligned2:   The second sequence with gaps inserted
    # max_score:  The best local alignment score
    # max_pos:    Where in the matrix that best alignment ended