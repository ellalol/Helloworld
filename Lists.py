#https://www.hackerrank.com/challenges/python-lists
#The script can run in pycharm, but not in website
# to test in website, change the N = int(raw_input())
if __name__ == "__main__":
    arr = list();
    # N = int(raw_input())
    N = "12\ninsert 0 5\ninsert 1 10"
    commands = N.split("\n")
    for n in range(1,len(commands)):
        str = commands[n]
        list = str.split(" ")
        if list[0] == "insert":
            arr.insert(int(list[1]),int(list[2]))
            print(arr)
        elif list[0] == "print":
            print(arr)
        elif list[0] == "remove":
            arr = arr.remove(int(list[1]))
        elif list[0] == "append":
            arr = arr.append(int(list[1]))
        elif list[0] == "sort":
            arr = arr.sort()
        elif list[0] == "pop":
            arr = arr.pop()
        elif list[0] == "reverse":
            arr = arr.reverse()