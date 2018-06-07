# -*- coding: utf-8 -*-
# python


def adjust_str(chars):
    star_idx = len(chars) - 1
    while star_idx > 0 and chars[star_idx] != '*':
        star_idx -= 1
    star_num = 0
    char_idx = star_idx
    while char_idx >= 0:
        while char_idx > 0 and chars[char_idx] == '*':
            char_idx -= 1
            star_num += 1
        chars[char_idx], chars[star_idx] = chars[star_idx], chars[char_idx]
        char_idx -= 1
        star_idx -= 1
    return star_num

chars = list('abcd*efg**H*ijk*l***MN*')
print(adjust_str(chars), chars)
