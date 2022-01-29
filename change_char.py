def split_and_join(line):
    nl = ''
    for char in line:
        if char == ' ':
            a = '-'
        else:
            a = char
        nl = nl + a
    return nl

    # write your code here


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)