# Write a program to use matplotlib and plot various graphs like line plots, scatter plots, box plots, bar
# charts, pie charts etc.

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Create multiple plots
plt.figure(figsize=(12, 8))

# 1. Line Plot
plt.subplot(2, 3, 1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Y")

# 2. Scatter Plot
plt.subplot(2, 3, 2)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

# 3. Box Plot
plt.subplot(2, 3, 3)
plt.boxplot(y)
plt.title("Box Plot")

# 4. Bar Chart
plt.subplot(2, 3, 4)
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X")
plt.ylabel("Y")

# 5. Pie Chart
plt.subplot(2, 3, 5)
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(y, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")

# Display all plots
plt.tight_layout()
plt.show()