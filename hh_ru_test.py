

def check_all_students_passed(scores_input: str, names_input: str) -> str:
    class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

    names: list[str] = names_input.split(",")
    scores: list[int] = [ int(score) for score in  scores_input.split(",")]


    students = [ Student(names[i], scores[i])  for i in range(len(names))  ]
    failed_students = [ student for student in students if student.score < 35 ]

    if len(failed_students) == 0:
        print("Все сдали")
    else:
        print("Есть не сдавшие")
        print( [  st.name  for st in failed_students ])



scores_input = input()
names_input = input()
result = check_all_students_passed(scores_input, names_input)
print(result)

