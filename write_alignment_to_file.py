def write_alignment_to_file(aligned_seq1, aligned_seq2, scores_matrix, filename):
    with open(filename, 'w') as file:
        file.write("Matriz de pontuacoes:\n")
        for row in reversed(scores_matrix):
            file.write(' '.join(map(str, row)) + '\n')
        file.write("\nAlinhamento 1: " + aligned_seq1 + "\n")
        file.write("Alinhamento 2: " + aligned_seq2 + "\n")