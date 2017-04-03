# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(input())
    arr_list = list(map(int, input().split()))
    my_set = set(arr_list)
    new_list = list(my_set)
    new_list.sort(reverse = True)
    second = new_list.pop(1)

    print(second)
