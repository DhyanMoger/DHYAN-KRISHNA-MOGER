num = int(input("Enter a Number: "))

if num % 2 == 0:
    num = num - 1

result = []

for i in range(1, num + 1, 2):
    result.append(i)

print(*result, sep=",")