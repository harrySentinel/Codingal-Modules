import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
velocity = [0, 10, 20, 30, 40, 50, 45, 35, 25, 15, 0]

plt.figure(figsize=(8, 5))
plt.plot(time, velocity, marker='o', color='blue', linewidth=2, label='Velocity')
plt.fill_between(time, velocity, alpha=0.1, color='blue')
plt.title("Time vs Velocity Graph")
plt.xlabel("Time (seconds)")
plt.ylabel("Velocity (m/s)")
plt.legend()
plt.grid(True)
plt.savefig("velocity_graph.png")
plt.show()

print("Max Velocity:", max(velocity), "m/s at t =", time[velocity.index(max(velocity))], "s")
