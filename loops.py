# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit, "Pie")

# for number in range(1, 51):
#     print(number)

student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(high_score)
print(max(student_scores))

low_score = student_scores[0]
for score in student_scores:
    if score < low_score:
        low_score = score
print(low_score)
print(min(student_scores))

total_score = 0
for score in student_scores:
    total_score += score
print(total_score)
print(sum(student_scores))