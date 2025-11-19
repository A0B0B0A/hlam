numbers = list(map(float, input("Введіть числа через пробіл: ").split()))

# Середнє
mean = sum(numbers) / len(numbers)

# Медіана
numbers_sorted = sorted(numbers)
n = len(numbers_sorted)

if n % 2 == 1:
    median = numbers_sorted[n // 2]
else:
    median = (numbers_sorted[n // 2 - 1] + numbers_sorted[n // 2]) / 2

# Мода
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

max_count = max(frequency.values())
modes = [num for num, count in frequency.items() if count == max_count]

# Вивід
print("Середнє:", mean)
print("Медіана:", median)
print("Мода:", modes)
