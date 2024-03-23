import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with your actual dataset file)
data = pd.read_csv('file.csv')

# Assuming your dataset has columns named 'x' and 'y' for x and y values
x_values = data['x']
y_values = data['y']

# Create a scatter plot
plt.scatter(x_values, y_values)

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Your Title')

# Show the plot
plt.show()