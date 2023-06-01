#7
def get_top_student(grades_dict):
    highest_grade = max(grades_dict.values())
    top_student = [name for name, grade in grades_dict.items() if grade == highest_grade]
    return top_student[0]
grades = {'Іван': 78,'Марія': 85,'Петро': 27,'Костя': 89,'Андрій': 96}
top_student_name = get_top_student(grades)
print("Студент з найвищою оцінкою:", top_student_name)
