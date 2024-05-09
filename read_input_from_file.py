def read_input_from_file(filename):
    with open(filename, 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()
        gap_penalty = int(file.readline().strip())
        miss_score = int(file.readline().strip())
        match_score = int(file.readline().strip())
    return seq1, seq2, gap_penalty, miss_score, match_score