from flask import Flask, render_template, redirect, url_for


app= Flask(__name__)



@app.route('/')
@app.route('/home/')
def home():
    return render_template('index.html')

@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/tasks/')
def notsignedin():
    return redirect(url_for("register"))




if __name__ == '__main__':
    app.run(debug=True)


