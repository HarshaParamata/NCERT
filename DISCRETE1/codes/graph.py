import numpy as np
import matplotlib.pyplot as plt

# Define the range of n
n = np.arange(0, 45)  # Adjust the range as needed

# Define the function x[n]
x_n = 121 - 4 * n

# Find the index of the first negative term
first_negative_index = np.argmax(x_n < 0)

# Plot x[n] vs n
plt.stem(n, x_n, linefmt='b-', markerfmt='bo', basefmt=' ')

# Highlight the first negative term
plt.annotate('First Negative Term', xy=(first_negative_index, x_n[first_negative_index]), 
             xytext=(first_negative_index + 2, x_n[first_negative_index] + 10),
             arrowprops=dict(facecolor='red', shrink=0.05))

# Add labels and title
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Graph of x[n] = 121 - 4n')

# Show plot
plt.grid(True)
plt.show()
