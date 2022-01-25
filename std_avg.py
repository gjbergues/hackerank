dict = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}

std = 'Malika'

n_std = 3

print(sum(dict[std])/len(dict[std]))

avg_r = sum(student_marks[query_name])/len(student_marks[query_name])
avg_r = "{:.2f}".format(avg_r)
print(avg_r)