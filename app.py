from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')


db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default="Not Completed")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Task {self.id}>"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an Issue in creating your task"
    
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    
@app.route('/delete/<id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        
        return redirect('/')
    
    except:
        return "There was an Issue in deleting your task"


@app.route('/update/<id>', methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task.content = request.form['content']
        try: 
            db.session.commit()
            return redirect('/')
        except:
            return "There was an Issue in updating your task"
            
    else:
        return render_template("update.html", task=task)


@app.route('/status/<id>')
def status(id):
    task = Todo.query.get_or_404(id)
    
    task.completed = "Completed"
    try: 
        db.session.commit()
        return redirect('/')
    except:
        return "There was an Issue in updating your task"



if __name__ == "__main__":
    app.run(debug=True)