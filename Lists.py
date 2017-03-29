#https://www.hackerrank.com/challenges/python-lists
#The script can run in pycharm, but not in website
# to test in website, change the N = int(raw_input())
if __name__ == "__main__":
    arr = list();
    N = int(raw_input())
    #N = "12\ninsert 0 5\ninsert 1 10\ninsert 0 6\nprint\nremove 6\nappend 9\nappend 1\nsort\nprint\npop\nreverse\nprint"
    for n in range(0, N):
        str = raw_input()
        list = str.split(" ")
        if list[0] == "insert":
            arr.insert(int(list[1]),int(list[2]))
        elif list[0] == "print":
            print(arr)
        elif list[0] == "remove":
            arr.remove(int(list[1]))
        elif list[0] == "append":
            arr.append(int(list[1]))
        elif list[0] == "sort":
            arr.sort()
        elif list[0] == "pop":
            arr.pop()
        elif list[0] == "reverse":
            arr.reverse()
