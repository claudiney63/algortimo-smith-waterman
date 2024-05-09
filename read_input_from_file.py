def read_input_from_file(filename):
    with open(filename, 'r') as file:
        seq1 = file.readline().strip()
        seq2 = file.readline().strip()
        scores = [int(score) for score in file.readline().strip().split()]
    return seq1, seq2, scores