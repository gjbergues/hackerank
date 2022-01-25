import sys

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    print(f'x : {line}')
    print(f'y : {line}')

print("Exit")