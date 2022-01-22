
n = 5
L = [2, 3, 6, 6, 5]

# newlist = [expression for item in iterable if condition == True]

print(max([x for x in L if x < max(L)]))


