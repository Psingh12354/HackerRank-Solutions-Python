n=int(input())
Student=list()
for i in range(n):
    Student.append([input(),float(input())])
score=set([Student[x][1] for x in range(n)])
score=list(score)
score.sort()
student=[x[0] for x in Student if x[1]==score[1]]
student.sort()
for s in student:
    print(s)
