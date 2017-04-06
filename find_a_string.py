def count_substring(string, sub_string):
    n = len(sub_string)
    n_str = len(string)
    count = 0
    for i in range(0,n_str-n+1):
        if string[i:i+n] == sub_string:
            count = count +1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)