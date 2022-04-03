# a

def get_min_avg_max(sequence):
    return min(sequence), sum(sequence) / len(sequence), max(sequence)


numbers = get_min_avg_max([0, 10, 1, 9])
print(numbers)
