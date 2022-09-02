# This app compares datasets entries using booleans

id_1 = "#4"
average_grade_id_1 = "A"
average_score_id_1 = 60

id_2 = "#5"
average_grade_id_2 = "A"
average_score_id_2 = 70

print('Are the student the same?')
print(id_1 == id_2)

print('Do they have the same grade?')
print(average_grade_id_1 == average_grade_id_2)

print('Who got the highest score?')

if average_score_id_1 > average_score_id_2:
    print(id_1)
else:
    print(id_2)
