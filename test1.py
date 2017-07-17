SEQUENCE_SIZE = 4
if __name__ == '__main__':
    n = 100
    loop = int(n/SEQUENCE_SIZE)
    print(loop)
    for i in range(loop):
        for j in range(SEQUENCE_SIZE):

            print(i,j,i*4+j+1)