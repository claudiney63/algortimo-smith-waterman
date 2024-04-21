# Função que implementa o algoritmo Needleman-Wunsch para o alinhamento global de duas sequências de caracteres
def needleman_wunsch(seq1, seq2, match_score, miss_score, gap_penalty):
    # Inicialização da matriz de pontuações com dimensões baseadas no comprimento das sequências mais um
    matrix = [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]

    # Preenchimento da primeira coluna da matriz com penalidades de gap
    for i in range(1, len(seq1) + 1):
        matrix[i][0] = matrix[i - 1][0] + gap_penalty

    # Preenchimento da primeira linha da matriz com penalidades de gap
    for j in range(1, len(seq2) + 1):
        matrix[0][j] = matrix[0][j - 1] + gap_penalty

    # Preenchimento da matriz de pontuações
    for i in range(1, len(seq1) + 1):
        for j in range(1, len(seq2) + 1):
            # Cálculo dos pontos para match, delete e insert
            match = matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else miss_score)
            delete = matrix[i - 1][j] + gap_penalty
            insert = matrix[i][j - 1] + gap_penalty
            # Atribuição do maior valor entre match, delete e insert à célula atual
            matrix[i][j] = max(match, delete, insert)

    return matrix  # Retorna a matriz de pontuações


# Função que realiza o traceback para obter o alinhamento das sequências
def trace_back(matrix, seq1, seq2, gap_penalty):
    aligned_seq1 = ""  # Inicialização da sequência alinhada 1
    aligned_seq2 = ""  # Inicialização da sequência alinhada 2
    i = len(seq1)  # Inicialização do índice i com o tamanho da sequência 1
    j = len(seq2)  # Inicialização do índice j com o tamanho da sequência 2

    # Enquanto houver elementos em seq1 ou seq2
    while i > 0 or j > 0:
        # Se a pontuação atual veio do canto superior esquerdo (match ou mismatch)
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + (1 if seq1[i - 1] == seq2[j - 1] else -1):
            # Adiciona o caractere correspondente de seq1 e seq2 às sequências alinhadas
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1  # Move para a célula superior esquerda
            j -= 1
        # Se a pontuação atual veio da célula acima (gap em seq2)
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap_penalty:
            # Adiciona um gap em seq2 às sequências alinhadas
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1  # Move para a célula acima
        # Se a pontuação atual veio da célula à esquerda (gap em seq1)
        else:
            # Adiciona um gap em seq1 às sequências alinhadas
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1  # Move para a célula à esquerda

    return aligned_seq1, aligned_seq2  # Retorna as sequências alinhadas


# Sequências a serem alinhadas
seq1 = "ATGGGAA"
seq2 = "CACTCG"
# Pontuações para match, mismatch e gap
match_score = 1
miss_score = -1
gap_penalty = -2

# Executa o algoritmo Needleman-Wunsch para calcular a matriz de pontuações
scores_matrix = needleman_wunsch(seq1, seq2, match_score, miss_score, gap_penalty)

# Imprime a matriz de pontuações invertida
print("Scores Matrix (inverted):")
for row in reversed(scores_matrix):
    print(row)

# Realiza o traceback para obter o alinhamento das sequências
aligned_seq1, aligned_seq2 = trace_back(scores_matrix, seq1, seq2, gap_penalty)

# Imprime as sequências alinhadas
print("\nAligned Sequence 1:", aligned_seq1)
print("Aligned Sequence 2:", aligned_seq2)
