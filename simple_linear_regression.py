# Initial implementation of a price prediction program
# Using the hypothesis: estimatePrice(mileage) = theta0 + (theta1 * mileage)

# Load trained theta values from file
try:
    with open("model_parameters.txt", "r") as file:
        lines = file.readlines()
        theta0 = float(lines[0].split(":")[1].strip())
        theta1 = float(lines[1].split(":")[1].strip())
except FileNotFoundError:
    print("Error: Model parameters not found. Please run the training program first.")
    exit()

def predict_price(mileage):
    """
    Predict the price of a car given its mileage using the hypothesis.
    
    Parameters:
        mileage (float): The mileage of the car.
        
    Returns:
        float: The predicted price.
    """
    return theta0 + (theta1 * mileage)

if __name__ == "__main__":
    print("Car Price Prediction Program")
    try:
        # Prompt user for mileage input
        mileage = float(input("Enter the mileage of the car (in km): "))
        
        # Predict and display the price
        predicted_price = predict_price(mileage)
        print(f"The estimated price for a car with {mileage} km is: {predicted_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value for mileage.")
