import matplotlib.pyplot as plt

def x_n(n, x_0, d):
    return x_0 + n * d

x_0 = 7/3
d = 8/3

# Generate values for n from 0 to 10 (you can adjust the range as needed)
n_values = list(range(11))
x_values = [x_n(n, x_0, d) for n in n_values]

# Plotting the stem graph
plt.stem(n_values, x_values, basefmt='b-', linefmt='r-', markerfmt='ro')
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Stem Graph of x(n)')
plt.grid(True)
plt.show()
