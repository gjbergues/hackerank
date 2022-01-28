"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.


"""

if __name__ == '__main__':
    N = int(input())

m = list()
for i in range(N):
    method, *l = input().split()
    k = list(map(int, l))
    if len(k) == 2:
        q = [k[0]]
        w = [k[1]]
    elif len(k) == 1:
        q = [k[0]]
    if method == 'insert':
        m.insert(q[0], w[0])
    elif method == 'append':
        m.append(q[0])
    elif method == 'remove':
        m.remove(q[0])
    elif method == 'print':
        print(m)
    elif method == 'reverse':
        m.reverse()
    elif method == 'pop':
        m.pop()
    elif method == 'sort':
        m.sort()