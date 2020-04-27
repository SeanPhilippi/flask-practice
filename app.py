from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # __name__ references this file
# tells apps where database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # 3 /'s is relative path, 4 for absolute path
# initialize database
db = SQLAlchemy(app)

# creating a model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) # don't want this to be blank
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # representation
    def __repr__(self):
        return '<Task %r>' % self.id

# decorator
@app.route('/', methods=['POST', 'GET'])

def index():
    if request.method == 'POST':
        task_content = request.form['content'] # id of the form input for content wanted
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        # querying all Todo database contents, ordering them by date created, and grabbing all of them
        tasks = Todo.query.order_by(Todo.date_created).all()
        # pass created variable to index.html template
        return render_template('index.html', tasks=tasks) # knows to look in templates folder

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

if __name__ == '__main__':
    app.run(debug=True)

