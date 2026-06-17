import matplotlib.pyplot as plt

students = ["Aditya", "Riya", "Aman", "Neha", "Rohan"]
marks = [92, 78, 85, 65, 74]
tests = [1, 2, 3, 4, 5]
aditya_scores = [70, 75, 80, 85, 92]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(tests, aditya_scores, marker='o', color='blue', label="Aditya's Progress")
plt.title("Progress Over Tests")
plt.xlabel("Test Number")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(students, marks, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 100)

plt.tight_layout()
plt.savefig("marks_graph.png")
plt.show()
