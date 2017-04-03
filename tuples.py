# https://www.hackerrank.com/challenges/python-tuples
import hashlib
if __name__ == '__main__':
    n = int(input())
    list = input().split(" ")
    int_list = map(int, list)
    print(int_list,type(int_list)) ############# how can I print the new list
    tup = tuple(int_list)
    print(hash(tup))
