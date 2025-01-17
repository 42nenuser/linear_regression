import pandas as pd
import numpy as np

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

# Define the hypothesis function
def predict_price(mileage):
    return theta0 + theta1 * mileage

# Calculate precision using Mean Squared Error (MSE)
def calculate_mse(x, y):
    predictions = [predict_price(mileage) for mileage in x]
    mse = np.mean((y - predictions) ** 2)
    return mse

# Calculate R-squared (R²)
def calculate_r2(x, y):
    predictions = [predict_price(mileage) for mileage in x]
    ss_total = np.sum((y - np.mean(y)) ** 2)
    ss_residual = np.sum((y - predictions) ** 2)
    r2 = 1 - (ss_residual / ss_total)
    return r2

if __name__ == "__main__":
    # Calculate precision metrics
    mse = calculate_mse(x, y)
    r2 = calculate_r2(x, y)

    # Print the results
    print("Precision of the Linear Regression Model:")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"R-squared (R²): {r2:.2f}")
