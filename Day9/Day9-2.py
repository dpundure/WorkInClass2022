def get_common_elements(seq1, seq2, seq3):
    return tuple(set(seq1) & set(seq2) & set(seq3))


print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))

