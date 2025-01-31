import joblib
import os
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Get the absolute path of the Django project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Corrected path to the saved model
model_path = os.path.join(BASE_DIR, 'linear_regression_model.pkl')

# Print to verify path
print(f"Looking for model at: {model_path}")

# Load the trained model
try:
    model = joblib.load(model_path)  # Load model
except FileNotFoundError:
    raise Exception(f"Model file not found at {model_path}. Please check the file location.")

@api_view(['GET', 'POST'])  # Allow both GET and POST
def predict_price(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Use POST with {"km": value} to get predictions'})

    try:
        data = request.data  # Get JSON data from request
        km = float(data.get('km', 0))  # Extract km value
        price_pred = model.predict([[km]])[0]  # Predict price

        return JsonResponse({'predicted_price': price_pred})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
