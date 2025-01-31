# 🚗 Car Price Prediction Web App

This project is a **machine learning-powered web application** that predicts **car prices** based on the number of kilometers driven. It uses a **pre-trained Linear Regression model** and serves predictions via a **Django REST API** with a simple **HTML, CSS, and JavaScript frontend**.

---

## **🛠️ Technologies Used**
### **🔹 Backend**
- **Django** – Web framework for handling API requests.
- **Django REST Framework (DRF)** – For building the REST API.
- **Joblib** – For loading the trained machine learning model.
- **Scikit-learn** – For training the linear regression model.

### **🔹 Frontend**
- **HTML** – Structure of the web interface.
- **CSS** – Styling and layout.
- **JavaScript (Vanilla JS)** – To send requests to the Django API.

### **🔹 Machine Learning**
- **Linear Regression** – Predicts car prices based on kilometers driven.
- **Scikit-learn** – For model training and saving.

### **🔹 Deployment & Containerization**
- **Docker** – Containerizes the application for easy deployment.
- **Gunicorn** – Production-ready WSGI server for Django.

---

## **🚀 Features**
✅ **Predicts car prices based on kilometers driven.**  
✅ **REST API built with Django to serve predictions.**  
✅ **Interactive web frontend for user input.**  
✅ **Dockerized application for easy deployment.**  
✅ **Lightweight and fast with no database required.**  

---

## **📂 Project Structure**
```
car_price_project/
├── car_price_project/        # Django project (settings, URLs, WSGI)
├── predictor/                # Django app (API, ML model)
│   ├── static/               # CSS & JavaScript files
│   ├── templates/predictor/  # Frontend (index.html)
│   ├── views.py              # API logic for price prediction
│   ├── model.py              # ML model training script
│   ├── urls.py               # API routes
├── linear_regression_model.pkl  # Trained ML model
├── Dockerfile                # Docker configuration
├── requirements.txt          # Dependencies
├── manage.py                 # Django management script
```

---

## **🛠️ How to Run the Project Locally**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction
```

### **2️⃣ Build & Run with Docker**
```bash
docker build -t car_price_app .
docker run -p 8000:8000 car_price_app
```
Now open **`http://127.0.0.1:8000/`** in your browser.

### **3️⃣ (Optional) Running Without Docker**
```bash
pip install -r requirements.txt
python manage.py runserver
```

---

## **📌 API Usage**
### **Endpoint:** `POST /api/predict/`
Send a **JSON request**:
```json
{
    "km": 120000
}
```
Response:
```json
{
    "predicted_price": 4500.0
}
```

---

## **🚀 Future Improvements**
- 📌 Add more car features for better predictions.
- 📌 Store past predictions in a database.
- 📌 Deploy online using Render, Heroku, or a VPS.
- 📌 Improve UI with better design.

---



---

