# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement?h_r=next-challenge&h_v=zen
from __future__ import print_function
from itertools import combinations_with_replacement
from itertools import combinations

if __name__ == '__main__':
    # print(list(combinations_with_replacement('12345',2)))
    # A = [1, 1, 3, 3, 3]
    # print(list(combinations(A, 2)))

    text = input("Please enter: HACK 2\n")
    words = text.split(" ")
    str1 = words[0]
    str2 = words[1]
    number = int(float(str2))

    str_list = sorted(str1)
    new_str = ''.join(str_list)
    # new_str = ''
    # for i in str_sort:
    #     new_str = new_str + i
    res = list(combinations_with_replacement(new_str, number))
    n = len(res)
    for i in range(0,n):
        res0 = ''.join(res[i])
        print(res0)
