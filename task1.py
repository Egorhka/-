numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Сумма всех элементов, кроме None
skipped_int = 0
count = 0
for i in numbers:
    count += 1
    if i is not None:
        skipped_int += i

skipped_int = skipped_int / count
# Замена None на полученную сумму
for idx, i in enumerate(numbers):
    if i is None:
        numbers[idx] = skipped_int


print("Измененный список:", numbers)
