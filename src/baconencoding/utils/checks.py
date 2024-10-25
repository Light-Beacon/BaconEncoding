def char_is_between(string,start_char,end_char):
    for char in string:
        if char < start_char or char > end_char:
            return False
    return True