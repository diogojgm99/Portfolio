from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

### To create file .db, activate env then python3 following by 'from app import db' then db.create_all()
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    begin_time = db.Column(db.String(200), nullable=False)
    end_time = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
        data = [
            request.form['content'],
            request.form['begin_time'],
            request.form['end_time']
        ]
        
        new_task = Todo(content=data[0],begin_time=data[1], end_time=data[2])
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Theres was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        task.begin_time = request.form['begin_time']
        task.end_time = request.form['end_time']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating task'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)

