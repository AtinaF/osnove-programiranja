ab = "aaabbbcccddd"
b = ab[:-1]
print(b)

student = {"a" : "b",
           "c" : "1",
           "d" : "ee"}
student2 = {"a" : "b2",
           "c" : "12",
           "d" : "ee2"}
studenti = [student, student2]
print(studenti)

stu = studenti[0]
stu["a"] = "mmm"

print(studenti)