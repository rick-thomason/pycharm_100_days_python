import random
import pandas as pd

# List Comprehension
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = 'roland'.title()
letters = [letter for letter in name]

doubled = [num * 2 for num in range(1, 5)]

names = ['Amy', 'Beth', 'Rick', 'Caroline', 'Eleanor', 'Maddox']
long_and_upper = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension
student_scores = {name: random.randint(50, 100) for name in names}
# print(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score > 70}
# print(passed_students)

# Looping through a pandas dataframe
student_dict = {
    'student': ['Rick', 'Roland', 'Maddox'],
    'score': [77, 88, 99]
}

student_df = pd.DataFrame(student_dict)
# print(student_df)

# for (key, value) in student_df.items():
#     print(key)

# Loop through the rows of the dataframe
for (index, row) in student_df.iterrows():
    print(row['student'])