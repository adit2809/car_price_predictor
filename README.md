```markdown
# 🚗 Car Price Predictor using Linear Regression

This project is a machine learning web app that predicts the price of a used car based on inputs like year of manufacture, kilometers driven, fuel type, and brand. It uses a Linear Regression model trained on real-world data from Quikr and is built using Python and Streamlit.

---

## 📌 Features

- Predicts car price in Indian Rupees (₹)
- Takes user input for:
  - Year of manufacture
  - Kilometers driven
  - Fuel type (Petrol, Diesel, CNG)
  - Company/brand (e.g., Maruti, Hyundai)
- Interactive web interface using Streamlit
- Linear Regression model built using Scikit-learn

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📁 Project Structure

```

car\_price\_predictor/
├── app.py               # Streamlit web app
├── car\_model.pkl        # Trained Linear Regression model
├── columns.pkl          # Column names used during training
├── quikr\_car.csv        # Dataset (optional)
├── README.md            # Project documentation
└── requirements.txt     # Required Python packages

````

---

## 🚀 How to Run the App

1. Install required packages:

```bash
pip install -r requirements.txt
````

2. Run the app:

```bash
streamlit run app.py
```

3. Open your browser and go to:

```
http://localhost:8501
```

---

## 💡 Sample Input

* Year: 2015
* Kilometers Driven: 50,000
* Fuel Type: Petrol
* Company: Hyundai

✅ **Estimated Price: ₹3,10,000**

---
