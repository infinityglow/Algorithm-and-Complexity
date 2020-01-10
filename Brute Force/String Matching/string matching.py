"""
# -*- coding: utf-8 -*-
@author: Hongzhi Fu
"""

# implementation of string matching solved by brute-force approach
# complementarity of DNA base pair, which has great similarity to string matching
# method `convert` is for converting A to T, T to A, C to G and G to C


def string_matching_bf(text, pattern):
    text = convert(text)
    n = len(text); m = len(pattern)
    for i in range(n-m+1):
        j = 0  # count the number of matching pairs
        while j < m and pattern[j] == text[i+j]:
            j += 1
        if j == m:
            return i
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
print("String matching solved by brute force approach:\n")
print("The plain text is %s" % plain_text)
print("The pattern string is %s\n" % pattern)
status = string_matching_bf(plain_text, pattern)
if  status != -1:
    print("String matching is successful, the index of first occurrence is %d." % status)
else:
    print("String matching in unsuccessful.")
