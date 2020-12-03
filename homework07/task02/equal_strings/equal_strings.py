"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(first: str, second: str) -> bool:
    if bool(first) != bool(second):
        return False
    elif not first and not second:
        return True
    else:
        tmp_first = ""
        tmp_second = ""
        for c in first:
            if c == "#":
                if tmp_first:
                    tmp_first = tmp_first[:-1]
            else:
                tmp_first += c
        for c in second:
            if c == "#":
                if tmp_second:
                    tmp_second = tmp_second[:-1]
            else:
                tmp_second += c
        return tmp_first == tmp_second
