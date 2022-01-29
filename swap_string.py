
def swap_case(s):
    ns = ''
    for i in range(0, len(s)):
        if s[i].isupper():
            a = s[i].lower()
        else:
            a = s[i].upper()
        ns = ns + a
    return ns

name = 'Guillermo'

nname = swap_case(name)

print(nname)