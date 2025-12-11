num = int(input("Enter the number: "))

result = []
i = 1 

for _ in range(num):
    result.append(i)
    i += 2
print(*result, sep=" ,")