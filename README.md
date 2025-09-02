🎓 AI-Based Student Performance and Guidance System

This is a Flask-based web application that predicts student performance using a trained Machine Learning model.
The system takes marks in multiple subjects along with attendance as input and provides:


✅ Pass/Fail Prediction

📊 Percentage Calculation

📚 Subject-wise Weakness Analysis

🎯 Personalized Learning Platform Suggestions (e.g., Khan Academy, BYJU’s, EnglishClass101, etc.)


🔧 Features

Input subject scores (Maths, Telugu, English, Science, Social, Hindi, etc.) and attendance.

ML-based Pass/Fail prediction.

Automatic percentage calculation.

Identifies weak subjects.

Recommends online platforms for improvement.

Simple Flask web interface for user interaction.



🛠 Tech Stack

Python (Machine Learning + Backend)

Flask (Web Framework)

HTML, CSS, JavaScript (Frontend)

Scikit-learn / Pandas / NumPy (ML + Data Handling)



📂 Project Structure

AI-Student-Performance/
│── static/                # CSS, JS, Images

│── templates/             # HTML files

│── model/                 # ML Model files

│── app.py                 # Flask main application

│── requirements.txt       # Dependencies

│── README.md              # Project Documentation



🚀 Installation & Usage

1. Clone the repository

git clone https://github.com/yourusername/AI-Student-Performance.git
cd AI-Student-Performance

2. Install dependencies

pip install -r requirements.txt

3. Run the Flask app

python app.py

4. Open in browser

http://127.0.0.1:5000/

📊 Example Workflow

1. Enter marks for each subject and attendance.

2. Click Predict.

3. Get results:

  Pass/Fail status

  Percentage score

  Weak subject analysis

  Personalized platform suggestions

📜 License

This project is open-source under the MIT License.
