from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # __name__ references this file
# tells apps where database is located
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # 3 /'s is relative path, 4 for absolute path
# initialize database
db = SQLAlchemy(app)

# creating a model
class Todo(db.Model):
    id = db.Column(db.Intgeter, primary_key=True)
    content = db.Column(db.String(200), nullable=False) # don't want this to be blank
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # representation
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/') # decorator

def index():
    return render_template('index.html') # knows to look in templates folder

if __name__ == '__main__':
    app.run(debug=True)

