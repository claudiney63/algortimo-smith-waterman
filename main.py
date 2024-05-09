import smith_waterman as sw
import backtrace as tb
import read_input_from_file as rif
import write_alignment_to_file as waf

def main(seq1, seq2, match_score, miss_score, gap_penalty, output_file):
    # Executa o algoritmo de Smith-Waterman
    scores_matrix = sw.smith_waterman(seq1, seq2, match_score, miss_score, gap_penalty)

    # Realiza o traceback para obter o alinhamento das sequências
    aligned_seq1, aligned_seq2 = tb.trace_back(scores_matrix, seq1, seq2, gap_penalty)

    # Escreve o alinhamento e a matriz de pontuações no arquivo de saída
    waf.write_alignment_to_file(aligned_seq1, aligned_seq2, scores_matrix, output_file)


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    seq1, seq2, scores = rif.read_input_from_file(input_file)
    match_score, miss_score, gap_penalty = scores
    main(seq1, seq2, match_score, miss_score, gap_penalty, output_file)