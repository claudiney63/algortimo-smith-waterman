import smith_waterman as sw

def main():
    # Sequências a serem alinhadas
    seq1 = "ATGGGAA"
    seq2 = "CACTCG"

    # Pontuações para match, mismatch e gap
    match_score = 1
    miss_score = -1
    gap_penalty = -2

    scores_matrix = sw.smith_waterman(seq1, seq2, match_score, miss_score, gap_penalty)

    print("\nMatriz de pontuacoes:")
    for row in reversed(scores_matrix):
        print(row)


if __name__ == "__main__":
    main()