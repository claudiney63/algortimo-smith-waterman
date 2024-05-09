def trace_back(matrix, seq1, seq2, gap_penalty):
    aligned_seq1 = ""  
    aligned_seq2 = ""  
    i = len(seq1)  
    j = len(seq2)  

    while i > 0 or j > 0:

        # Se a pontuação atual veio do canto superior esquerdo (match ou mismatch)
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + (1 if seq1[i - 1] == seq2[j - 1] else -1):
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1  # Move para a célula superior esquerda
            j -= 1

        # Se a pontuação atual veio da célula acima (gap em seq2)
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap_penalty:
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1  # Move para a célula acima

        # Se a pontuação atual veio da célula à esquerda (gap em seq1)
        else:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1  # Move para a célula à esquerda

    return aligned_seq1, aligned_seq2 
