from flask import Flask, render_template

app = Flask(__name__) # __name__ references this file

@app.route('/') # decorator

def index():
    return render_template('index.html') # knows to look in templates folder

if __name__ == '__main__':
    app.run(debug=True)

