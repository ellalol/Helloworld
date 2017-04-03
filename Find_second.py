# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(input())
    arr_list = list(map(int, input().split()))
    print(arr_list)
    sort_list = arr_list.sort()
    print(sort_list) ########## why is None????
    a = max(arr_list)
    print(a)
    N = arr_list.count(a)
    print(N)
    second = sort_list.pop(N + 1)
    print(second)