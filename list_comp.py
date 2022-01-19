# Enter your code here. Read input from STDIN. Print output to STDOUT
X = 1
Y = 1
Z = 2
N = 2

ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print(ans)