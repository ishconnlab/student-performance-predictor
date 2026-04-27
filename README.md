🎓 Student Performance Predictor

A Machine Learning web application that predicts a student's final grade based on academic history and lifestyle factors.

🚀 Overview

This project uses a Random Forest Regression model to estimate a student's final grade (G3) using:

Academic performance (G1, G2)
Study habits
Lifestyle factors

The app provides:

🎯 Grade prediction
📊 Performance classification
💡 Personalized improvement tips
🧠 How It Works
User enters student details in the web interface
Data is sent to a trained ML model
Model predicts final grade
App displays:
Predicted grade
Performance level
Suggestions for improvement
📊 Input Features
Feature	Description
age	Student age
absences	Number of absences
failures	Past class failures
studytime	Weekly study time (1–4)
goout	Social activity level (1–5)
health	Health status (1–5)
freetime	Free time (1–5)
traveltime	Travel time to school (1–4)
Walc	Weekend alcohol consumption (1–5)
Fedu	Father's education level (0–4)
G1	First period grade
G2	Second period grade
🎯 Output Classes
Grade Range	Status
0 – 9	⚠️ Needs Improvement
10 – 14	👍 Average
15 – 20	🎉 Excellent
🛠 Tech Stack
Python
Flask
Scikit-learn
Pandas
Joblib
Tailwind CSS
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/ishconnlab/student-performance-predictor.git
cd student-performance-predictor
2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
4. Train the model
python train_model.py
5. Run the application
python app.py
🧪 Example

Input:

G1: 17
G2: 18

Output:

Predicted Grade: 18.22 (Excellent 🎉)
🧠 Model Details
Algorithm: RandomForestRegressor
Trees: 300
Max Depth: 12
Target: Final Grade (G3)
📌 Key Insight

👉 G1 and G2 are the strongest predictors
Adding them significantly improves accuracy.

🚀 Future Improvements
📊 Data visualization (charts)
🎯 Target grade simulator
🧠 Feature importance explanation
🌐 Deployment (Render / Vercel)
👨‍💻 Author

IshConnLab
🚀 Building intelligent systems with Machine Learning

⭐ Support

If you like this project, give it a ⭐ on GitHub!
