# https://www.hackerrank.com/challenges/swap-case
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    str = input()
    new_str = swap_case(str)
    print(new_str)