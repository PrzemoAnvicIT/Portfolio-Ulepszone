import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from models import db, User, Content, Skill
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'img')
# Ensure the data directory exists
data_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
os.makedirs(data_dir, exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(data_dir, 'content.db')
db.init_app(app)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    content = Content.query.first()
    skills = Skill.query.all()
    return render_template('index.html', content=content, skills=skills)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return "Invalid credentials!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    content = Content.query.first()
    skills = Skill.query.all()
    if request.method == 'POST':
        content.about_me = request.form['about_me']
        
        for skill in skills:
            skill.info = request.form[f"{skill.name}_info"]
            
            image_file = request.files.get(f"{skill.name}_image")
            if image_file and image_file.filename != '':
                filename = secure_filename(image_file.filename)
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                
                # Ensure the directory exists
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                
                image_file.save(image_path)
                skill.image = filename

        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('admin.html', content=content, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
