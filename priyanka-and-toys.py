length = int(raw_input())
weights = map(int, raw_input().strip().split(" "))
cost = [0,0,0,0,0]
for i in range(length):
    for j in range(length):
        if weights[i] > weights[j] or weights[i] + 4 < weights[j] or weights[i] == weights[j]:
            cost[i] += 1
print(min(cost))