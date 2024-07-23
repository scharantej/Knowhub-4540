
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///knowledge_hub.db'
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    platform = db.Column(db.String(50))
    progress = db.Column(db.Integer)
    completed = db.Column(db.Boolean)

# Define the routes
@app.route('/')
def index():
    """Render the home page."""
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@app.route('/courses')
def courses():
    """Render the courses page."""
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/progress')
def progress():
    """Render the progress page."""
    courses = Course.query.all()
    return render_template('progress.html', courses=courses)

@app.route('/add_course', methods=['POST'])
def add_course():
    """Add a new course to the database."""
    title = request.form.get('title')
    platform = request.form.get('platform')
    progress = request.form.get('progress')
    completed = request.form.get('completed')
    new_course = Course(title=title, platform=platform, progress=progress, completed=completed)
    db.session.add(new_course)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update_progress', methods=['POST'])
def update_progress():
    """Update the progress of a course in the database."""
    course_id = request.form.get('course_id')
    progress = request.form.get('progress')
    course = Course.query.get(course_id)
    course.progress = progress
    db.session.commit()
    return redirect(url_for('progress'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
