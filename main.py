# Função que implementa o algortimo-smith-waterman para o alinhamento global de duas sequências de caracteres
def smith_waterman(seq1, seq2, match_score, miss_score, gap_penalty):

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
            match_or_miss = matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else miss_score)
            print(seq1[i - 1], seq2[j - 1])
            gap1_row = matrix[i - 1][j] + gap_penalty
            gap2_col = matrix[i][j - 1] + gap_penalty

            print(f"match_or_miss: {match_or_miss}, gap1_row: {gap1_row}, gap2_col: {gap2_col}")
            
            # Atribuição do maior valor entre match, delete e insert à célula atual
            matrix[i][j] = max(match_or_miss, gap1_row, gap2_col)

            for row in matrix:
                print(row)
            print()

    return matrix  # Retorna a matriz de pontuações


# Sequências a serem alinhadas
seq1 = "ATGGGAA"
seq2 = "CACTCG"

# Pontuações para match, mismatch e gap
match_score = 1
miss_score = -1
gap_penalty = -2

# Executa o algoritmo smith-waterman para calcular a matriz de pontuações
scores_matrix = smith_waterman(seq1, seq2, match_score, miss_score, gap_penalty)

print("\nMatriz de pontuacoes:")
# Imprime a matriz
for row in reversed(scores_matrix):
    print(row)
