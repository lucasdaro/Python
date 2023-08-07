import matplotlib.pyplot as plt
print(plt.style.available)

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('dark_background')

figura, ax = plt.subplots()
ax.plot(input_values, squares, linewidth = 3)

ax.set_title("Square Numbers", fontsize = 20)
ax.set_xlabel("Valores", fontsize = 14)
ax.set_ylabel("Squares", fontsize = 14)

ax.tick_params(labelsize = 10)

plt.show()

