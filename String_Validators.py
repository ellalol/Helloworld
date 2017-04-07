if __name__ == '__main__':
    s = input()
    flag = 0
    for i in s:
        if i.isalnum():
            print(True)
            flag = 1
            break
    if flag ==0:
        print(False)

    flag = 0
    for i in s:
        if i.isalpha():
            print(True)
            flag = 1
            break
    if flag ==0:
        print(False)

    flag = 0
    for i in s:
        if i.isdigit():
            print(True)
            flag = 1
            break
    if flag ==0:
        print(False)

    flag = 0
    for i in s:
        if i.islower():
            print(True)
            flag = 1
            break
    if flag ==0:
        print(False)

    flag = 0
    for i in s:
        if i.isupper():
            print(True)
            flag = 1
            break
    if flag == 0:
        print(False)

        # if __name__ == '__main__':
        #     s = input()
        #     alnum = alpha = digit = lower = upper = False
        #     for c in s:
        #         if c.isalnum():
        #             alnum = True
        #         if c.isalpha():
        #             alpha = True
        #         if c.isdigit():
        #             digit = True
        #         if c.islower():
        #             lower = True
        #         if c.isupper():
        #             upper = True
        #     print(alnum)
        #     print(alpha)
        #     print(digit)
        #     print(lower)
        #     print(upper)