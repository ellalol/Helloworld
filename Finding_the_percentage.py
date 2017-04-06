# https://www.hackerrank.com/challenges/finding-the-percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = list(map(float, scores))
        student_marks[name] = scores
    print(student_marks)
    query_name = input()
    if query_name in student_marks:
        print(student_marks[query_name])
        sum = 0
        for i in student_marks[query_name]:
            sum = sum + i
        ave = sum/len(student_marks[query_name])
        print("%.2f" % ave)