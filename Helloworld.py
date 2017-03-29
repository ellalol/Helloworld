def read():
    s = input("Please enter your name:")
    return s
if __name__ == '__main__':
    my_str = read()
    print (my_str)
    print("Hello, World!")

    x = 1
    if x < 0:
        x = 0
        print ("Negative changed to zero")
    elif x == 0:
        print("Zero")
    elif x == 1:
        print("Single")
    else:
        print("More")

    a = int(input())
    b = int(input())
    sum = a + b
    diff = a - b
    prod = a * b
    print(sum)
    print(diff)
    print(prod)

    n = int(input())
    N = range(0, n)
    for i in N:
        res = i * i
        print(res)