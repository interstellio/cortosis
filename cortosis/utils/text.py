

def group_chars(my_str, group=3, char='-'):
    my_str = str(my_str)
    return char.join(my_str[i:i + group] for i in range(0, len(my_str), group))
