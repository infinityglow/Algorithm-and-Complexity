"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of string matching solved by Horspool's algorithm
# complementarity of DNA base pair, which has great similarity to string matching
# method `get_shift_table` builds a shift table from a given pattern
# method `convert` is for converting A to T, T to A, C to G and G to C
# time complexity: Θ(mn) for the worst case, even worse than brute-force approach,
# e.g. text = 000000000000000000, pattern = 10000
# Θ(n) for the average case

def shift_table(p, m):
    table = {}
    for i in range(m):
        table[p[i]] = m
    for j in range(m-1):
        table[p[j]] = m-1-j
    return table

def Horspool(text, pattern):
    n = len(text); m = len(pattern)
    text = convert(text)
    table = shift_table(pattern, m)
    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m-1-k] == text[i-k]:
            k += 1
        if k == m:
            return i - m + 1
        else:
            i += table[text[i]]
    return -1

# to convert A-T and C-G pairs
def convert(ori_text):
    dic = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    temp = []
    for char in ori_text:
        conv_char = dic[char]
        temp.append(conv_char)
    conv_text = ''.join(temp)
    return conv_text


plain_text = "TCGAGAATTCCTA"
pattern = "CTTAAG"
print("String matching solved by Horspool's algorithm:\n")
print("The plain text is %s" % plain_text)
print("The pattern string is %s\n" % pattern)
status = Horspool(plain_text, pattern)
if status != -1:
    print("String matching is successful, the index of first occurrence is %d." % status)
else:
    print("String matching in unsuccessful.")