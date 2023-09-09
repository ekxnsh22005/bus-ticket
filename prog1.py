t = int(input())
results = []

for _ in range(t):
    x, y, z = map(int, input().split())
    s = x * 10

    if y >= s:
        result = s * z
    else:
        result = z * y

    results.append(result)

for result in results:
    print(result)
