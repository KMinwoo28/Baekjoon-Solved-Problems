grade = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
gradescore = 0
multiplex = 0
for i in range(20):
    sub, credit, applied = map(str,input().split())
    if applied in grade:
        gradescore += float(credit)
        multiplex += float(credit)*score[grade.index(applied)]
print(multiplex/gradescore)