# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement?h_r=next-challenge&h_v=zen
from __future__ import print_function
from itertools import combinations_with_replacement
from itertools import combinations

if __name__ == '__main__':
    # print(list(combinations_with_replacement('12345',2)))
    # 上面这行可以运行，但是挪到下面去就不能运行
    # A = [1, 1, 3, 3, 3]
    # print(list(combinations(A, 2)))

    text = input("Please enter:\n")
    words = text.split(" ")
    str1 = words[0]
    str2 = words[1]
    number = int(float(str2))

    str_list = sorted(str1)
    new_str = ''.join(str_list)
    # new_str = ''
    # for i in str_sort:
    #     new_str = new_str + i
    print(new_str)
    # print(list(combinations_with_replacement('12345', 2)))
    print(list(combinations_with_replacement(new_str, number)))
    # 运行出错，并且改参数也出错
