from flask import Flask, render_template, request, redirect, url_for,make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database1.sqlite3'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    register_number = db.Column(db.String(20), unique=True, nullable=False)
    year = db.Column(db.String(10), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    marks = db.Column(db.Integer, nullable=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    choice1 = db.Column(db.String(255), nullable=False)
    choice2 = db.Column(db.String(255), nullable=False)
    choice3 = db.Column(db.String(255), nullable=False)
    choice4 = db.Column(db.String(255), nullable=False)
    correct_choice = db.Column(db.Integer, nullable=False)

class Java_ques(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    choice1 = db.Column(db.String(255), nullable=False)
    choice2 = db.Column(db.String(255), nullable=False)
    choice3 = db.Column(db.String(255), nullable=False)
    choice4 = db.Column(db.String(255), nullable=False)
    correct_choice = db.Column(db.Integer, nullable=False)

class C_ques(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    choice1 = db.Column(db.String(255), nullable=False)
    choice2 = db.Column(db.String(255), nullable=False)
    choice3 = db.Column(db.String(255), nullable=False)
    choice4 = db.Column(db.String(255), nullable=False)
    correct_choice = db.Column(db.Integer, nullable=False)
with app.app_context():
    db.create_all()
# ... other routes and configurations
#questions = Question.query.all()

@app.route('/')
def front():
    return render_template('front.html')
@app.route('/student', methods=['GET', 'POST'])
def student():
    subjects = ['Python', 'Java', 'C']
    if request.method == 'POST':
        name = request.form['name']
        register_number = request.form['rno']
        year = request.form['year']
        subject = request.form['subject']
        new_student = Student(name=name, register_number=register_number, year=year, subject=subject)
        db.session.add(new_student)
        db.session.commit() 
    
    #    print("success")
        
        return redirect(url_for('student'))
    
    return render_template('student.html', subjects=subjects)    


@app.route('/faculty')
def faculty():
    students = Student.query.all()
    return render_template('faculty.html', students = students)
@app.route('/quiz')
def index():
    questions = Question.query.all()
    return render_template('index1.html', questions=questions)

@app.route('/javaquiz')
def index1():
    questions = Java_ques.query.all()
    return render_template('index2.html', questions=questions)
@app.route('/cquiz')
def index2():
    questions = C_ques.query.all()
    return render_template('index3.html', questions=questions)

@app.route('/result', methods=['POST'])
    
def result():
    questions = Question.query.all()
    
    student=request.form["student"]
    student_data=db.session.query(Student).filter_by(register_number=student).first()
    print(student_data)
    print(student)
    questions_as_dicts = [{'id': question.id, 'ans': question.correct_choice} for question in questions]
    print(questions_as_dicts)
    print(questions)
    l=[]
    num_questions = len(questions)
    user_answers = dict()
    score = 0
    for question in questions:
        question_id = question.id
        correct_choice=question.correct_choice
        user_answer_choice = 'choice' + str(request.form.get(f'question{question_id}'))
        user_answers[question_id] = user_answer_choice
        choice=f"{user_answers[question_id]}"
        user_choice = getattr(question, choice)
        if user_choice == correct_choice:
            score+=1
    setattr(student_data,"marks",score)
    db.session.commit()
    print(score)
    print(user_answers)

    return render_template('result.html', questions=questions, user_answers=user_answers, num_questions=num_questions,rno=student)

@app.route('/result1', methods=['POST'])
    
def result1():
    questions = Java_ques.query.all()
    
    student=request.form["student"]
    student_data=db.session.query(Student).filter_by(register_number=student).first()
    print(student_data)
    print(student)
    questions_as_dicts = [{'id': question.id, 'ans': question.correct_choice} for question in questions]
    print(questions_as_dicts)
    print(questions)
    l=[]
    num_questions = len(questions)
    user_answers = dict()
    score = 0
    for question in questions:
        question_id = question.id
        correct_choice=question.correct_choice
        user_answer_choice = 'choice' + str(request.form.get(f'question{question_id}'))
        user_answers[question_id] = user_answer_choice
        choice=f"{user_answers[question_id]}"
        user_choice = getattr(question, choice)
        if user_choice == correct_choice:
            score+=1
    setattr(student_data,"marks",score)
    db.session.commit()
    print(score)
    print(user_answers)

    return render_template('result.html', questions=questions, user_answers=user_answers, num_questions=num_questions,rno=student)

@app.route('/result2', methods=['POST'])
    
def result2():
    questions = C_ques.query.all()
    
    student=request.form["student"]
    student_data=db.session.query(Student).filter_by(register_number=student).first()
    print(student_data)
    print(student)
    questions_as_dicts = [{'id': question.id, 'ans': question.correct_choice} for question in questions]
    print(questions_as_dicts)
    print(questions)
    l=[]
    num_questions = len(questions)
    user_answers = dict()
    score = 0
    for question in questions:
        question_id = question.id
        correct_choice=question.correct_choice
        user_answer_choice = 'choice' + str(request.form.get(f'question{question_id}'))
        user_answers[question_id] = user_answer_choice
        choice=f"{user_answers[question_id]}"
        user_choice = getattr(question, choice)
        if user_choice == correct_choice:
            score+=1
    setattr(student_data,"marks",score)
    db.session.commit()
    print(score)
    print(user_answers)

    return render_template('result.html', questions=questions, user_answers=user_answers, num_questions=num_questions,rno=student)

if __name__ == '__main__':
    app.run(debug=True)
