def write_alignment_to_file(aligned_seq1, aligned_seq2, scores_matrix, seq1, seq2, filename, match_score, miss_score, gap_penalty):
    with open(filename, 'w') as file:
        file.write("Matriz de pontuacoes:\n")
        cont = 1
        for i in reversed(range(len(scores_matrix))):
            if i - cont < 0:
                file.write("U\t" + "\t".join(map(str, scores_matrix[i])) + "\n")
            else:
                file.write(seq1[i - cont] + "\t" + "\t".join(map(str, scores_matrix[i])) + "\n")
            # if i < len(seq1):
                
            # else:
            #     file.write("  " + " ".join(map(str, scores_matrix[i])) + "\n")
        file.write("\tU\t" + "\t".join(seq2) + "\n")
        file.write("\nMatch = " +str(match_score)+ "; Miss = "+str(miss_score)+ "; Gap = "+str(gap_penalty)+"; \n")
        file.write("\nAlinhamento 1: " + aligned_seq1 + "\n")
        file.write("Alinhamento 2: " + aligned_seq2 + "\n")
        file.write("\nNumero chamada: 8 \n")