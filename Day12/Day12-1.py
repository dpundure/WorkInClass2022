def file_line_len(fname):
    file_length = 0
    with open(fname, encoding="UTF-8") as f:
        for i in f:
            file_length +=1
        return file_length


print(file_line_len("veidenbaums.txt"))


def get_poem_lines(fname):
    clean_lines = []
    with open(fname, encoding="UTF-8") as f:
        for line in f:
            if line.strip() and "***" not in line:
                clean_lines.append(line)
    return clean_lines


print(len(get_poem_lines("veidenbaums.txt")))
