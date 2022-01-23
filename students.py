

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
print(students)

#strings = [ ['foo', 'bar'], ['baz', 'taz'], ['w', 'koko'] ]
# [ (letter, idx) for idx, lst in enumerate(strings) for word in lst if len(word)>2 for letter in word]
# [ value for sub_list in main_list if len(sub_list) > 2 for value in sub_list ]
# d = [sub_lst[1] for sub_lst in students if sub_lst[1] > 40 for value in sub_lst]
cal_max = max([sub_lst[1] for sub_lst in students])
sec_cal = max(sub_lst[1] for sub_lst in students if sub_lst[1] < cal_max)

st_sb = sorted([sub_lst[0] for sub_lst in students if sub_lst[1] == sec_cal], key=str.lower)
print(st_sb)

cal_min = min([sub_lst[1] for sub_lst in students])
sec_cal = min(sub_lst[1] for sub_lst in students if sub_lst[1] > cal_min)

st_sb = sorted([sub_lst[0] for sub_lst in students if sub_lst[1] == sec_cal], key=str.lower)

for x in st_sb:
    print(x)