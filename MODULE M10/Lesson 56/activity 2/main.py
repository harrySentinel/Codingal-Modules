def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

students = ["Riya", "Aman", "Aditya", "Neha", "Rohan"]
target = "Aditya"

index = linear_search(students, target)
if index != -1:
    print(target, "found at index", index)
else:
    print(target, "not found")

print("This is O(n) - time grows with input size.")
