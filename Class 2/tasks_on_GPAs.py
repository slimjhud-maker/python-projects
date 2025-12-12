# Given scores
scores = [95, 67, 88, 76, 45, 99, 100, 52]

# 1. Use map + lambda to convert each score to GPA (score / 20)
gpas = list(map(lambda x: x / 20, scores))
print("\n1. All GPAs:", gpas, "\n")

# 2. Use filter + lambda to keep only GPAs above 3.0
passed_gpas = list(filter(lambda g: g > 3.0, gpas))
print("2. Passed GPAs:", passed_gpas, "\n")

# 3. Function using *args to calculate average GPA
def average_gpa(*args):
    return sum(args) / len(args)

avg = average_gpa(*passed_gpas)
print("3. Average GPA:", avg, "\n")

# 4. Function using **kwargs to print a summary
def summary(**kwargs):
    print(f"4. Summary:\n"
          f"   Total Students: {kwargs['total']}\n"
          f"   Passed Count: {kwargs['passed']}\n"
          f"   Average GPA: {kwargs['average']:.2f}\n")

summary(total=len(scores), passed=len(passed_gpas), average=avg)