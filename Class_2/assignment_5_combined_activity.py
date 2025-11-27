data = [14, 50, 99, 101, 22, 33, 150]

filtered = list(filter(lambda x: x > 50, data))
print("1. Filtered (>50):", filtered, "\n")

mapped = list(map(lambda x: x * 2, filtered))
print("2. Mapped (*2):", mapped, "\n")

final_list = mapped
print("3. Final List:", final_list)