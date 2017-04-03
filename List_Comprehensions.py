# https://www.hackerrank.com/challenges/list-comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # for X in range(0,x+1):
    #     for Y in range(0,y+1):
    #         for Z in range(0,z+1):
    #             if X+Y+Z != n:
    #                 print(X,Y,Z)
    result_list = [[X,Y,Z] for X in range(0,x+1) for Y in range(0,y+1) for Z in range(0,z+1) if X+Y+Z != n]
    print(result_list)
