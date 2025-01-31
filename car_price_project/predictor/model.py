import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset (replace with the actual path if necessary)
df = pd.read_csv("dat.csv")

# Extract features (X) and target variable (y)
X = df[['km']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()  # Create a model instance
model.fit(X_train, y_train)  # Train the model
joblib.dump(model, 'linear_regression_model.pkl')
