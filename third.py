import numpy as np
import matplotlib.pyplot as plt
# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)   # Create a plot
plt.plot(x, y)
# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
# Display the plot
plt.show()