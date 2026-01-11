numbers = [1, 2, 3, 1, 4, 2, 5]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate elements:", list(duplicates))