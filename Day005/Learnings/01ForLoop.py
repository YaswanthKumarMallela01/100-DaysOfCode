fruits = ["Apple", "Banana", "Strawberry"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# ---------------> Functions to code

scores = [128, 185, 143, 156, 175, 199, 187, 125, 122, 110, 134, 177, 186]
total_scores = sum(scores)  # Sum function returns the sum of all the numbers in the list

sum_using_forLoop = 0
# Replicating Sum function using for loop
for score in scores:
    sum_using_forLoop += score
print(f"\nSum using for Loop: {sum_using_forLoop}")

max_score = max(scores)  # Max function returns the maximum score in the list
# Replicating Max function using for loop
max_using_forLoop = 0
for score in scores:
    if score > max_using_forLoop:
        max_using_forLoop = score
print(f"\nMax using for loop: {max_using_forLoop}")

# -----------------> Range Function in for loop

for num in range(1, 10):  # 1 <= num < 10, 10 is exclusive. So it will only print from 1 to 9
    print(num)

print("\n")
for num in range(1, 10, 3):  # Here 3 is step number. It prints 1, 4, 7 because it steps 3 times before printing
    print(num)

# Sum of 1 to 100 using range function
sum_1To100 = 0
for num in range(1, 101):  # 101 is exclusive
    sum_1To100 += num
print(f"Sum of 1 to 100 using range function is: {sum_1To100}")
