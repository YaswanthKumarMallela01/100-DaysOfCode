"""Dictionary comprehension in Python offers a concise and efficient way to create dictionaries.
 It provides a more compact syntax compared to traditional for loops for constructing dictionaries
  from iterables."""
import pandas
import random

dict_names = ["Rama", "Sita", "Lakshmana", "Ravana"]
scores = {student: random.randint(1, 100) for student in dict_names}
print(scores)
passed_students = {student: score for (student, score) in scores.items() if score >= 60}
print(passed_students)
print()

student_dict = {
    "students": ["Rama", "Sita", "Lakshmana", "Ravana"],
    "scores": [95, 96, 85, 42]
}

student_dataframe = pandas.DataFrame(student_dict)
for (index, row) in student_dataframe.iterrows():
    print(index)
for (index, row) in student_dataframe.iterrows():
    print(row.students)
for (index, row) in student_dataframe.iterrows():
    print(row.scores)