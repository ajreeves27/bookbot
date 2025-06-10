def get_num_words(filepath):
    count = 0
    with open(filepath) as f:
        read = f.read()
        w = read.split()
        count += len(w)
    return count

def get_char_nums(filepath):
    with open(filepath) as f:
        read = f.read().lower()
        letter_counts = {}
        for char in read:
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
        return letter_counts

def chars_to_sorted_list(letter_counts):
    stats_list = []
    for char, num in letter_counts.items():
        if char.isalpha():
            stats_list.append({"char": char, "num": num})
    stats_list.sort(reverse=True, key=lambda d: d["num"])
    return stats_list

    