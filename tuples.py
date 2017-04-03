# https://www.hackerrank.com/challenges/python-tuples
import hashlib
if __name__ == '__main__':
    n = int(input())
    str_list = input().split(" ")
    int_list = list(map(int, str_list))
    tup = tuple(int_list)
    print(hash(tup))
