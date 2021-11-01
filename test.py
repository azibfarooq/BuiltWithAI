from student import Student
import random


subjects = ["Math", "Science", "IT", "Arabic", "Quran", "English", "French"]
x = set(
    [random.choice(subjects) for _ in range(5)]
    )

print(x)