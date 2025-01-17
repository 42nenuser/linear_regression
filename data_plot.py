import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("data.csv")  # Replace with your file path if necessary

# Extract mileage (x) and price (y)
x = data['km']
y = data['price']

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', alpha=0.7, label='Data Points')
plt.title("Mileage vs Price of Cars")
plt.xlabel("Mileage (km)")
plt.ylabel("Price")
plt.grid(True)
plt.legend()
plt.show()
