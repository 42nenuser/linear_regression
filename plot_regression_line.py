import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("data.csv")  # Ensure the dataset is in the same directory

# Extract mileage (x) and price (y)
x = data['km']
y = data['price']

# Load the trained theta values from the model parameters file
try:
    with open("model_parameters.txt", "r") as file:
        lines = file.readlines()
        theta0 = float(lines[0].split(":")[1].strip())
        theta1 = float(lines[1].split(":")[1].strip())
except FileNotFoundError:
    print("Error: Model parameters not found. Please run the training program first.")
    exit()

# Plot the data points
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.7, label='Data Points')

# Plot the regression line
x_range = [min(x), max(x)]
y_range = [theta0 + theta1 * x_val for x_val in x_range]
plt.plot(x_range, y_range, color='red', label='Regression Line')

# Add titles and labels
plt.title("Mileage vs Price of Cars with Regression Line")
plt.xlabel("Mileage (km)")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()
