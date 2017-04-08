# https://www.hackerrank.com/challenges/python-string-formatting
def print_formatted(number):
    # your code goes here
    l = len(bin(number)[2:])
    for i in range(1,number+1):
        i_octal = oct(i)[2:]
        i_hex = hex(i)[2:].swapcase()
        i_bi = bin(i)[2:]
        i_str = str(i)
        print(i_str.rjust(l),i_octal.rjust(l),i_hex.rjust(l),i_bi.rjust(l))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)