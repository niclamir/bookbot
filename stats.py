def count_words(text):
    return len(text.split())

def count_chars(text):
    counts = {}

    for c in text:
        if c.lower() in counts:
            counts[c.lower()] += 1
        else:
            counts[c.lower()] = 1

    return counts

def sort_dict(dict):
    new_dict = []

    for d in dict:
        if d.isalpha():
            new_dict.append({"char":d,"num": dict[d]})

    new_dict.sort(reverse=True, key=sort_on)
    return new_dict

def sort_on(items):
    return items["num"]