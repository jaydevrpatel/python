numbers = [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
