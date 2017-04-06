# https://www.hackerrank.com/challenges/nested-list
def getKey(item):
    return item[1]

if __name__ == '__main__':
    n = int(input())
    result_list = list()
    for i in range(0,n):
        name = input()
        score = float(input())
        result_list.insert(i, [name, score])
    sort_list = sorted(result_list,key=getKey)
    MIN = min(sort_list,key=getKey)
    Min_count = 0
    for i in range(0,n):
        if sort_list[i][1] == MIN[1]:
            Min_count += 1
    result = []
    for j in range(Min_count, n):
        NEW_MIN = sort_list[Min_count][1]
        if sort_list[j][1] == NEW_MIN:
            result.append(sort_list[j][0])
    result.sort()
    for k in result:
        print(k)


    # Find the MIN.
    # Remove all the elements with MIN.
    # [ num for num in numbers if num < 5 ]
    # Find the MIN again, which is the second lowest.
    # Find all the element with the second MIN.
    # Sort the results based on the name.