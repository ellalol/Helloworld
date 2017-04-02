# https://www.hackerrank.com/challenges/python-tuples
import hashlib
if __name__ == '__main__':
    n = input() #input "2"
    t_str = input() #input "2 1"
    list = t_str.split(" ")
    print(list)
    tup = tuple(list)
    print(hash(tup))