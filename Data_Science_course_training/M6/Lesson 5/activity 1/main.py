def ways(stairs, path=""):
    if stairs == 0:
        print(path.strip())
        return
    if stairs >= 1:
        ways(stairs - 1, path + "1 ")
    if stairs >= 2:
        ways(stairs - 2, path + "2 ")

n = 4
print(f"All paths to climb {n} stairs:\n")
ways(n)

count = [0]
def count_ways(stairs):
    if stairs == 0:
        count[0] += 1
        return
    if stairs >= 1:
        count_ways(stairs - 1)
    if stairs >= 2:
        count_ways(stairs - 2)

count_ways(n)
print(f"\nTotal paths for {n} stairs: {count[0]}")
