if __name__ == "__main__":
    arr = list();
    N = "12\ninsert 5 7\ninsert 0 6"
    commands = N.split("\n")
    for n in range(1,len(commands)):
        print(commands[n])
        str = commands[n]
        list = str.split(" ")
        print(list)
        if list[0] == 'insert':
            arr.insert(list[1],list[2])
