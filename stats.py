def count_words(string):
    return len(string.split())

def count_char(string):
    chars = {}
    for c in string:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict(dict):
    sorted_list = []
    for key in dict:
        sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=lambda item: item["num"])
    return sorted_list