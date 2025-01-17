import numpy as np
import pandas as pd

# Load the dataset
data_path = "data.csv"  # Ensure the dataset is in the same directory as this script
data = pd.read_csv(data_path)

# Extract features (x) and target (y)
x = data['km'].values
y = data['price'].values

# Normalize the data for better gradient descent performance
x_mean = np.mean(x)
x_std = np.std(x)
x_normalized = (x - x_mean) / x_std

y_mean = np.mean(y)
y_std = np.std(y)
y_normalized = (y - y_mean) / y_std

# Gradient Descent Parameters
alpha = 0.01  # Learning rate
iterations = 1000  # Number of iterations
m = len(x)  # Number of examples

# Initialize theta values
theta0 = 0
theta1 = 0

def compute_cost(theta0, theta1, x, y):
    """Compute the cost function J."""
    predictions = theta0 + theta1 * x
    errors = predictions - y
    return (1 / (2 * m)) * np.sum(errors**2)

def gradient_descent(x, y, theta0, theta1, alpha, iterations):
    """Perform gradient descent to learn theta0 and theta1."""
    for i in range(iterations):
        predictions = theta0 + theta1 * x
        errors = predictions - y

        # Update theta0 and theta1
        theta0 -= alpha * (1 / m) * np.sum(errors)
        theta1 -= alpha * (1 / m) * np.sum(errors * x)

        # Optionally print the cost for debugging
        if i % 100 == 0:
            cost = compute_cost(theta0, theta1, x, y)
            print(f"Iteration {i}: Cost {cost:.4f}, theta0 {theta0:.4f}, theta1 {theta1:.4f}")

    return theta0, theta1

if __name__ == "__main__":
    print("Training Linear Regression Model...")

    # Perform gradient descent
    theta0, theta1 = gradient_descent(x_normalized, y_normalized, theta0, theta1, alpha, iterations)

    # Un-normalize theta values for predictions
    theta1 = theta1 * (y_std / x_std)
    theta0 = theta0 * y_std + y_mean - theta1 * x_mean

    print(f"Training completed. Final values: theta0 = {theta0:.4f}, theta1 = {theta1:.4f}")

    # Save the results to a file
    with open("model_parameters.txt", "w") as file:
        file.write(f"theta0: {theta0}\n")
        file.write(f"theta1: {theta1}\n")

    print("Model parameters saved to 'model_parameters.txt'.")
