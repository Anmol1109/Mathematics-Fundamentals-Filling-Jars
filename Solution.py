inp = [int(a) for a in input().split()]
t = 0
for i in range(inp[1]):
    inp1 = [int(a) for a in input().split()]
    t += (inp1[1] - inp1[0] + 1) * inp1[2];
print(int(t/inp[0]))
