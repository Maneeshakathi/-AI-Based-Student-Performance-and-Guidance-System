from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    subjects = ['Maths', 'Telugu', 'Hindi', 'English', 'Science', 'Social']
    inputs = [int(request.form[sub]) for sub in subjects]
    attendance = int(request.form['attendance'])

    full_input = inputs + [attendance]
    prediction = model.predict([full_input])[0]

    total_marks = sum(inputs)
    percentage = round(total_marks / (len(subjects) * 100) * 100, 2)

    failed_subjects = [subject for subject, mark in zip(subjects, inputs) if mark < 35]
    status = "Fail" if failed_subjects else "Pass"

    platform_names = {
        'Maths': 'Khan Academy',
        'Telugu': 'Typing Baba (Telugu)',
        'Hindi': 'Typing Baba (Hindi)',
        'English': 'EnglishClass101',
        'Science': 'LearnCBSE',
        'Social': "BYJU'S"
    }

    suggestions = {}
    for subject, mark in zip(subjects, inputs):
        if (status == "Fail" and mark < 35) or (status == "Pass" and mark < 60):
            suggestions[subject] = platform_names[subject]

    if status == "Pass":
        message = f"✅ Great job! You passed with {percentage}%. Keep pushing to improve your weaker subjects."
    else:
        message = f"❌ You failed with {percentage}%. Focus on the subjects below to improve your performance."

    scores = dict(zip(subjects, inputs))

    return render_template(
        'result.html',
        result=message,
        scores=scores,
        suggestions=suggestions,
        percentage=percentage,
        status=status
    )

if __name__ == '__main__':
    app.run(debug=True)
