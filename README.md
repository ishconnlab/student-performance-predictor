# 🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's final academic performance based on behavioral patterns, lifestyle factors, and prior grades.

---

## 🚀 Overview

This project leverages a **Random Forest Regression model** to estimate a student’s final grade (**G3**) using a combination of:

* 📚 Academic history (**G1, G2**)
* ⏱ Study habits
* 🌐 Lifestyle and social behavior

The application delivers:

* 🎯 Accurate grade predictions
* 📊 Performance classification
* 💡 Actionable improvement insights

---

## 🧠 How It Works

1. Users input student data via a web interface
2. The data is processed and structured into a feature vector
3. A trained ML model generates a prediction
4. The system returns:

   * Predicted final grade
   * Performance category
   * Personalized recommendations

---

## 📊 Input Features

| Feature    | Description                       |
| ---------- | --------------------------------- |
| age        | Student age                       |
| absences   | Number of school absences         |
| failures   | Number of past academic failures  |
| studytime  | Weekly study time (1–4 scale)     |
| goout      | Social activity level (1–5)       |
| health     | Health status (1–5)               |
| freetime   | Free time availability (1–5)      |
| traveltime | Travel time to school (1–4)       |
| Walc       | Weekend alcohol consumption (1–5) |
| Fedu       | Father's education level (0–4)    |
| **G1**     | First period grade                |
| **G2**     | Second period grade               |

---

## 🎯 Output Classification

| Grade Range | Performance Level    |
| ----------- | -------------------- |
| 0 – 9       | ⚠️ Needs Improvement |
| 10 – 14     | 👍 Average           |
| 15 – 20     | 🎉 Excellent         |

---

## 🛠 Technology Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn (RandomForestRegressor)
* **Data Processing:** Pandas
* **Model Persistence:** Joblib
* **Frontend:** Tailwind CSS

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ishconnlab/student-performance-predictor.git
cd student-performance-predictor
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python train_model.py
```

### 5. Run the Application

```bash
python app.py
```

---

## 🧪 Example

**Input:**

```
G1: 17
G2: 18
```

**Output:**

```
Predicted Grade: 18.22 (Excellent 🎉)
```

---

## 🧠 Model Details

* **Algorithm:** Random Forest Regressor
* **Number of Trees:** 300
* **Max Depth:** 12
* **Target Variable:** Final Grade (G3)

---

## 📌 Key Insight

> **G1 and G2 are the most influential features** in predicting final performance.
> Incorporating prior academic results significantly enhances model accuracy.

---

## 🚀 Future Enhancements

* 📊 Interactive data visualizations
* 🎯 Target grade simulation
* 🧠 Model explainability (feature importance)
* 🌐 Cloud deployment (Render / Vercel)

---

## 👨‍💻 Author

**IshConnLab**
🚀 Building intelligent systems with Machine Learning

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub to support its development.
